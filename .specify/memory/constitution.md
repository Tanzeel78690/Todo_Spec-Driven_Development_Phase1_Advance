<!--
---
version_change: "1.0.0 → 1.1.0"
modified_principles:
  - "Spec-Driven Development → Spec-first development"
  - "Process over Manual Coding → Incremental feature progression"
  - "Clarity & Simplicity → Clarity and simplicity for console-based user experience"
  - "Reproducibility → Maintainability and clean Python architecture"
  - "Clean Code Discipline → Deterministic behavior"
added_sections:
  - "Development standards"
  - "Feature scope"
  - "Constraints"
  - "Documentation & traceability"
  - "Validation & success criteria"
removed_sections:
  - "Key Standards and Constraints"
  - "Project Definition"
  - "Scope"
  - "Success Criteria"
templates_requiring_updates:
  - path: ".specify/templates/plan-template.md"
    status: "✅ updated"
  - path: ".specify/templates/spec-template.md"
    status: "✅ updated"
  - path: ".specify/templates/tasks-template.md"
    status: "✅ updated"
  - path: "README.md"
    status: "⚠ pending"
todos: []
---
-->
# Spec-driven, agentic development of a CLI-based Todo application using Gemini CLI and SpecKitPlus.

## Core principles

### I. Spec-first development
All implementation must strictly follow specifications generated through Spec-Kit Plus and executed via approved agentic workflows. No manual coding is permitted; all code must be generated from specs.

### II. Incremental feature progression
Features will be developed in stages, from Basic to Intermediate to Advanced, allowing for iterative development and testing.

### III. Clarity and simplicity for console-based user experience
The console interface should be intuitive and easy to use, prioritizing a straightforward user experience.

### IV. Maintainability and clean Python architecture
Code should be readable, modular, and follow single-responsibility principles to ensure long-term maintainability.

### V. Deterministic behavior
The application should have no hidden state and produce predictable outputs for the same inputs.

## Development standards

- **Language**: Python 3.13+
- **Interface**: Command-line (interactive menu-based)
- **Data storage**: In-memory only (no files, no databases)
- **Code quality**: Readable, modular, single-responsibility functions
- **Error handling**: Graceful handling of invalid inputs

## Feature scope

- **Basic Level**: Add, Delete, Update, View, Mark Complete
- **Intermediate Level**: Priorities, Tags/Categories, Search, Filter, Sort
- **Advanced Level**: Recurring Tasks, Due Dates, Time-based Reminders

## Constraints

- No external dependencies beyond Python standard library
- No persistence between runs
- No UI frameworks (CLI only)
- All features must be toggleable and testable via CLI

## Documentation & traceability

- Every feature must map back to a specification.
- Specs must be stored in `specs/`.
- Code structure must reflect spec structure.
- `README.md` must explain setup and usage.
- `GEMINI.md` must document agent instructions.

## Validation & success criteria

- All listed features function correctly via CLI.
- User can manage tasks end-to-end in one session.
- No crashes on invalid input.
- Code passes basic linting and logical review.
- Generated code strictly follows the approved specs.

## Governance

- **Supremacy**: This Constitution supersedes all other practices and ad-hoc decisions.
- **Compliance**: All development activities, code reviews, and pull requests must verify compliance with the principles and standards outlined herein.
- **Amendments**: Amendments require documentation, team approval, and a clear migration plan for existing artifacts.

**Version**: 1.1.0 | **Ratified**: TODO(RATIFICATION_DATE) | **Last Amended**: 2026-01-02