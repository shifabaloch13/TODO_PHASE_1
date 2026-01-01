---
description: "Task list for Intermediate Level Todo CLI application features"
---

# Tasks: Intermediate Level Todo CLI Application

**Input**: Design documents from `/specs_history/`
**Prerequisites**: intermediate_plan.md (required), priority_feature_spec.md (required for user stories), research.md, data-model.md, contracts/

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

**Purpose**: Project initialization and basic structure for intermediate features

- [x] T001 Create extended project structure if needed
- [x] T002 Update existing files to prepare for extensions
- [x] T003 [P] Verify existing functionality works before extensions

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Extend Task class with priority, tags, and due_date fields in src/models/task.py
- [x] T005 Extend TodoManager class with search, filter, sort methods in src/services/todo_manager.py
- [x] T006 Update CLI argument parser in main.py to support new features
- [x] T007 [P] Ensure backward compatibility with existing functionality

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Task Priorities (Priority: P1) 🎯 MVP

**Goal**: Enable users to assign priority levels (high, medium, low) to tasks and manage them through CLI commands

**Independent Test**: User can run `python main.py add "Task" --priority high`, then `python main.py list --priority high` to see only high priority tasks, and `python main.py update-priority 1 medium` to change priority

### Implementation for User Story 1

- [x] T008 [P] [US1] Implement priority validation in src/models/task.py
- [x] T009 [US1] Add priority parameter to add_task method in src/services/todo_manager.py
- [x] T010 [US1] Implement update_priority method in src/services/todo_manager.py
- [x] T011 [US1] Add 'update-priority' command to CLI parser in main.py
- [x] T012 [US1] Implement priority filtering in list functionality in main.py
- [x] T013 [US1] Implement priority sorting in list functionality in main.py
- [x] T014 [US1] Handle edge cases for priority commands (invalid priority, non-existent tasks) in main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Tags/Categories (Priority: P2)

**Goal**: Enable users to add tags to tasks for categorization and organize tasks by tags

**Independent Test**: User can run `python main.py add "Task" --tags work,urgent` to add a task with tags, then `python main.py list --tag work` to see only tasks with 'work' tag

### Implementation for User Story 2

- [x] T015 [P] [US2] Implement tags functionality in src/models/task.py
- [x] T016 [US2] Add tags parameter to add_task method in src/services/todo_manager.py
- [x] T017 [US2] Implement update_tags method in src/services/todo_manager.py
- [x] T018 [US2] Add 'add-tag' and 'remove-tag' commands to CLI parser in main.py
- [x] T019 [US2] Implement tag filtering in list functionality in main.py
- [x] T020 [US2] Handle edge cases for tag commands (invalid tags, non-existent tasks) in main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Search Tasks (Priority: P3)

**Goal**: Enable users to search tasks by keyword in title and description

**Independent Test**: User can run `python main.py search "groceries"` to find all tasks containing "groceries" in title or description

### Implementation for User Story 3

- [x] T021 [P] [US3] Implement search functionality in src/services/todo_manager.py
- [x] T022 [US3] Add 'search' command to CLI parser in main.py
- [x] T023 [US3] Implement case-insensitive search algorithm in src/services/todo_manager.py
- [x] T024 [US3] Handle edge cases for search (no matches, empty search) in main.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Filter Tasks (Priority: P4)

**Goal**: Enable users to filter tasks by multiple criteria (status, priority, tags)

**Independent Test**: User can run `python main.py list --status incomplete --priority high` to see only incomplete high-priority tasks

### Implementation for User Story 4

- [x] T025 [P] [US4] Implement advanced filtering methods in src/services/todo_manager.py
- [x] T026 [US4] Add filter parameters to list command in main.py
- [x] T027 [US4] Implement combined filter logic in src/services/todo_manager.py
- [x] T028 [US4] Handle edge cases for filtering (no matches, conflicting filters) in main.py

**Checkpoint**: At this point, all user stories should be independently functional

---

## Phase 7: User Story 5 - Sort Tasks (Priority: P5)

**Goal**: Enable users to sort tasks by various criteria (priority, due date, title, status)

**Independent Test**: User can run `python main.py list --sort priority` to see tasks sorted by priority (high first) or `python main.py list --sort due_date` to sort by due date

### Implementation for User Story 5

- [x] T029 [P] [US5] Implement sorting functionality in src/services/todo_manager.py
- [x] T030 [US5] Add sort parameters to list command in main.py
- [x] T031 [US5] Implement multi-level sorting algorithm in src/services/todo_manager.py
- [x] T032 [US5] Handle edge cases for sorting (invalid sort criteria, empty lists) in main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T033 [P] Update README.md with new organization features
- [x] T034 Code cleanup and refactoring across all components
- [x] T035 [P] Add comprehensive error messages for all new commands
- [x] T036 Add input validation across all new commands
- [x] T037 Test all features together for integration issues
- [x] T038 Validate all acceptance criteria from specifications
- [x] T039 Perform regression testing to ensure Basic Level features still work
- [x] T040 [P] Update documentation to reflect all new features

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
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May use functionality from US1/US2
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May use functionality from US1

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
Task: "Implement priority validation in src/models/task.py"
Task: "Add priority parameter to add_task method in src/services/todo_manager.py"
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