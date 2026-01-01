#!/usr/bin/env python
"""
Test script to verify the recurring tasks disable functionality
"""
from src.services.todo_manager import TodoManager

def test_disable_recurrence():
    # Initialize the TodoManager
    todo_manager = TodoManager()

    print("=== Adding recurring tasks ===")
    daily_task = todo_manager.add_task("Daily Exercise", "Morning workout", recurrence_rule="daily")
    print(f"Added: {daily_task}")

    print("\n=== Marking task as complete ===")
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

    print("\n=== Disabling recurrence for task 1 ===")
    updated_task = todo_manager.disable_task_recurrence(1)
    if updated_task:
        print(f"Recurrence disabled: {updated_task}")
    else:
        print("Failed to disable recurrence")

    print("\n=== Marking the new recurring task (ID 2) as complete ===")
    todo_manager.mark_task_complete(2)
    print(f"Task 2 completed: {todo_manager.get_task_by_id(2).completed}")

    print("\n=== Processing recurring tasks again (should not create new instance since original is disabled) ===")
    todo_manager.process_recurring_tasks()

    print("\n=== Final state ===")
    print(f"Total tasks: {len(todo_manager.get_all_tasks())}")
    for task in todo_manager.get_all_tasks():
        print(task)

if __name__ == "__main__":
    test_disable_recurrence()