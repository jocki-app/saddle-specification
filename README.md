# SADDLE v1

**Sidecar Archive for Description, Distributed state, Lineage, and Exchange.**

SADDLE gives any ordinary file or folder an optional, independent archive. The original file remains directly usable by other applications. Metadata, retained versions and approved synchronization travel with the unit rather than relying on an enclosing application database.

Read the [specification](specification/README.md), use the [TypeScript SDK](https://github.com/jocki-app/saddle-typescript-sdk), [Python SDK](https://github.com/jocki-app/saddle-python-sdk), or [CLI](https://github.com/jocki-app/saddle-cli). The [documentation website](https://jocki-app.github.io/saddle-website/) includes examples.

This is version 1. Writers use the version 1 identifiers and reject unknown major formats; there is no compatibility import layer.

Licensed under GPL-3.0-only. See [LICENSE](LICENSE).

## Reference and verification

Read the numbered chapters in `specification/`: unit boundaries, binary layout, metadata, history, sharing, conformance, record models, and implementation guidance. The [published site](https://jocki-app.github.io/saddle-website/) renders the same revisioned source. Core resource shapes are in `schemas/`; byte and metadata cases are in `conformance/v1/`.

Install `requirements-dev.txt` with pip, then run `python3 scripts/check.py`. The TypeScript and Python SDKs run the shared fixture snapshot plus their own runtime tests. See [RELEASING.md](RELEASING.md) for document revisions, wire-major rules and versioned releases. The standard does not require Jocki, a central database, or a workspace to read a file’s archive.
