---
description: Generate an actionable task list from a feature plan
---

<!-- Source: spec-kit -->

Generate a dependency-ordered task list from the feature plan.

**Steps:**
1. Find the target plan file in `.specify/specs/` (most recent, or specified)
2. Read the plan, spec, and constitution
3. Create `.specify/specs/NN-feature-name-tasks.md` from `.specify/templates/tasks-template.md`
4. Organize tasks by phase:
   - Phase 1: Setup (branch, environment)
   - Phase 2: Foundational (blocking prerequisites - must complete before user stories)
   - Phase 3-N: User Stories (by priority P1→P2→P3, each independently testable)
   - Final: Polish (cross-cutting concerns)
5. Mark each task with:
   - `[TID]` unique task ID
   - `[P]` if parallelizable (different files, no dependencies)
   - `[USN]` which user story it belongs to
   - Exact file path in description
6. Report: tasks file path, total count, dependency notes

**Task format:** `- [ ] [T001] [P] [US1] Description with src/file/path.py`
**Principle:** Each user story must be independently implementable and testable

$ARGUMENTS
