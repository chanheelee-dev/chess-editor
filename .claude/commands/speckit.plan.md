---
description: Create a technical implementation plan from a feature specification
---

<!-- Source: spec-kit -->

Create a technical implementation plan from the feature specification.

**Steps:**
1. Find the target spec file in `.specify/specs/` (most recent, or specified by user)
2. Read `.specify/memory/constitution.md` for project constraints
3. Read the spec file thoroughly
4. Resolve any `[NEEDS CLARIFICATION]` items through research or user questions
5. Create `.specify/specs/NN-feature-name-plan.md` from `.specify/templates/plan-template.md`:
   - Extract technical context (language, framework, dependencies)
   - Perform constitution check (verify alignment with principles)
   - Design architecture (files to modify/create, data models)
   - Document complexity justifications for non-simple decisions
6. Validate: plan must be fully implementable without additional clarification
7. Report: plan file path, key decisions made, any remaining open questions

**Constraints:**
- Error on gate failures (constitution violations or unresolved clarifications)
- Use absolute paths in file references
- Choose the simplest architecture that satisfies the spec

$ARGUMENTS
