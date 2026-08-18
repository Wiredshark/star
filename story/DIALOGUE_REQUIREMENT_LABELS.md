# Dialogue Requirement-Label Convention

Status: **A2 specialist candidate / reusable content-authoring convention**

When a player response is special because of persistent state, its choice text may begin with a concise square-bracket label. The label is presentation only. The actual authority MUST remain an adjacent stock `to display` or `to activate` condition.

- Use `to display` when the response should stay hidden until known/eligible.
- Use `to activate` when the response should stay visible but disabled until eligible.
- Do not encode hidden truth solely in the label.
- Do not create dialogue-only shadow state.
- Persistent consequences should use normal mission/action conditions and later readers.

The initial production consumer is `data/human/a2 deep security debrief.txt`, which uses `Deep: Syndicate Convoy: done` and `combat rating` as authoritative sources and gives every route a persistent later reader.
