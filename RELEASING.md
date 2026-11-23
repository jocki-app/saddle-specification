# Specification releases

`VERSION` is the document revision; binary magic and document identifiers carry their own wire version. Clarifications and additional non-breaking test vectors increment minor/patch revisions. An incompatible storage or authorization change requires a new wire major and new magic/identifiers; a prose-only version bump is insufficient.

Install `requirements-dev.txt` with pip, then run `python3 scripts/check.py`, update `VERSION`, review and commit the documents/fixtures, then push the matching `vVERSION` tag. The release workflow checks the revision, publishes a licensed specification/schema/conformance archive and computes SHA-256 checksums.

SDKs pin a specification revision in `conformance/source.json`. Update the fixture snapshot explicitly and run both SDK suites before advertising support. The documentation website updates its `reference/` snapshot using `npm run spec:update -- /path/to/saddle-specification`, followed by `npm run build && npm test`.
