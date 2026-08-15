import json
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "asset_verification" / "verify_asset.py"
# 1x1 transparent PNG.
PNG = bytes.fromhex(
    "89504e470d0a1a0a0000000d49484452000000010000000108060000001f15c489"
    "0000000d49444154789c6360000000020001e221bc330000000049454e44ae426082"
)


def git(repo, *args):
    return subprocess.run(["git", *args], cwd=repo, text=True, capture_output=True, check=True).stdout.strip()


class AssetVerificationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        git(self.repo, "init")
        git(self.repo, "config", "user.email", "test@example.invalid")
        git(self.repo, "config", "user.name", "Asset Verify Test")
        (self.repo / "candidate.png").write_bytes(PNG)
        helper = self.repo / "fake_capture.py"
        helper.write_text(
            "import os, pathlib\n"
            "p=pathlib.Path(os.environ['ASSET_VERIFY_CAPTURE_DIR'])/'proof.png'\n"
            f"p.write_bytes(bytes.fromhex('{PNG.hex()}'))\n",
            encoding="utf-8",
        )
        git(self.repo, "add", "candidate.png", "fake_capture.py")
        git(self.repo, "commit", "-m", "fixture")
        self.evidence = self.root / "evidence"

    def tearDown(self):
        self.tmp.cleanup()

    def capture(self):
        cmd = [
            "python3", str(SCRIPT), "capture",
            "--repo", str(self.repo),
            "--asset-id", "TEST-ASSET",
            "--candidate", "candidate.png",
            "--scene-id", "test-scene",
            "--capture-command", "python3 fake_capture.py",
            "--evidence-root", str(self.evidence),
        ]
        return subprocess.run(cmd, text=True, capture_output=True)

    def test_capture_and_verify_pass(self):
        result = self.capture()
        self.assertEqual(result.returncode, 0, result.stderr)
        run_id = (self.evidence / "LATEST").read_text().strip()
        receipt = self.evidence / run_id / "receipt.json"
        payload = json.loads(receipt.read_text())
        self.assertEqual(payload["status"], "PASS")
        self.assertEqual(payload["acceptance"]["status"], "PROOF_VERIFIED")
        self.assertEqual(len(payload["screenshots"]), 1)
        verify = subprocess.run(
            ["python3", str(SCRIPT), "verify", "--repo", str(self.repo), "--receipt", str(receipt), "--require-current-head"],
            text=True, capture_output=True,
        )
        self.assertEqual(verify.returncode, 0, verify.stderr)

    def test_dirty_tree_is_refused(self):
        (self.repo / "dirty.txt").write_text("dirty")
        result = self.capture()
        self.assertEqual(result.returncode, 2)
        self.assertIn("working tree is not clean", result.stderr)

    def test_uncommitted_candidate_is_refused(self):
        (self.repo / "candidate.png").write_bytes(PNG + b"x")
        result = self.capture()
        self.assertEqual(result.returncode, 2)
        self.assertTrue(
            "working tree is not clean" in result.stderr or "candidate bytes do not match HEAD" in result.stderr,
            result.stderr,
        )

    def test_receipt_becomes_stale_after_new_commit(self):
        result = self.capture()
        self.assertEqual(result.returncode, 0, result.stderr)
        run_id = (self.evidence / "LATEST").read_text().strip()
        receipt = self.evidence / run_id / "receipt.json"
        (self.repo / "later.txt").write_text("later")
        git(self.repo, "add", "later.txt")
        git(self.repo, "commit", "-m", "later")
        verify = subprocess.run(
            ["python3", str(SCRIPT), "verify", "--repo", str(self.repo), "--receipt", str(receipt), "--require-current-head"],
            text=True, capture_output=True,
        )
        self.assertEqual(verify.returncode, 2)
        self.assertIn("proof is stale for current HEAD", verify.stderr)

    def test_tampered_screenshot_is_refused(self):
        result = self.capture()
        self.assertEqual(result.returncode, 0, result.stderr)
        run_id = (self.evidence / "LATEST").read_text().strip()
        run_dir = self.evidence / run_id
        receipt = run_dir / "receipt.json"
        (run_dir / "captures" / "proof.png").write_bytes(PNG + b"tamper")
        verify = subprocess.run(
            ["python3", str(SCRIPT), "verify", "--repo", str(self.repo), "--receipt", str(receipt)],
            text=True, capture_output=True,
        )
        self.assertEqual(verify.returncode, 2)
        self.assertIn("screenshot hash mismatch", verify.stderr)


if __name__ == "__main__":
    unittest.main()
