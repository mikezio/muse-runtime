# muse-runtime

System files, structure and version history for the Muse runtime.

This repo archives the Muse runtime as it exists on live instances: the file layout, the scheduler and background jobs, the memory and skill systems. Snapshots are regenerated from a running instance and updated when the runtime changes.

Instances vary. If yours looks different from what's archived here, share your snapshot and it will be added. See [snapshot/](snapshot/) for the format.

## Contents

- [docs/](docs/) - how the pieces fit together: filesystem, scheduler, memory, skills, browser, agents, toolbox, autonomy, safety
- [snapshot/](snapshot/) - live file tree, runtime info, redacted copies of actual runtime files, and the sanitized full-runtime zip ([latest release](https://github.com/mikezio/muse-runtime/releases/latest))
- [assets/](assets/) - architecture diagrams
- [tools/](tools/) - the snapshot generator
- [CHANGELOG.md](CHANGELOG.md) - version history

```bash
git clone https://github.com/mikezio/muse-runtime.git
```

## Contributing a snapshot

Paste the prompt in [CONTRIBUTING.md](CONTRIBUTING.md) into your Muse to build a sanitized zip of its runtime, then attach the zip to a release. Different runtime variations are the point of the archive.

## Scope

Unofficial. Not Meta documentation. Where behavior is inferred rather than directly observed, the docs say so.
