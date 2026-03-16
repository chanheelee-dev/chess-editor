---
description: Execute all tasks from the task list to implement the feature
---

<!-- Source: spec-kit -->

Implement the feature by executing tasks from the task list.

**Steps:**
1. Find the target tasks file in `.specify/specs/`
2. Read tasks.md, plan.md, spec.md for full context
3. Verify all checklist items in Phase 1 & 2 are complete (halt if not, unless user confirms)
4. Execute tasks phase by phase:
   - **Phase 2 first** (foundational - blocking prerequisites)
   - **Then user stories** in priority order (P1→P2→P3)
   - **Parallel tasks** (`[P]`) can be implemented in the same response
   - **Sequential tasks** must complete before the next starts
5. After each task:
   - Mark as complete: `- [x] [T001] ...`
   - Verify the implementation matches the spec acceptance criteria
6. After all tasks:
   - Verify all user story acceptance criteria are met
   - Run any available tests: `uv run pytest` (if tests exist)
7. Report: completion status, any deviations from plan, suggested commit message

**Principles:**
- Follow the plan; deviate only if technically necessary (document why)
- Each user story should be demonstrable when its tasks complete
- Validate against spec, not just plan

$ARGUMENTS
