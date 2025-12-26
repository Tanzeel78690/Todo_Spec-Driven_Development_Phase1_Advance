<!--
Sync Impact Report:

- Version change: none -> 1.0.0
- List of modified principles:
  - Added: Spec-Driven Development
  - Added: Process over Manual Coding
  - Added: Clarity & Simplicity
  - Added: Reproducibility
  - Added: Clean Code Discipline
- Added sections:
  - Key Standards and Constraints
  - Project Definition
  - Scope
  - Success Criteria
- Removed sections:
  - None
- Templates requiring updates:
  - ⚠ pending: .specify/templates/plan-template.md
  - ⚠ pending: .specify/templates/spec-template.md
  - ⚠ pending: .specify/templates/tasks-template.md
- Follow-up TODOs:
  - TODO(RATIFICATION_DATE): Set initial ratification date.
-->

# Todo Application (Agentic, Spec-Driven) Constitution

## Core Principles

### I. Spec-Driven Development
All implementation must strictly follow specifications generated through Spec-Kit Plus and executed via approved agentic workflows.

### II. Process over Manual Coding
No manual coding is permitted. All code must be generated through Claude Code or Gemini using the Agentic Dev Stack workflow to ensure consistency and traceability.

### III. Phase-Based Evolution
The project must evolve in clearly defined phases. Each phase builds upon the previous phase without breaking traceability, governance, or specifications.

### IV. Clarity & Simplicity
Code and structure must be easily understandable to beginner–intermediate developers. Simplicity is valued over unnecessary complexity.

### V. Reproducibility
Any reviewer must be able to clone the repository, follow the README instructions precisely, and run the application successfully in the specified environment.

### VI. Clean Code Discipline
Maintain a readable, logical structure, use meaningful naming conventions, create modular functions, and enforce a clear separation of concerns across layers.

---

## Key Standards and Constraints

- **Traceability**: All features must be traceable to explicit specifications.
- **Documentation**: Each development phase (spec → plan → tasks → implementation) must be fully documented in the repository.
- **Code Style**: Python code must adhere to clean-code practices and PEP-8 guidelines; frontend code must follow idiomatic Next.js and TypeScript conventions.
- **Spec Authority**: Specifications override implementation assumptions.
- **No Feature Drift**: Undocumented features are not permitted.

---

## Project Phases

### Phase I: In-Memory Python Console Application
A single-user command-line todo application with in-memory storage only.

### Phase II: Full-Stack Web Application
A multi-user, authenticated web-based todo application with persistent storage and RESTful APIs.

---

## Phase I Definition

### Objective
Build a command-line todo application that stores tasks in memory using spec-driven, agentic workflows only.

### Tech Stack
- **Language**: Python 3.13+
- **Package Manager**: UV
- **Development Tools**: Claude Code / Gemini, Spec-Kit Plus
- **Runtime**: WSL 2 (Ubuntu 22.04)

### Scope

#### In Scope (Mandatory Features)
1. Add task with title and description
2. View all tasks
3. Update task by ID
4. Delete task by ID
5. Mark task complete / incomplete

#### Out of Scope
- File or database persistence
- Graphical or web interface
- Authentication or user accounts
- Advanced task metadata

---

## Phase II Definition

### Objective
Transform the console application into a modern, multi-user web application with authentication and persistent storage.

### Technology Stack
- **Frontend**: Next.js 16+ (App Router), TypeScript, Tailwind CSS
- **Backend**: Python FastAPI
- **ORM**: SQLModel
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: Better Auth (JWT-based)
- **Spec-Driven Tools**: Claude Code / Gemini, Spec-Kit Plus

---

## API Standards (Phase II)

- RESTful endpoints under `/api/*`
- All endpoints require a valid JWT token
- User identity must be verified on every request
- Each user may only access their own tasks
- Proper HTTP status codes must be returned

---

## Repository Structure

- **/specs**: Organized specifications (features, api, database, ui)
- **/frontend**: Next.js application
- **/backend**: FastAPI application
- **/specs_history**: Archived specification iterations
- **README.md**: Setup and usage instructions
- **CLAUDE.md**: Agentic workflow instructions
- **Constitution**: This file must remain updated

---

## Success Criteria

The project is considered successful if:

- All Phase I and Phase II features work as specified
- Authentication and user isolation are correctly enforced
- No manual code edits exist outside agentic workflows
- All development phases are clearly traceable
- The application runs successfully in documented environments
- Codebases remain clean, readable, and maintainable

---

## Governance

- **Supremacy**: This Constitution supersedes all other practices and ad-hoc decisions.
- **Compliance**: All development activities must comply with this Constitution.
- **Amendments**: Any amendment requires documentation and a clear migration path.

---

**Version**: 2.0.0  
**Ratified**: TODO  
**Last Amended**: 2025-12-25
