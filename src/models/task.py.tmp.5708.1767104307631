"""
Task model for the Todo CLI application
Represents a single todo task with ID, title, description, completion status, priority, tags, due date, and recurrence properties
"""

from datetime import datetime, timedelta
import re


class Task:
    def __init__(self, task_id, title, description="", completed=False, priority="medium", tags=None, due_date="", recurrence_rule=None, next_occurrence=None, recurrence_active=True, original_task_id=None):
        """
        Initialize a new Task instance

        Args:
            task_id (int): Unique identifier for the task
            title (str): Task title (required)
            description (str): Task description (optional)
            completed (bool): Completion status (default: False)
            priority (str): Task priority (default: "medium")
            tags (list): List of tags for the task (default: [])
            due_date (str): Due date for the task (optional)
            recurrence_rule (str): The recurrence pattern - "daily", "weekly", "monthly" (optional)
            next_occurrence (datetime): The date/time when this task should reappear (optional)
            recurrence_active (bool): Whether the recurrence should continue after completion (default: True)
            original_task_id (int): Reference to parent task for recurring instances (optional)
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty or contain only whitespace")

        if len(title) > 200:
            raise ValueError("Task title cannot exceed 200 characters")

        if len(description) > 500:
            raise ValueError("Task description cannot exceed 500 characters")

        # Validate priority
        if priority is None:
            priority = "medium"
        elif priority.lower() not in ['high', 'medium', 'low', 'h', 'm', 'l']:
            raise ValueError("Priority must be one of: high, medium, low, h, m, l")
        else:
            # Normalize priority to full form
            priority_map = {'h': 'high', 'm': 'medium', 'l': 'low'}
            priority = priority_map.get(priority.lower(), priority.lower())

        # Validate due_date format (YYYY-MM-DD)
        if due_date:
            date_pattern = r'^\d{4}-\d{2}-\d{2}$'
            if not re.match(date_pattern, due_date):
                raise ValueError("Due date must be in YYYY-MM-DD format")

        # Validate recurrence_rule
        if recurrence_rule is not None:
            if recurrence_rule not in ['daily', 'weekly', 'monthly']:
                raise ValueError("Recurrence rule must be one of: daily, weekly, monthly")

        self.id = task_id
        self.title = title.strip()
        self.description = description.strip() if description else ""
        self.completed = completed
        self.priority = priority
        self.tags = tags if tags is not None else []
        self.due_date = due_date
        self.recurrence_rule = recurrence_rule
        self.next_occurrence = next_occurrence
        self.recurrence_active = recurrence_active
        self.original_task_id = original_task_id
        self.created_at = datetime.now()

    def __str__(self):
        """String representation of the task"""
        status = "X" if self.completed else "O"
        tags_str = ", ".join(self.tags) if self.tags else "None"
        due_date_str = f" | Due: {self.due_date}" if self.due_date else ""

        # Add recurrence indicator if the task has recurrence properties
        recurrence_indicator = ""
        if self.recurrence_rule:
            recurrence_indicator = f" | Recurrence: {self.recurrence_rule}"
            if self.recurrence_active:
                recurrence_indicator += " (active)"
            else:
                recurrence_indicator += " (inactive)"

        return f"[{status}] ID: {self.id} | Priority: {self.priority.upper()} | Title: {self.title} | Description: {self.description} | Tags: {tags_str}{due_date_str}{recurrence_indicator}"

    def to_dict(self):
        """Convert task to dictionary representation"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "priority": self.priority,
            "tags": self.tags,
            "due_date": self.due_date,
            "recurrence_rule": self.recurrence_rule,
            "next_occurrence": self.next_occurrence.isoformat() if self.next_occurrence else None,
            "recurrence_active": self.recurrence_active,
            "original_task_id": self.original_task_id
        }

    def mark_complete(self):
        """Mark the task as complete"""
        self.completed = True

    def mark_incomplete(self):
        """Mark the task as incomplete"""
        self.completed = False

    def update_priority(self, priority):
        """Update task priority with validation"""
        if priority is None:
            raise ValueError("Priority cannot be None")
        if priority.lower() not in ['high', 'medium', 'low', 'h', 'm', 'l']:
            raise ValueError("Priority must be one of: high, medium, low, h, m, l")

        # Normalize priority to full form
        priority_map = {'h': 'high', 'm': 'medium', 'l': 'low'}
        self.priority = priority_map.get(priority.lower(), priority.lower())

    def add_tag(self, tag):
        """Add a tag to the task if it doesn't already exist"""
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag):
        """Remove a tag from the task if it exists"""
        if tag in self.tags:
            self.tags.remove(tag)

    def update(self, title=None, description=None, priority=None, due_date=None, recurrence_rule=None, recurrence_active=None):
        """Update task fields with validation"""
        if title is not None:
            if not title or not title.strip():
                raise ValueError("Task title cannot be empty or contain only whitespace")

            if len(title) > 200:
                raise ValueError("Task title cannot exceed 200 characters")

            self.title = title.strip()

        if description is not None:
            if len(description) > 500:
                raise ValueError("Task description cannot exceed 500 characters")

            self.description = description.strip() if description else ""

        if priority is not None:
            self.update_priority(priority)

        if due_date is not None:
            # Validate due_date format (YYYY-MM-DD)
            if due_date:  # Only validate if not empty
                date_pattern = r'^\d{4}-\d{2}-\d{2}$'
                if not re.match(date_pattern, due_date):
                    raise ValueError("Due date must be in YYYY-MM-DD format")
            self.due_date = due_date

        if recurrence_rule is not None:
            if recurrence_rule is not None and recurrence_rule not in ['daily', 'weekly', 'monthly']:
                raise ValueError("Recurrence rule must be one of: daily, weekly, monthly")
            self.recurrence_rule = recurrence_rule

        if recurrence_active is not None:
            self.recurrence_active = bool(recurrence_active)

    def is_recurring_task(self):
        """Check if this task is a recurring task"""
        return self.recurrence_rule is not None

    def is_recurring_and_active(self):
        """Check if this task is recurring and currently active"""
        return self.is_recurring_task() and self.recurrence_active

    def should_create_next_occurrence(self):
        """Check if a new occurrence should be created based on completion and recurrence status"""
        return self.completed and self.is_recurring_and_active()

    def calculate_next_occurrence(self, current_date=None):
        """
        Calculate the next occurrence date based on the recurrence rule

        Args:
            current_date (datetime): The date from which to calculate next occurrence (default: now)

        Returns:
            datetime: The next occurrence date
        """
        if current_date is None:
            current_date = datetime.now()

        if self.recurrence_rule == 'daily':
            return current_date + timedelta(days=1)
        elif self.recurrence_rule == 'weekly':
            return current_date + timedelta(weeks=1)
        elif self.recurrence_rule == 'monthly':
            # Handle monthly recurrence with special care for month-end dates
            current_year = current_date.year
            current_month = current_date.month
            current_day = current_date.day

            # Calculate next month
            if current_month == 12:
                next_year = current_year + 1
                next_month = 1
            else:
                next_year = current_year
                next_month = current_month + 1

            # Handle month-end dates (e.g., Jan 31 -> Feb 28/29)
            import calendar
            max_day_next_month = calendar.monthrange(next_year, next_month)[1]
            next_day = min(current_day, max_day_next_month)

            return current_date.replace(year=next_year, month=next_month, day=next_day)

        return None