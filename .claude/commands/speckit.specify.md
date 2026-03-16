---
description: Create a feature specification focusing on WHAT and WHY, not HOW
---

<!-- Source: spec-kit -->

Create a new feature specification based on the user's description.

**Steps:**
1. Generate a short branch name (2-4 words, action-noun format, e.g., `feat/fen-support`)
2. Determine next spec number from existing files in `.specify/specs/`
3. Copy `.specify/templates/spec-template.md` → `.specify/specs/NN-feature-name.md`
4. Fill in the template based on user's description:
   - Focus on user value (WHAT/WHY), NOT implementation (HOW)
   - Write user stories with Given/When/Then acceptance criteria
   - Mark ambiguities with `[NEEDS CLARIFICATION]` (max 3)
   - Make reasonable assumptions; document them
5. Validate spec quality:
   - Each user story delivers value independently
   - Success criteria are measurable and technology-agnostic
   - No implementation details in the spec
6. If clarifications needed, present them as a table with suggested options
7. Report: spec file path, branch name, readiness status

**Target audience:** Business stakeholders, not engineers
**Focus:** User outcomes, not technical decisions

$ARGUMENTS
