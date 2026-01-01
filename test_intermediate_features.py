"""
Test script to verify all Intermediate Level Todo CLI functionality in a single run
"""
from src.services.todo_manager import TodoManager


def test_all_intermediate_functionality():
    # Initialize the TodoManager
    todo_manager = TodoManager()

    print("=== Testing Add Task with Priority, Tags, and Due Date ===")
    task1 = todo_manager.add_task("Test Task 1", "This is the first test task", priority="high", tags=["work", "urgent"], due_date="2025-12-31")
    print(f"Added: {task1}")

    task2 = todo_manager.add_task("Test Task 2", "This is the second test task", priority="low", tags=["personal"], due_date="2025-12-25")
    print(f"Added: {task2}")

    task3 = todo_manager.add_task("Test Task 3", "This is the third test task", priority="medium", tags=["work"])
    print(f"Added: {task3}")

    print("\n=== Testing List All Tasks ===")
    tasks = todo_manager.get_all_tasks()
    for task in tasks:
        print(task)

    print("\n=== Testing Priority Update ===")
    updated_task = todo_manager.update_task_priority(1, "low")
    print(f"Updated task 1 priority to low: {updated_task is not None}")
    print(f"Updated task: {todo_manager.get_task_by_id(1)}")

    print("\n=== Testing Add Tag ===")
    updated_task = todo_manager.add_tag_to_task(2, "important")
    print(f"Added 'important' tag to task 2: {updated_task is not None}")
    print(f"Updated task: {todo_manager.get_task_by_id(2)}")

    print("\n=== Testing Remove Tag ===")
    updated_task = todo_manager.remove_tag_from_task(2, "personal")
    print(f"Removed 'personal' tag from task 2: {updated_task is not None}")
    print(f"Updated task: {todo_manager.get_task_by_id(2)}")

    print("\n=== Testing Update Task with Multiple Fields ===")
    updated_task = todo_manager.update_task(3, title="Updated Task 3", description="Updated description", priority="high", due_date="2026-01-15")
    print(f"Updated task 3: {updated_task is not None}")
    print(f"Updated task: {todo_manager.get_task_by_id(3)}")

    print("\n=== Testing Search Functionality ===")
    search_results = todo_manager.search_tasks("updated")
    print(f"Search results for 'updated': {len(search_results)} tasks found")
    for task in search_results:
        print(f"  {task}")

    print("\n=== Testing Filter by Priority ===")
    filtered_tasks = todo_manager.filter_tasks(priority="high")
    print(f"Tasks with high priority: {len(filtered_tasks)} tasks found")
    for task in filtered_tasks:
        print(f"  {task}")

    print("\n=== Testing Filter by Tag ===")
    filtered_tasks = todo_manager.filter_tasks(tag="work")
    print(f"Tasks with 'work' tag: {len(filtered_tasks)} tasks found")
    for task in filtered_tasks:
        print(f"  {task}")

    print("\n=== Testing Filter by Status ===")
    # Mark a task as complete first
    todo_manager.mark_task_complete(1)
    filtered_tasks = todo_manager.filter_tasks(status=True)  # completed tasks
    print(f"Completed tasks: {len(filtered_tasks)} tasks found")
    for task in filtered_tasks:
        print(f"  {task}")

    print("\n=== Testing Sort by Priority ===")
    all_tasks = todo_manager.get_all_tasks()
    sorted_tasks = todo_manager.sort_tasks(sort_by="priority")
    print("Tasks sorted by priority (high first):")
    for task in sorted_tasks:
        print(f"  {task}")

    print("\n=== Testing Sort by Due Date ===")
    sorted_tasks = todo_manager.sort_tasks(sort_by="due_date")
    print("Tasks sorted by due date:")
    for task in sorted_tasks:
        print(f"  {task}")

    print("\n=== Testing Sort by Title ===")
    sorted_tasks = todo_manager.sort_tasks(sort_by="title")
    print("Tasks sorted by title:")
    for task in sorted_tasks:
        print(f"  {task}")

    print("\n=== Testing Error Handling ===")
    try:
        # Try to add a task with invalid priority
        todo_manager.add_task("Invalid Priority Task", priority="invalid")
    except ValueError as e:
        print(f"Caught expected error: {e}")

    try:
        # Try to add a task with invalid due date
        todo_manager.add_task("Invalid Date Task", due_date="invalid-date")
    except ValueError as e:
        print(f"Caught expected error: {e}")

    print("\n=== All Intermediate Features Tested Successfully! ===")


if __name__ == "__main__":
    test_all_intermediate_functionality()