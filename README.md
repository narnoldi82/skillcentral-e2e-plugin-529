# e2e-plugin-529

Test plugin for the SkillCentral end-to-end check of [issue #529](https://github.com/narnoldi82/skillcentral/issues/529). It has no LICENSE on purpose, so the validator shows a warning.

| Component | Path | What it does |
|---|---|---|
| Skill | `skills/e2e-hello/` | Says hello through the echo tool |
| Command | `commands/e2e-greet.md` | Prints a greeting (1.3.1) |
| Agent | `agents/e2e-helper.md` | Summarises a request in one line |
| Hook | `hooks/hooks.json` | Prints one line at session start |
| MCP server | `.mcp.json`, `scripts/echo_mcp.py` | Local stdio server with one `echo` tool. No network, no file access |
