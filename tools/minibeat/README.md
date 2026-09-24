# Pink Cat (free heartbeat for a self-hosted workspace) · module minibeat

Part of the ThreadCat lab tooling. Free, local, stdlib-only Python.

## Status: PENDING PI ADOPTION; fixture tests pass

Fixture tests pass (3/3) against a throwaway git repo. Needs a run on the Mac Mini, not just the sandbox.

One pulse: repo sync state, uncommitted file count, and an optional
HEARTBEAT.md stamp. Designed for the Mac Mini self-host loop. Nudge
discipline is the caller's job: the tool reports, it never sends
anything. Smoke-tested only in the build sandbox so far.
