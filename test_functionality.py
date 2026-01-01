"""
Test script to verify all Todo CLI functionality in a single run
"""
from src.services.todo_manager import TodoManager


def test_all_functionality():
    # Initialize the TodoManager
    todo_manager = TodoManager()

    print("=== Testing Add Task ===")
    task1 = todo_manager.add_task("Test Task 1", "This is the first test task")
    print(f"Added: {task1}")

    task2 = todo_manager.add_task("Test Task 2")
    print(f"Added: {task2}")

    print("\n=== Testing List All Tasks ===")
    tasks = todo_manager.get_all_tasks()
    for task in tasks:
        print(task)

    print("\n=== Testing Mark Complete ===")
    success = todo_manager.mark_task_complete(1)
    print(f"Marked task 1 as complete: {success}")

    print("\n=== Testing List After Update ===")
    tasks = todo_manager.get_all_tasks()
    for task in tasks:
        print(task)

    print("\n=== Testing Update Task ===")
    updated_task = todo_manager.update_task(2, "Updated Task 2", "This task has been updated")
    print(f"Updated task 2: {updated_task is not None}")

    print("\n=== Testing List After Update ===")
    tasks = todo_manager.get_all_tasks()
    for task in tasks:
        print(task)

    print("\n=== Testing Delete Task ===")
    success = todo_manager.delete_task(1)
    print(f"Deleted task 1: {success}")

    print("\n=== Testing List After Deletion ===")
    tasks = todo_manager.get_all_tasks()
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("No tasks found.")

    print("\n=== Testing Error Handling ===")
    try:
        # Try to add a task with empty title
        todo_manager.add_task("")
    except ValueError as e:
        print(f"Caught expected error: {e}")

    try:
        # Try to add a task with too long title
        todo_manager.add_task("A" * 201)
    except ValueError as e:
        print(f"Caught expected error: {e}")


if __name__ == "__main__":
    test_all_functionality()