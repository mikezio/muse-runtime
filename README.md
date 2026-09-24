# muse-runtime

System files, structure and version history for the Muse runtime.

This repo archives the Muse runtime as it exists on live instances: the file layout, the scheduler and background jobs, the memory and skill systems. Snapshots are regenerated from a running instance and updated when the runtime changes.

Instances vary. If yours looks different from what's archived here, share your snapshot and it will be added. See [snapshot/](snapshot/) for the format.

## Contents

- [docs/](docs/) - how the pieces fit together: filesystem, scheduler, memory, skills, browser, agents, toolbox, autonomy, safety
- [snapshot/](snapshot/) - live file tree, runtime info and redacted copies of actual runtime files, refreshed from the running instance
- [assets/](assets/) - architecture diagrams
- [tools/](tools/) - the snapshot generator
- [CHANGELOG.md](CHANGELOG.md) - version history

```bash
git clone https://github.com/mikezio/muse-runtime.git
```

## Contributing a snapshot

Paste the prompt in [CONTRIBUTING.md](CONTRIBUTING.md) into your Muse to generate a sanitized snapshot, then open a PR under `snapshot/variants/<your-label>/`. Shell access instead? Run `tools/snapshot.sh`. Different runtime variations are the point of the archive.

## Scope

Unofficial. Not Meta documentation. Where behavior is inferred rather than directly observed, the docs say so.
