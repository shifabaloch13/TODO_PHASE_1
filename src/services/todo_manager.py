"""
TodoManager for the Todo CLI application
Manages in-memory storage and operations for tasks with recurring task functionality
"""

from src.models.task import Task
from datetime import datetime


class TodoManager:
    def __init__(self):
        """Initialize the TodoManager with an empty task list"""
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description="", priority="medium", tags=None, due_date="", recurrence_rule=None, recurrence_active=True):
        """
        Add a new task to the in-memory storage

        Args:
            title (str): Task title
            description (str): Task description (optional)
            priority (str): Task priority (default: "medium")
            tags (list): List of tags for the task (default: [])
            due_date (str): Due date for the task (optional)
            recurrence_rule (str): The recurrence pattern - "daily", "weekly", "monthly" (optional)
            recurrence_active (bool): Whether the recurrence should continue after completion (default: True)

        Returns:
            Task: The newly created task
        """
        # Validate inputs
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")
        if len(title) > 200:
            raise ValueError("Task title cannot exceed 200 characters")
        if len(description) > 500:
            raise ValueError("Task description cannot exceed 500 characters")

        # Validate recurrence_rule if provided
        if recurrence_rule is not None:
            if recurrence_rule not in ['daily', 'weekly', 'monthly']:
                raise ValueError("Recurrence rule must be one of: daily, weekly, monthly")

        # Create new task with unique ID
        new_task = Task(
            self.next_id,
            title,
            description,
            completed=False,
            priority=priority,
            tags=tags,
            due_date=due_date,
            recurrence_rule=recurrence_rule,
            recurrence_active=recurrence_active
        )
        self.tasks.append(new_task)

        # Increment next ID for the subsequent task
        self.next_id += 1

        return new_task

    def get_all_tasks(self):
        """
        Get all tasks in the in-memory storage

        Returns:
            list: List of all Task objects
        """
        return self.tasks

    def update_task_priority(self, task_id, priority):
        """
        Update the priority of a task by its ID

        Args:
            task_id (int): The ID of the task to update
            priority (str): The new priority level

        Returns:
            Task: The updated task, or None if task not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.update_priority(priority)
            return task
        return None

    def add_tag_to_task(self, task_id, tag):
        """
        Add a tag to a task by its ID

        Args:
            task_id (int): The ID of the task to update
            tag (str): The tag to add

        Returns:
            Task: The updated task, or None if task not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.add_tag(tag)
            return task
        return None

    def remove_tag_from_task(self, task_id, tag):
        """
        Remove a tag from a task by its ID

        Args:
            task_id (int): The ID of the task to update
            tag (str): The tag to remove

        Returns:
            Task: The updated task, or None if task not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.remove_tag(tag)
            return task
        return None

    def search_tasks(self, keyword):
        """
        Search tasks by keyword in title and description

        Args:
            keyword (str): The keyword to search for

        Returns:
            list: List of tasks that match the keyword
        """
        keyword_lower = keyword.lower()
        matching_tasks = []
        for task in self.tasks:
            if (keyword_lower in task.title.lower() or
                keyword_lower in task.description.lower()):
                matching_tasks.append(task)
        return matching_tasks

    def filter_tasks(self, status=None, priority=None, tag=None):
        """
        Filter tasks by status, priority, or tag

        Args:
            status (bool, optional): Filter by completion status
            priority (str, optional): Filter by priority level
            tag (str, optional): Filter by tag

        Returns:
            list: List of tasks that match the filter criteria
        """
        filtered_tasks = self.tasks

        if status is not None:
            filtered_tasks = [task for task in filtered_tasks if task.completed == status]

        if priority is not None:
            priority_lower = priority.lower()
            priority_map = {'h': 'high', 'm': 'medium', 'l': 'low'}
            normalized_priority = priority_map.get(priority_lower, priority_lower)
            filtered_tasks = [task for task in filtered_tasks if task.priority == normalized_priority]

        if tag is not None:
            filtered_tasks = [task for task in filtered_tasks if tag in task.tags]

        return filtered_tasks

    def sort_tasks(self, sort_by="priority"):
        """
        Sort tasks by specified criteria

        Args:
            sort_by (str): Criteria to sort by ('priority', 'due_date', 'title', 'status')

        Returns:
            list: List of sorted tasks
        """
        if sort_by == "priority":
            # Sort by priority: high, medium, low
            priority_order = {"high": 0, "medium": 1, "low": 2}
            return sorted(self.tasks, key=lambda task: priority_order.get(task.priority, 3))
        elif sort_by == "due_date":
            # Sort by due date (empty dates last)
            from datetime import datetime
            def date_key(task):
                if not task.due_date:
                    return datetime.max  # Put tasks without due date at the end
                try:
                    return datetime.strptime(task.due_date, "%Y-%m-%d")
                except ValueError:
                    return datetime.max  # In case of invalid date format
            return sorted(self.tasks, key=date_key)
        elif sort_by == "title":
            # Sort by title alphabetically
            return sorted(self.tasks, key=lambda task: task.title.lower())
        elif sort_by == "status":
            # Sort by status (incomplete first, then complete)
            return sorted(self.tasks, key=lambda task: task.completed)
        else:
            # Default to sorting by priority
            priority_order = {"high": 0, "medium": 1, "low": 2}
            return sorted(self.tasks, key=lambda task: priority_order.get(task.priority, 3))

    def get_task_by_id(self, task_id):
        """
        Get a specific task by its ID

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Task: The task with the specified ID, or None if not found
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id, title=None, description=None, priority=None, due_date=None):
        """
        Update an existing task's title, description, priority, and/or due date

        Args:
            task_id (int): The ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task
            priority (str, optional): New priority for the task
            due_date (str, optional): New due date for the task

        Returns:
            Task: The updated task, or None if task not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            # Only call update with non-None values
            update_kwargs = {}
            if title is not None:
                update_kwargs['title'] = title
            if description is not None:
                update_kwargs['description'] = description
            if priority is not None:
                update_kwargs['priority'] = priority
            if due_date is not None:
                update_kwargs['due_date'] = due_date

            task.update(**update_kwargs)
            return task
        return None

    def delete_task(self, task_id):
        """
        Delete a task by its ID

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if task was deleted, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def mark_task_complete(self, task_id):
        """
        Mark a task as complete by its ID

        Args:
            task_id (int): The ID of the task to mark as complete

        Returns:
            bool: True if task was marked complete, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.mark_complete()
            return True
        return False

    def mark_task_incomplete(self, task_id):
        """
        Mark a task as incomplete by its ID

        Args:
            task_id (int): The ID of the task to mark as incomplete

        Returns:
            bool: True if task was marked incomplete, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.mark_incomplete()
            return True
        return False

    def get_next_id(self):
        """
        Get the next available task ID

        Returns:
            int: The next available task ID
        """
        return self.next_id

    def process_recurring_tasks(self):
        """
        Process recurring tasks at application startup.
        Check for completed recurring tasks and create new instances if needed.
        """
        completed_recurring_tasks = [task for task in self.tasks if task.should_create_next_occurrence()]

        for task in completed_recurring_tasks:
            # Create a new task instance with the same properties
            new_task = Task(
                task_id=self.next_id,
                title=task.title,
                description=task.description,
                priority=task.priority,
                tags=task.tags[:],  # Create a copy of the tags list
                due_date=task.due_date,
                recurrence_rule=task.recurrence_rule,
                recurrence_active=task.recurrence_active,
                original_task_id=task.id  # Reference to the original task
            )

            # Calculate the next occurrence date
            next_occurrence = task.calculate_next_occurrence()
            new_task.next_occurrence = next_occurrence

            # Add the new task to the list
            self.tasks.append(new_task)
            self.next_id += 1

    def get_recurring_tasks(self):
        """
        Get all recurring tasks

        Returns:
            list: List of recurring Task objects
        """
        return [task for task in self.tasks if task.is_recurring_task()]

    def disable_task_recurrence(self, task_id):
        """
        Disable recurrence for a specific task

        Args:
            task_id (int): The ID of the task to disable recurrence for

        Returns:
            Task: The updated task, or None if task not found
        """
        task = self.get_task_by_id(task_id)
        if task and task.is_recurring_task():
            task.recurrence_active = False
            return task
        return None

    def get_recurring_tasks_by_status(self, active=True):
        """
        Get recurring tasks filtered by their recurrence status

        Args:
            active (bool): Filter by active (True) or inactive (False) recurrence status

        Returns:
            list: List of recurring tasks with specified status
        """
        return [task for task in self.tasks if task.is_recurring_task() and task.recurrence_active == active]