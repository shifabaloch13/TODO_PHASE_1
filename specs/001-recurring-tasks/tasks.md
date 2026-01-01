---
description: "Task list for recurring tasks feature implementation"
---

# Tasks: Recurring Tasks with Automatic Rescheduling

**Input**: Design documents from `/specs/001-recurring-tasks/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Update Task model with recurrence properties in src/models/task.py
- [x] T002 Extend TodoManager with recurring task logic in src/services/todo_manager.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T003 [P] Add recurrence properties to Task class: recurrence_rule, next_occurrence, recurrence_active, original_task_id in src/models/task.py
- [x] T004 [P] Implement recurrence validation methods in src/models/task.py
- [x] T005 Add recurring task creation logic to TodoManager in src/services/todo_manager.py
- [x] T006 Add recurring task evaluation logic at startup in src/services/todo_manager.py
- [x] T007 Update CLI to support recurrence options in src/cli/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Create Daily Recurring Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to create tasks that automatically reappear every day, with the system checking for pending recurring tasks at startup and creating new instances when their recurrence period elapses.

**Independent Test**: Can be fully tested by creating a daily recurring task and verifying it appears again the next day when the application is run, delivering the value of reduced manual task entry.

### Implementation for User Story 1

- [x] T008 [P] [US1] Add daily recurrence validation in src/models/task.py
- [x] T009 [US1] Implement daily recurrence calculation logic in src/services/todo_manager.py
- [x] T010 [US1] Add daily recurrence CLI command option in src/cli/main.py
- [x] T011 [US1] Test daily recurrence creation with add command in src/cli/main.py
- [x] T012 [US1] Verify daily recurring tasks appear after application restart

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Create Weekly Recurring Tasks (Priority: P2)

**Goal**: Enable users to create tasks that automatically reappear every week on the same day, extending the recurrence functionality to weekly intervals.

**Independent Test**: Can be fully tested by creating a weekly recurring task and verifying it appears again the following week when the application is run, delivering the value of consistent weekly task management.

### Implementation for User Story 2

- [x] T013 [P] [US2] Add weekly recurrence validation in src/models/task.py
- [x] T014 [US2] Implement weekly recurrence calculation logic in src/services/todo_manager.py
- [x] T015 [US2] Add weekly recurrence CLI command option in src/cli/main.py
- [x] T016 [US2] Test weekly recurrence creation with add command in src/cli/main.py
- [x] T017 [US2] Verify weekly recurring tasks appear after 7 days

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Create Monthly Recurring Tasks (Priority: P3)

**Goal**: Enable users to create tasks that automatically reappear every month, handling month-end edge cases appropriately.

**Independent Test**: Can be fully tested by creating a monthly recurring task and verifying it appears again the following month when the application is run, delivering the value of consistent monthly task scheduling.

### Implementation for User Story 3

- [x] T018 [P] [US3] Add monthly recurrence validation in src/models/task.py
- [x] T019 [US3] Implement monthly recurrence calculation logic in src/services/todo_manager.py
- [x] T020 [US3] Add monthly recurrence CLI command option in src/cli/main.py
- [x] T021 [US3] Handle month-end date edge cases in src/services/todo_manager.py
- [x] T022 [US3] Test monthly recurrence creation with add command in src/cli/main.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - View and Manage Recurring Tasks (Priority: P2)

**Goal**: Allow users to identify and manage recurring tasks, with clear visual indicators to distinguish recurring tasks from regular tasks.

**Independent Test**: Can be fully tested by creating recurring tasks and using CLI commands to view and distinguish recurring tasks from regular tasks, delivering the value of task management transparency.

### Implementation for User Story 4

- [x] T023 [P] [US4] Add recurring task identification methods in src/models/task.py
- [x] T024 [US4] Implement recurring task filtering in src/services/todo_manager.py
- [x] T025 [US4] Add recurring task display indicators in src/cli/main.py
- [x] T026 [US4] Add CLI command to list only recurring tasks in src/cli/main.py
- [x] T027 [US4] Implement recurrence disabling functionality in src/services/todo_manager.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T028 [P] Update documentation and help text in src/cli/main.py
- [x] T029 Handle multiple missed recurrence periods in src/services/todo_manager.py
- [x] T030 Add comprehensive error handling for recurrence operations
- [x] T031 Test edge cases like February 30th scenarios in src/services/todo_manager.py
- [x] T032 Run quickstart validation with all recurrence features

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with other stories but should be independently testable

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all parallel tasks for User Story 1:
Task: "Add daily recurrence validation in src/models/task.py"
Task: "Implement daily recurrence calculation logic in src/services/todo_manager.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence