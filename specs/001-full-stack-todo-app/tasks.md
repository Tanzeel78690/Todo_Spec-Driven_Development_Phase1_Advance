# Tasks: Full-Stack Todo App

**Input**: Design documents from `/specs/001-full-stack-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The feature specification does not explicitly request TDD or test tasks for implementation. Testing will be covered implicitly through validation checks and independent test criteria.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description with file path`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create monorepo base directories: `backend/`, `frontend/`
- [x] T002 Initialize Python backend project with `uv` and `pyproject.toml` in `backend/`
- [x] T003 [P] Add FastAPI, SQLModel, Uvicorn, and `python-jose` (for JWT) to `backend/pyproject.toml`
- [x] T004 Initialize Node.js frontend project (Next.js with TypeScript and Tailwind CSS) in `frontend/`
- [x] T005 [P] Configure shared `.gitignore` for monorepo in repository root
- [x] T006 Create `.env` template file for backend: `backend/.env.example`
- [x] T007 Create `.env.local` template file for frontend: `frontend/.env.local.example`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T008 Setup database connection logic in `backend/src/database.py`
- [x] T009 Define base `SQLModel` models for `User` and `Todo` entities in `backend/src/models/user.py` and `backend/src/models/todo.py` respectively, establishing relationships
- [x] T010 Implement JWT token utility functions (encoding, decoding) in `backend/src/auth/jwt.py`
- [x] T011 Implement password hashing utility functions in `backend/src/auth/hashing.py`
- [x] T012 Define FastAPI `Auth` router with dependency injection for current user in `backend/src/api/auth.py`
- [x] T013 Create FastAPI main application instance in `backend/src/main.py`
- [x] T014 [P] Configure CORS middleware for FastAPI application in `backend/src/main.py`
- [x] T015 [P] Configure global exception handling for FastAPI application in `backend/src/main.py`
- [x] T016 [P] Configure basic logging for backend application in `backend/src/main.py`
- [x] T017 Create a base `requirements.txt` for backend based on `pyproject.toml` in `backend/requirements.txt`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - User Signup (Priority: P1) 🎯 MVP

**Goal**: Enable new users to register an account with email and password.

**Independent Test**: A new user can successfully register via the `/api/signup` endpoint and their hashed password is stored.

### Implementation for User Story 1

- [x] T018 [P] [US1] Implement `create_user` service function in `backend/src/services/user_service.py` to handle user creation and password hashing.
- [x] T019 [US1] Implement `POST /api/signup` endpoint in `backend/src/api/auth.py` using `user_service.py`.
- [x] T020 [P] [US1] Create signup page/component in `frontend/src/pages/signup.tsx` or `frontend/src/components/SignupForm.tsx`.
- [x] T021 [US1] Implement frontend API call for signup in `frontend/src/services/auth_api.ts`.
- [x] T022 [US1] Integrate signup form with API call and basic client-side validation in `frontend/src/pages/signup.tsx`.

**Checkpoint**: User Signup should be fully functional and testable independently

---

## Phase 4: User Story 2 - User Signin (Priority: P1)

**Goal**: Enable registered users to sign in and receive a JWT.

**Independent Test**: A registered user can successfully sign in via the `/api/signin` endpoint and receive a valid JWT. The frontend stores and uses this JWT.

### Implementation for User Story 2

- [x] T023 [P] [US2] Implement `authenticate_user` service function in `backend/src/services/user_service.py` to verify credentials and generate JWT.
- [x] T024 [US2] Implement `POST /api/signin` endpoint in `backend/src/api/auth.py` using `user_service.py`.
- [x] T025 [P] [US2] Create signin page/component in `frontend/src/pages/signin.tsx` or `frontend/src/components/SigninForm.tsx`.
- [x] T026 [US2] Implement frontend API call for signin and JWT storage in `frontend/src/services/auth_api.ts`.
- [x] T027 [US2] Integrate signin form with API call, JWT storage, and redirection in `frontend/src/pages/signin.tsx`.

**Checkpoint**: User Signin should be fully functional and testable independently

---

## Phase 5: User Story 3 - Todo Management (Priority: P2)

**Goal**: Authenticated users can create, view, update, delete, and mark complete/incomplete their own todo items.

**Independent Test**: An authenticated user can perform all CRUD operations on their own todo items via the API and observe changes in the UI. Cross-user access is denied.

### Implementation for User Story 3

- [x] T028 [P] [US3] Implement `Todo` CRUD service functions (create, get_all, get_by_id, update, delete) in `backend/src/services/todo_service.py`, ensuring `owner_id` is used for all operations.
- [x] T029 [US3] Implement `POST /api/todos` endpoint in `backend/src/api/todos.py` using `todo_service.py`, associating new todos with the authenticated user.
- [x] T030 [US3] Implement `GET /api/todos` endpoint in `backend/src/api/todos.py` using `todo_service.py`, filtering by authenticated user.
- [x] T031 [US3] Implement `GET /api/todos/{id}` endpoint in `backend/src/api/todos.py` using `todo_service.py`, ensuring user ownership.
- [x] T032 [US3] Implement `PUT /api/todos/{id}` endpoint in `backend/src/api/todos.py` using `todo_service.py`, ensuring user ownership.
- [x] T033 [US3] Implement `DELETE /api/todos/{id}` endpoint in `backend/src/api/todos.py` using `todo_service.py`, ensuring user ownership.
- [x] T034 [P] [US3] Implement `PATCH /api/todos/{id}/complete` (or similar) endpoint for toggling completion status in `backend/src/api/todos.py`.
- [x] T035 [P] [US3] Create main todo dashboard page/component in `frontend/src/pages/dashboard.tsx` to display todos.
- [x] T036 [US3] Implement frontend API calls for all todo CRUD operations in `frontend/src/services/todo_api.ts`.
- [x] T037 [US3] Integrate todo list display, create form, update/delete/toggle buttons with API calls and state management in `frontend/src/pages/dashboard.tsx`.

