---
description: "Task list for Todo CLI application implementation"
---

# Tasks: Todo CLI Application

**Input**: Design documents from `/specs_history/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure with src/models/ and src/services/ directories
- [x] T002 Initialize Python project with requirements.txt
- [x] T003 [P] Create main.py file as CLI entry point

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Create Task class definition in src/models/task.py
- [x] T005 Create TodoManager class with in-memory storage in src/services/todo_manager.py
- [x] T006 Setup argument parsing for CLI in main.py
- [x] T007 Implement basic error handling infrastructure

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks to the in-memory task list with unique ID, title, and optional description

**Independent Test**: User can run `python main.py add "Test Title" "Test Description"` and see "Task added successfully! ID: 1, Title: Test Title" with the task stored in memory

### Implementation for User Story 1

- [x] T008 [P] [US1] Implement Task creation validation in src/models/task.py
- [x] T009 [US1] Implement add_task method in src/services/todo_manager.py
- [x] T010 [US1] Add 'add' command to CLI parser in main.py
- [x] T011 [US1] Implement input validation for add command in main.py
- [x] T012 [US1] Handle edge cases for add command (empty title, title too long, etc.) in main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P2)

**Goal**: Enable users to view all tasks in the in-memory task list with their status indicators

**Independent Test**: User can run `python main.py list` and see all tasks with their ID, title, description, and completion status

### Implementation for User Story 2

- [x] T013 [P] [US2] Implement get_all_tasks method in src/services/todo_manager.py
- [x] T014 [US2] Add 'list' command to CLI parser in main.py
- [x] T015 [US2] Format task display with status indicators in main.py
- [x] T016 [US2] Handle empty task list case in main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Task as Complete/Incomplete (Priority: P3)

**Goal**: Enable users to toggle the completion status of tasks by ID

**Independent Test**: User can run `python main.py complete 1` to mark task with ID 1 as complete and `python main.py incomplete 1` to mark it as incomplete

### Implementation for User Story 3

- [x] T017 [P] [US3] Implement mark_complete and mark_incomplete methods in src/services/todo_manager.py
- [x] T018 [US3] Add 'complete' command to CLI parser in main.py
- [x] T019 [US3] Add 'incomplete' command to CLI parser in main.py
- [x] T020 [US3] Handle invalid task ID for complete/incomplete commands in main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Update Task (Priority: P4)

**Goal**: Enable users to modify existing task details (title, description) by ID

**Independent Test**: User can run `python main.py update 1 "New Title" "New Description"` to update task with ID 1

### Implementation for User Story 4

- [x] T021 [P] [US4] Implement update_task method in src/services/todo_manager.py
- [x] T022 [US4] Add 'update' command to CLI parser in main.py
- [x] T023 [US4] Implement input validation for update command in main.py
- [x] T024 [US4] Handle invalid task ID for update command in main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: User Story 5 - Delete Task (Priority: P5)

**Goal**: Enable users to remove tasks from the in-memory task list by ID

**Independent Test**: User can run `python main.py delete 1` to remove task with ID 1 from the list

### Implementation for User Story 5

- [x] T025 [P] [US5] Implement delete_task method in src/services/todo_manager.py
- [x] T026 [US5] Add 'delete' command to CLI parser in main.py
- [x] T027 [US5] Handle invalid task ID for delete command in main.py
- [x] T028 [US5] Handle edge case for deleting from empty list in main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T029 [P] Update README.md with setup and usage instructions
- [x] T030 Code cleanup and refactoring across all components
- [x] T031 [P] Add comprehensive error messages for all commands
- [x] T032 Add input validation across all commands
- [x] T033 Test all features together for integration issues
- [x] T034 Validate all acceptance criteria from specifications

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4 → P5)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all implementation tasks for User Story 1 together:
Task: "Implement Task creation validation in src/models/task.py"
Task: "Implement add_task method in src/services/todo_manager.py"
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
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence