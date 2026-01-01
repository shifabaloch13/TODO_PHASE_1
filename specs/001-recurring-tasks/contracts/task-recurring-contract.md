# API Contracts: Recurring Tasks

## Task Model Extension

### New Fields for Recurring Tasks
```json
{
  "recurrence_rule": {
    "type": "string",
    "enum": ["daily", "weekly", "monthly"],
    "required": false,
    "description": "The recurrence pattern for the task"
  },
  "next_occurrence": {
    "type": "string",
    "format": "date-time",
    "required": false,
    "description": "The next date/time this task should appear"
  },
  "recurrence_active": {
    "type": "boolean",
    "default": true,
    "required": false,
    "description": "Whether recurrence should continue after completion"
  },
  "original_task_id": {
    "type": "integer",
    "required": false,
    "description": "Reference to the original recurring task"
  }
}
```

## CLI Command Contracts

### Add Command Extension
```
Command: add <title> [description] [--recur daily|weekly|monthly] [other options]

Input:
  - title: string (required)
  - description: string (optional)
  - --recur: enum (optional, values: daily, weekly, monthly)
  - other options: priority, tags, due_date (inherited from base task)

Output:
  - Success: Created task with recurrence properties
  - Error: Appropriate error message
```

### List Command Extension
```
Command: list [--recur]

Input:
  - --recur: flag (optional, show only recurring tasks)

Output:
  - Success: List of tasks with recurrence indicators
  - Error: Appropriate error message
```

### Update Command Extension
```
Command: update <id> [--disable-recur]

Input:
  - id: integer (required)
  - --disable-recur: flag (optional, disable recurrence for task)

Output:
  - Success: Updated task
  - Error: Appropriate error message
```

## Runtime Behavior Contracts

### Application Startup
```
When: Application starts
Then: Check for pending recurring tasks
And: Create new instances for any due recurring tasks
```

### Task Completion
```
When: Recurring task is marked complete
Then: Check if recurrence is active
If: recurrence_active is true
Then: Calculate next occurrence date
And: Create new task instance with same properties
```