**Checkpoint**: Todo Management should be fully functional and testable independently, with data isolation enforced.

---

## Phase 6: Final Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T038 [P] Implement global authentication middleware in `backend/src/middleware/auth_middleware.py` to protect all relevant API routes.
- [x] T039 [P] Add a global loading indicator and error message display in `frontend/src/components/layout.tsx` or similar.
- [x] T040 Review and refine database schema (indices, constraints) based on usage patterns in `backend/src/models/`.
- [x] T041 Ensure all API endpoints return appropriate HTTP status codes and error messages as per `api.md`.
- [x] T042 Update `README.md` in repository root with setup instructions, project overview, and quickstart guide.
- [x] T043 Update `CLAUDE.md` in repository root with agentic workflow instructions and project details.
- [x] T044 Run all validation checks as defined in `plan.md` (e.g., API requests without JWT return 401, only access own tasks).

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase 6)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1 - Signup)**: Can start after Foundational (Phase 2). No dependencies on other stories.
- **User Story 2 (P1 - Signin)**: Can start after Foundational (Phase 2). Depends on User Story 1 (Signup) for user creation to test signin.
- **User Story 3 (P2 - Todo Management)**: Can start after Foundational (Phase 2). Depends on User Story 1 (Signup) and User Story 2 (Signin) for authentication context.
- **User Story 4 (Data Isolation)**: Integrated into User Story 3 (Todo Management) implementation.

### Within Each User Story

- Models before services
- Services before API endpoints
- Backend before frontend integration
- Story complete before moving to next priority (or integrating parallel stories)

### Parallel Opportunities

- All tasks marked [P] can run in parallel with other [P] tasks within the same phase, or across phases if dependencies are met.
- Once the Foundational phase completes, User Stories can be tackled by different team members in parallel (e.g., one dev on Signup, another on Signin, etc., considering inter-story dependencies).
- Within User Story 3, the implementation of different CRUD endpoints (`POST`, `GET`, `PUT`, `DELETE`) can be parallelized, as can the frontend components that use these.

---

## Parallel Example: User Story 3 - Todo Management

```bash
# Backend services and APIs can be developed in parallel for different CRUD operations:
- [ ] T028 [P] [US3] Implement `Todo` CRUD service functions...
- [ ] T029 [US3] Implement `POST /api/todos` endpoint...
- [ ] T030 [US3] Implement `GET /api/todos` endpoint...
- [ ] T031 [US3] Implement `GET /api/todos/{id}` endpoint...
- [ ] T032 [US3] Implement `PUT /api/todos/{id}` endpoint...
- [ ] T033 [US3] Implement `DELETE /api/todos/{id}` endpoint...
- [ ] T034 [P] [US3] Implement `PATCH /api/todos/{id}/complete`...

# Frontend components and API calls can be developed in parallel:
- [ ] T035 [P] [US3] Create main todo dashboard page/component...
- [ ] T036 [US3] Implement frontend API calls for all todo CRUD operations...
```

---

## Implementation Strategy

### MVP First (User Signup and Signin Only)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3.  Complete Phase 3: User Story 1 (Signup)
4.  Complete Phase 4: User Story 2 (Signin)
5.  **STOP and VALIDATE**: Test User Signup and Signin independently. Ensure users can register and login successfully.
6.  Deploy/demo if ready (e.g., a basic auth service)

### Incremental Delivery (Adding Todo Management)

1.  Complete Setup + Foundational → Foundation ready
2.  Complete User Story 1 (Signup) → Test independently
3.  Complete User Story 2 (Signin) → Test independently → Deploy/Demo (Auth MVP!)
4.  Complete User Story 3 (Todo Management) → Test independently → Deploy/Demo (Full functional MVP!)
5.  Complete Phase 6 (Polish) → Final Release

### Parallel Team Strategy

With multiple developers:

1.  Team completes Setup + Foundational together.
2.  Once Foundational is done:
    *   Developer A: User Story 1 (Signup)
    *   Developer B: User Story 2 (Signin)
    *   Developer C: User Story 3 (Todo Management - Backend)
    *   Developer D: User Story 3 (Todo Management - Frontend)
3.  Stories integrate as dependencies are met.

---

## Notes

-   [P] tasks = different files, no dependencies
-   [Story] label maps task to specific user story for traceability
-   Each user story should be independently completable and testable
-   Commit after each task or logical group
-   Stop at any checkpoint to validate story independently
-   Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence