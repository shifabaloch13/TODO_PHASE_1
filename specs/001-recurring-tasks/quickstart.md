# Quickstart: Recurring Tasks Feature

## Overview
The recurring tasks feature allows users to create tasks that automatically reappear based on specified intervals (daily, weekly, monthly), reducing manual task re-entry for routine activities.

## CLI Commands

### Adding Recurring Tasks
```bash
# Add a daily recurring task
python main.py add "Daily Exercise" --recur daily

# Add a weekly recurring task
python main.py add "Weekly Team Meeting" --recur weekly

# Add a monthly recurring task
python main.py add "Monthly Report" --recur monthly

# Add a recurring task with additional properties
python main.py add "Daily Meditation" --priority high --tags mindfulness --recur daily
```

### Managing Recurring Tasks
```bash
# List all tasks (recurring tasks will be marked)
python main.py list

# List only recurring tasks
python main.py list --recur

# Disable recurrence for a specific task
python main.py update 1 --disable-recur
```

## Implementation Notes

### Runtime Behavior
- When the application starts, it checks for any pending recurring tasks
- If recurrence intervals have passed, new task instances are created automatically
- Recurring tasks are visually marked in the task list (e.g., with [R] prefix)

### Data Structure
- Recurring tasks extend the base Task model with recurrence properties
- Each recurring task stores its recurrence rule and next occurrence date
- Completed recurring tasks generate new instances based on their recurrence rules

### Constraints
- Recurrence is evaluated only when the application runs
- No background processes or external schedulers are used
- Recurrence state is maintained in-memory only