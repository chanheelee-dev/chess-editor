---
description: Create or update the project constitution with governing principles
---

<!-- Source: spec-kit -->

Load `.specify/memory/constitution.md` and update it based on the user's input.

**Steps:**
1. Read the current constitution at `.specify/memory/constitution.md`
2. Identify all bracketed placeholder tokens like `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`
3. Gather values from user conversation or infer from repository context (README, pyproject.toml, existing code)
4. Replace all placeholders with concrete values
5. Apply semantic versioning: MAJOR for incompatible changes, MINOR for new principles, PATCH for clarifications
6. Validate that no unexplained bracketed tokens remain
7. Write the completed constitution back to `.specify/memory/constitution.md`
8. Report: version change rationale and suggested commit message

**Constraints:**
- Dates use ISO format (YYYY-MM-DD)
- Principles must be declarative and testable
- Single blank line between sections; no trailing whitespace

$ARGUMENTS
