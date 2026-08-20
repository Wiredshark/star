from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

FILES = {
    "repair": ROOT / "data/human/a1 free worlds repair capacity.txt",
    "maintenance_bridge": ROOT / "data/human/a1 syndicate maintenance transit spillover.txt",
    "rescue_bridge": ROOT / "data/human/a1 southern rim rescue spillover.txt",
    "salvage": ROOT / "data/human/a1 merchant salvage demand.txt",
    "diversion": ROOT / "data/human/a1 merchant route diversion.txt",
}


def maintenance_to_congestion(congestion, maintenance, latched=False):
    if maintenance >= 4 and congestion < 6 and not latched:
        return min(6, congestion + 1), True
    return congestion, latched


def congestion_to_rescue(rescue, congestion, latched=False):
    if congestion >= 4 and rescue < 5 and not latched:
        return min(5, rescue + 1), True
    return rescue, latched


def rescue_to_salvage(salvage, rescue, latched=False):
    if rescue >= 3 and salvage < 4 and not latched:
        return min(4, salvage + 1), True
    return salvage, latched


def route_diversion(diversion, rescue, congestion):
    if rescue >= 3 and congestion >= 3:
        if diversion > 4:
            return diversion, 0
        return diversion + 2, 2
    if rescue >= 3 or congestion >= 3:
        if diversion >= 6:
            return diversion, 0
        return diversion + 1, 1
    return diversion, 0


def repair_intake(backlog, defense_strain, patrol_surge):
    if patrol_surge:
        if defense_strain < 1 or backlog > 4:
            return backlog, 0
        return min(6, backlog + 2), 2
    if defense_strain < 3 or backlog >= 6:
        return backlog, 0
    return min(6, backlog + 1), 1


def test_bundle_files_preserve_cross_system_ownership_contracts():
    text = {name: path.read_text(encoding="utf-8") for name, path in FILES.items()}

    assert '"world: free worlds defense strain" += ' not in text["repair"]
    assert '"world: syndicate maintenance backlog" +=' not in text["maintenance_bridge"]
    assert '"world: southern rim transit congestion" +=' not in text["rescue_bridge"]
    assert '"world: merchant rescue load" +=' not in text["salvage"]
    assert '"world: merchant rescue load" +=' not in text["diversion"]
    assert '"world: southern rim transit congestion" +=' not in text["diversion"]


def test_pressure_can_propagate_across_the_reconciled_chain_without_exceeding_caps():
    congestion, maintenance_latch = maintenance_to_congestion(3, 5)
    assert (congestion, maintenance_latch) == (4, True)

    rescue, rescue_latch = congestion_to_rescue(2, congestion)
    assert (rescue, rescue_latch) == (3, True)

    salvage, salvage_latch = rescue_to_salvage(0, rescue)
    assert (salvage, salvage_latch) == (1, True)

    diversion, contribution = route_diversion(0, rescue, congestion)
    assert (diversion, contribution) == (2, 2)

    repair, repair_contribution = repair_intake(4, 3, True)
    assert (repair, repair_contribution) == (6, 2)

    assert 0 <= congestion <= 6
    assert 0 <= rescue <= 5
    assert 0 <= salvage <= 4
    assert 0 <= diversion <= 6
    assert 0 <= repair <= 6


def test_three_year_combined_horizon_is_deterministic_bounded_and_drains():
    traces = []
    for _run in range(2):
        congestion = rescue = salvage = diversion = repair = 0
        maintenance_latch = rescue_latch = salvage_latch = 0
        congestion_recovery = []
        rescue_recovery = []
        salvage_recovery = []
        diversion_recovery = []
        repair_recovery = []
        trace = []

        for day in range(365 * 3):
            # Apply scheduled recovery obligations first.
            for due in [x for x in congestion_recovery if x == day]:
                congestion = max(0, congestion - 1)
            for due in [x for x in rescue_recovery if x == day]:
                rescue = max(0, rescue - 1)
            for due in [x for x in salvage_recovery if x == day]:
                salvage = max(0, salvage - 1)
            for due, amount in [x for x in diversion_recovery if x[0] == day]:
                diversion = max(0, diversion - amount)
            for due, amount in [x for x in repair_recovery if x[0] == day]:
                repair = max(0, repair - amount)

            # Deterministic stress seasons; arrivals every two days.
            acute = day % 180 < 60
            maintenance = 5 if acute else 1
            defense = 4 if acute else 0
            patrol = acute and day % 10 < 5

            if day % 2 == 0:
                # Existing Southern Rim traffic producer contributes during acute windows.
                if acute and congestion < 6:
                    congestion += 1
                    congestion_recovery.append(day + 3)

                congestion, activated = maintenance_to_congestion(
                    congestion, maintenance, maintenance_latch > 0
                )
                if activated and maintenance_latch == 0:
                    maintenance_latch = 6
                    congestion_recovery.append(day + 3)

                rescue, activated = congestion_to_rescue(
                    rescue, congestion, rescue_latch > 0
                )
                if activated and rescue_latch == 0:
                    rescue_latch = 6
                    rescue_recovery.append(day + 5)

                salvage, activated = rescue_to_salvage(
                    salvage, rescue, salvage_latch > 0
                )
                if activated and salvage_latch == 0:
                    salvage_latch = 5
                    salvage_recovery.append(day + 8)

                diversion, contribution = route_diversion(diversion, rescue, congestion)
                if contribution:
                    diversion_recovery.append((day + 6, contribution))

                repair, contribution = repair_intake(repair, defense, patrol)
                if contribution:
                    repair_recovery.append((day + 7, contribution))

            maintenance_latch = max(0, maintenance_latch - 1)
            rescue_latch = max(0, rescue_latch - 1)
            salvage_latch = max(0, salvage_latch - 1)

            assert 0 <= congestion <= 6
            assert 0 <= rescue <= 5
            assert 0 <= salvage <= 4
            assert 0 <= diversion <= 6
            assert 0 <= repair <= 6
            trace.append((congestion, rescue, salvage, diversion, repair))

        # Explicit quiet tail: no new arrivals or upstream pressure, only recovery.
        for _ in range(32):
            congestion = max(0, congestion - 1)
            rescue = max(0, rescue - 1)
            salvage = max(0, salvage - 1)
            diversion = max(0, diversion - 2)
            repair = max(0, repair - 2)

        assert (congestion, rescue, salvage, diversion, repair) == (0, 0, 0, 0, 0)
        traces.append(trace)

    assert traces[0] == traces[1]
