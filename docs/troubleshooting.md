# Troubleshoot by layer

Start with the smallest failed operation and its timestamp. Avoid changing unrelated settings to test a theory.

| Symptom | First checks | Common mistaken conclusion |
|---|---|---|
| Remote device says online but commands fail | Live ping, then a tiny harmless command; compare last-seen time | Cached online status proves the current transport works |
| A helper vanished after a runtime recycle | Persistent home files, process state, and how the helper starts | A systemd unit added to the replaceable OS must survive |
| A daemon method is listed but returns 404 | Actual method/transport, current client/build and availability | The registry is an account capability list |
| A feature has a skill but no working tool | Account gate, connection, action permission, device prerequisites | Installed instructions grant the capability |
| Browser work is stuck | Owning task, waiting state, required user input and latest result | Start another task immediately |
| A device command fails | Device reachability and operating-system/action permission | A paired device is necessarily online |
| The model name disagrees across surfaces | Branding, selector, stored agent row, per-request metadata | Every field represents the current upstream model |
| Reasoning file says max but behavior looks unchanged | API readback and effective request fields, if exposed | Response length or timing proves effort |
| Chat forgets working context after a model switch | Model-change notice and session/context state | A side chat isolated the global setting |
| A background task was accepted but nothing arrived | Execution status, result and delivery path | Accepted means completed and delivered |
| A memory edit seems ignored | Source records, retrieval, summaries and dependent workflows | One file is the entire memory system |

## Connection checks are layered too

A remote shell bridge and the Muse application can fail independently:

1. **Bridge inventory:** is a device listed?
2. **Bridge liveness:** does it answer now?
3. **Execution:** can it run a tiny read-only command?
4. **Application:** does a supported Muse health/check request succeed?
5. **Task:** can the actual requested operation complete?

A failure at step 2 does not establish that inference or the Muse website is down. A successful shell command does not establish that every application service is healthy.

## Inspect before restarting

A restart can discard running work and transient evidence. First identify the component, its error, and the scope of the failure. For local helpers, distinguish home-persistent configuration from replaceable OS/service setup.

Do not treat host-rendered environment files as user settings. Their lifecycle and authority differ from `home.yaml`; see [configuration](configuration.md).

## Report enough evidence to be useful

A good failure report contains the build/date, interface, sanitized parameters, selected error/status fields, and whether any action may have completed before the error.

For operations with external effects, an unknown outcome needs investigation before retry. For read-only queries, use bounded retries tied to a concrete transient failure.

## Continue from the right reference

- [API surfaces](runtime-api.md): which interface exposes what.
- [Model routes](model-routes.md): routing and metadata ambiguity.
- [Feature flags](feature-flags.md): UI versus backend availability.
- [Archive workflow](archive-workflow.md): inspect changes across builds.
- [Evidence template](evidence.md): capture a reproducible finding.
