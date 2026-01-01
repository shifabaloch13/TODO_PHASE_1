# Colorful Todo CLI Application

A feature-rich, colorful, and user-friendly command-line interface for managing tasks efficiently with advanced features including recurring tasks, priority management, and tagging.

## Features

### ✨ Core Features
- **Colorful Interface**: All commands provide colorful, easy-to-read output
- **In-Memory Storage**: Fast, lightweight task management
- **Priority Management**: High, medium, and low priority levels with color coding
- **Tagging System**: Add and manage tags for better organization
- **Due Dates**: Optional due date support for tasks

### 🔄 Advanced Features
- **Recurring Tasks**: Daily, weekly, and monthly recurring tasks
- **Recurrence Management**: Enable/disable recurrence for tasks
- **Smart Filtering**: Filter by priority, status, tags, and more
- **Advanced Search**: Search through task titles and descriptions
- **Sorting Options**: Sort tasks by priority, due date, title, or status

### 🎨 User Experience
- **Color-Coded Output**: Different colors for different operations
  - Green (`+`) for successful operations
  - Red (`-`) for errors and deletions
  - Yellow (`->`) for updates and transitions
  - Cyan for headers and information
  - Magenta for recurring tasks
- **Visual Status Indicators**: Clear completion status with colored symbols
- **Intuitive Commands**: Easy-to-remember command structure

## Prerequisites

- Python 3.13 or higher

## Setup

1. Clone or download the repository
2. Ensure Python 3.13+ is installed on your system
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Add a Task

```bash
python main.py add "Task Title" "Task Description (optional)"
```

### Add a Task with Priority, Tags, and Due Date

```bash
python main.py add "Task Title" "Description" --priority high --tags work,urgent --due-date 2025-12-31
```

### List All Tasks

```bash
python main.py list
```

### List Tasks with Filters and Sorting

```bash
python main.py list --priority high
python main.py list --tag work
python main.py list --status complete
python main.py list --sort priority
python main.py list --sort due_date
```

### Search Tasks

```bash
python main.py search "keyword"
```

### Mark a Task as Complete

```bash
python main.py complete [task_id]
```

### Mark a Task as Incomplete

```bash
python main.py incomplete [task_id]
```

### Update a Task

```bash
python main.py update [task_id] "New Title (optional)" "New Description (optional)"
```

### Update Task Priority

```bash
python main.py update-priority [task_id] [priority_level]
```

### Add/Remove Tags

```bash
python main.py add-tag [task_id] [tag]
python main.py remove-tag [task_id] [tag]
```

### Delete a Task

```bash
python main.py delete [task_id]
```

### Update Task Priority

```bash
python main.py update-priority [task_id] [priority_level]
```

### Add/Remove Tags

```bash
python main.py add-tag [task_id] [tag]
python main.py remove-tag [task_id] [tag]
```

### Recurring Tasks

```bash
# Add a recurring task
python main.py add "Daily Task" "Description" --recur daily
# Options: daily, weekly, monthly

# List all recurring tasks
python main.py list-recurring

# List recurring tasks with status filter
python main.py list-recurring --active true
python main.py list-recurring --active false

# Disable recurrence for a task
python main.py disable-recurrence [task_id]
```

### Interactive Mode

```bash
# Run the application in interactive mode (menu-driven interface)
python main.py interactive
```

The interactive mode provides a step-by-step menu-driven interface that allows you to manage all your tasks efficiently:
- Add, update, complete, and delete tasks
- Set priorities, tags, and recurrence
- Search and filter tasks
- All with colorful, user-friendly prompts

## Example

```bash
# Add a new task with priority and tags
python main.py add "Buy groceries" "Milk, bread, eggs" --priority high --tags shopping,urgent

# Add a recurring task
python main.py add "Daily Exercise" "30 minutes workout" --recur daily --priority medium

# List all tasks
python main.py list

# List tasks with filters
python main.py list --priority high
python main.py list --tag shopping
python main.py list --status incomplete
python main.py list --sort priority

# Search tasks containing "groceries"
python main.py search groceries

# Mark task with ID 1 as complete
python main.py complete 1

# Mark task as incomplete
python main.py incomplete 1

# Update task priority
python main.py update-priority 1 medium

# Add a tag to a task
python main.py add-tag 1 food

# Remove a tag from a task
python main.py remove-tag 1 shopping

# Update task title and description
python main.py update 1 "New Title" "New Description"

# List all recurring tasks
python main.py list-recurring

# List only active recurring tasks
python main.py list-recurring --active true

# Disable recurrence for a task
python main.py disable-recurrence 1

# Run in interactive mode (menu-driven interface)
python main.py interactive

# Delete task with ID 1
python main.py delete 1
```

## Data Model

- **Task**: Each task has:
  - `id`: Unique integer identifier
  - `title`: Required string (max 200 characters)
  - `description`: Optional string (max 500 characters)
  - `completed`: Boolean status (default: False)
  - `priority`: String (high, medium, low - default: medium)
  - `tags`: List of tag strings for categorization
  - `due_date`: Optional string in YYYY-MM-DD format
  - `recurrence_rule`: String (daily, weekly, monthly - optional)
  - `next_occurrence`: DateTime for when recurring task should reappear
  - `recurrence_active`: Boolean for whether recurrence should continue (default: True)
  - `original_task_id`: Reference to parent task for recurring instances (optional)

## Architecture

- `main.py`: CLI entry point and command routing
- `src/models/task.py`: Extended Task data model with priority, tags, due date, and recurrence properties
- `src/services/todo_manager.py`: Enhanced in-memory task storage and operations with search, filter, sort, and recurrence processing
- `requirements.txt`: Dependencies including colorama for colorful output

## Testing

Run the comprehensive test suite to verify all features:

```bash
# Test all colorful features
python test_colorful_features.py

# Test all functionality
python test_all_features.py

# Test complete functionality
python test_complete_functionality.py
```

## Key Benefits

1. **Efficient Task Management**: All common operations available through simple commands
2. **Visual Feedback**: Color-coded output makes status and priority clear at a glance
3. **Flexible Organization**: Tags, priorities, and filtering options for complex task management
4. **Recurring Tasks**: Automated task creation for routine activities
5. **Cross-Platform**: Works on Windows, macOS, and Linux with consistent color output
6. **No Setup Required**: In-memory storage means no database or configuration needed