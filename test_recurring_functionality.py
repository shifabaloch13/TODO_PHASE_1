#!/usr/bin/env python
"""
Test script to verify the recurring tasks functionality
"""
from src.services.todo_manager import TodoManager

def test_recurring_tasks():
    # Initialize the TodoManager
    todo_manager = TodoManager()

    print("=== Adding recurring tasks ===")
    daily_task = todo_manager.add_task("Daily Exercise", "Morning workout", recurrence_rule="daily")
    print(f"Added: {daily_task}")

    weekly_task = todo_manager.add_task("Weekly Team Meeting", "Weekly sync meeting", recurrence_rule="weekly")
    print(f"Added: {weekly_task}")

    monthly_task = todo_manager.add_task("Monthly Report", "Monthly status report", recurrence_rule="monthly")
    print(f"Added: {monthly_task}")

    print("\n=== All tasks ===")
    for task in todo_manager.get_all_tasks():
        print(task)

    print("\n=== Marking daily task as complete ===")
    todo_manager.mark_task_complete(1)
    print(f"Task 1 completed: {todo_manager.get_task_by_id(1).completed}")

    print("\n=== Before processing recurring tasks ===")
    print(f"Total tasks: {len(todo_manager.get_all_tasks())}")
    for task in todo_manager.get_all_tasks():
        print(task)

    print("\n=== Processing recurring tasks (simulating app restart) ===")
    todo_manager.process_recurring_tasks()

    print("\n=== After processing recurring tasks ===")
    print(f"Total tasks: {len(todo_manager.get_all_tasks())}")
    for task in todo_manager.get_all_tasks():
        print(task)

    print("\n=== Testing list recurring tasks ===")
    recurring_tasks = todo_manager.get_recurring_tasks()
    print(f"Found {len(recurring_tasks)} recurring tasks:")
    for task in recurring_tasks:
        print(task)

if __name__ == "__main__":
    test_recurring_tasks()