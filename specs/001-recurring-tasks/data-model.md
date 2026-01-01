# Data Model: Recurring Tasks

## Extended Task Entity

### New Properties
- **recurrence_rule** (string): The recurrence pattern - "daily", "weekly", "monthly"
- **next_occurrence** (datetime): The date/time when this task should reappear
- **recurrence_active** (boolean): Whether the recurrence should continue after completion
- **original_task_id** (int, optional): Reference to parent task for recurring instances

### Updated Properties
- **id** (int): Unique identifier (unchanged)
- **title** (string): Task title (unchanged)
- **description** (string): Task description (unchanged)
- **priority** (string): Task priority (unchanged: "high", "medium", "low")
- **tags** (list of strings): Task tags (unchanged)
- **due_date** (datetime, optional): Task due date (unchanged)
- **completed** (boolean): Completion status (unchanged)
- **created_at** (datetime): Creation timestamp (unchanged)

## RecurrenceRule Entity (Conceptual)

### Properties
- **interval_type** (string): "daily", "weekly", "monthly"
- **interval_count** (int): Number of intervals (e.g., every 2 weeks would be interval_type="weekly", interval_count=2)
- **end_condition** (string, optional): When recurrence should stop ("never", "after_n_occurrences", "until_date")
- **end_value** (mixed, optional): Value for end condition (number of occurrences or end date)

## Relationships
- Each recurring task has one recurrence rule
- Recurring task instances reference their original task via original_task_id

## Validation Rules
- recurrence_rule must be one of: "daily", "weekly", "monthly"
- next_occurrence must be a valid future date when recurrence_active is true
- original_task_id must reference an existing task when present
- recurrence_active can only be set to false (once disabled, recurrence cannot be re-enabled for that specific task)

## State Transitions
- Regular task → Recurring task: When user specifies recurrence on task creation/update
- Recurring task (completed) → New recurring task: When recurrence is active and next occurrence is due
- Recurring task → Regular task: When recurrence is disabled