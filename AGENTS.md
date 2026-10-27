# Instructions for agents working with WB-OPDK

Read `START_HERE.md` first. For releases or upload failures, also read `70-release-engineering/upload-package-guide.md` before choosing the package structure.

- Record the intended asset type and actual upload entry. Native Skill, Expert, Expert Team and Connector have different roots and metadata. A missing plugin manifest at an Expert entry does not mean every Skill needs that manifest.
- Current official docs define platform rules. Screenshots prove only what is visible; another assistant's explanation is not a platform error or successful upload. Obtain the original ZIP when its exact contents determine the diagnosis.
- Build with `release_check.py`; validate the exact delivered ZIP with `validate_release_zip.py --type ... --source ...`. Inspect its inventory, logical root, hidden plugin manifest where applicable, declared files and SHA256. Source-folder validation alone is insufficient.
- Keep ZIP, manifest and submission notes outside the asset directory. Preserve `.codebuddy-plugin` and required `.mcp.json`; do not filter every dotfile.
- Distinguish standalone marketplace Skill metadata, plugin metadata and embedded Skill paths. Do not silently convert product types to satisfy an error.
- Report the DevKit commit, commands, archive SHA256, tests run and tests not run. Static validation does not establish WorkBuddy parser, Runtime or review success. Upload, merge and deployment require user authorization.
- Run `python3 scripts/doctor.py --json` for release-code changes, including actual-ZIP and metadata regression tests. Change source-watch baselines only after semantic review.
