## Feature Name
Task Priorities

## Problem Statement
Users need a way to organize and prioritize their tasks to focus on the most important ones first. Without priority levels, all tasks appear equal in importance, making it difficult for users to determine which tasks should be completed first. This feature addresses the organization issue by allowing users to assign priority levels to tasks.

## Feature Description
This feature allows users to assign priority levels (high, medium, low) to tasks. Users can set or update the priority of existing tasks through CLI commands. The priority will be displayed when viewing tasks, helping users identify important tasks quickly. The feature integrates with the existing task model and CLI interface.

## User Interaction (CLI)
Users will interact with this feature through the following commands:

1. Add a task with priority:
```
python main.py add "Task Title" "Task Description" --priority high
```

2. Update task priority:
```
python main.py update-priority 1 high
```

3. List tasks with priority filtering:
```
python main.py list --priority high
```

4. List tasks sorted by priority:
```
python main.py list --sort priority
```

The priority flag can be abbreviated as -p:
```
python main.py add "Task Title" --priority high
python main.py update-priority 1 -p medium
```

## Inputs
- **Task ID**: Integer, required for update-priority command
  - Validation: Must be a positive integer, must correspond to an existing task
- **Priority Level**: String, required for priority-related commands
  - Allowed values: "high", "medium", "low" (case-insensitive)
  - Validation: Must be one of the allowed values
  - Abbreviation: h for high, m for medium, l for low

## Outputs
- **Success Messages**: "Priority updated successfully for task [ID] to [priority level]"
- **Task Display**: When listing tasks, priority level is shown (e.g., "[X] ID: 1 | Priority: HIGH | Title: Task Title")
- **Filtered Lists**: When filtering by priority, only tasks with matching priority are shown
- **Error Messages**: Appropriate error messages for invalid inputs or non-existent tasks

## Expected Behavior
1. When adding a task with priority, the system creates a new task with the specified priority level (default to "medium" if not specified)
2. When updating a task's priority, the system validates the task ID and priority level, then updates the task's priority
3. When listing tasks with priority filter, only tasks matching the specified priority are displayed
4. When sorting by priority, tasks are displayed in order: high, medium, then low priority
5. The priority is stored as part of the task data structure in memory
6. All existing functionality remains unchanged when priority is not used

## Edge Cases & Error Handling
- **Invalid Priority**: If user provides an invalid priority level, display error: "Error: Invalid priority level. Use 'high', 'medium', or 'low'."
- **Non-existent Task ID**: If user tries to update priority for a non-existent task, display error: "Error: Task with ID [ID] not found."
- **Empty Task List**: When filtering by priority and no tasks exist, display "No tasks found."
- **No Matching Tasks**: When filtering by priority and no tasks match, display "No tasks with [priority] priority found."
- **Case Insensitivity**: Accept priority values in any case (HIGH, High, high, etc.)
- **Abbreviation Support**: Support priority abbreviations (h, m, l)
- **Default Priority**: If no priority is specified when adding a task, default to "medium"

## Dependencies & Data Model Impact
- **Task Model**: Add a "priority" attribute to the Task class with default value "medium"
- **TodoManager**: Add methods for updating task priority and filtering/sorting by priority
- **CLI Interface**: Add priority-related arguments to existing commands and add new update-priority command
- **Compatibility**: All existing features (add, list, complete, etc.) continue to work without requiring priority

## Acceptance Criteria
- [ ] Users can add tasks with priority levels (high, medium, low)
- [ ] Users can update the priority of existing tasks
- [ ] Users can list tasks filtered by priority level
- [ ] Users can list tasks sorted by priority (high first)
- [ ] Priority information is displayed when viewing tasks
- [ ] Default priority is "medium" when not specified
- [ ] Priority values are validated and case-insensitive
- [ ] Priority abbreviations (h, m, l) are supported
- [ ] Error messages are displayed for invalid inputs
- [ ] Existing functionality remains unaffected when priority is not used
- [ ] All existing acceptance criteria for basic features continue to pass
- [ ] Priority feature integrates cleanly with existing CLI commands