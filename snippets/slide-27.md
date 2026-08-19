## Why

Currently, the `git_log` tool returns a fixed set of fields for every commit. This can lead to excessive data transfer when only specific information (e.g., just hashes or just messages) is needed. Allowing users to specify fields improves efficiency and flexibility for AI/LLM consumption.

## What Changes

- Add an optional `fields` parameter to the `git_log` tool.
- The `fields` parameter will accept an array of strings representing the desired commit fields.
- Minimal default fields will be returned if the parameter is omitted (to maintain backward compatibility while allowing future optimization).
- The tool will only populate and return the requested fields in the JSON output.
- Optional filters and pagination options are grouped in a separate `filters` object.

