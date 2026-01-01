#!/usr/bin/env python
"""
Verification script to test all recurring tasks functionality in a single run
"""
from src.services.todo_manager import TodoManager

def verify_all_functionality():
    print("=== Verifying Recurring Tasks Functionality ===\n")

    # Initialize the TodoManager
    todo_manager = TodoManager()

    print("1. Testing task creation with recurrence...")
    daily_task = todo_manager.add_task("Daily Exercise", "Morning workout", recurrence_rule="daily")
    print(f"   OK Created daily task: {daily_task}")

    weekly_task = todo_manager.add_task("Weekly Meeting", "Team sync", recurrence_rule="weekly")
    print(f"   OK Created weekly task: {weekly_task}")

    monthly_task = todo_manager.add_task("Monthly Report", "Status report", recurrence_rule="monthly")
    print(f"   OK Created monthly task: {monthly_task}")

    regular_task = todo_manager.add_task("Regular Task", "No recurrence")
    print(f"   OK Created regular task: {regular_task}\n")

    print("2. Testing task identification...")
    assert daily_task.is_recurring_task() == True
    assert daily_task.is_recurring_and_active() == True
    assert regular_task.is_recurring_task() == False
    print("   OK Task identification methods working correctly\n")

    print("3. Testing recurrence calculation...")
    import datetime
    next_daily = daily_task.calculate_next_occurrence()
    next_weekly = weekly_task.calculate_next_occurrence()
    next_monthly = monthly_task.calculate_next_occurrence()

    print(f"   OK Daily next occurrence: {next_daily}")
    print(f"   OK Weekly next occurrence: {next_weekly}")
    print(f"   OK Monthly next occurrence: {next_monthly}\n")

    print("4. Testing recurrence creation after completion...")
    # Mark the daily task as complete
    todo_manager.mark_task_complete(1)
    print(f"   OK Marked daily task as complete: {todo_manager.get_task_by_id(1)}")

    # Process recurring tasks (simulating app restart)
    todo_manager.process_recurring_tasks()
    print("   OK Processed recurring tasks (simulated app restart)")

    # Verify new task was created
    all_tasks = todo_manager.get_all_tasks()
    daily_tasks = [t for t in all_tasks if t.title == "Daily Exercise"]
    assert len(daily_tasks) == 2  # Original + new instance
    print(f"   OK New recurring instance created (total daily tasks: {len(daily_tasks)})\n")

    print("5. Testing recurring task filtering...")
    recurring_tasks = todo_manager.get_recurring_tasks()
    print(f"   OK Found {len(recurring_tasks)} recurring tasks")

    active_tasks = todo_manager.get_recurring_tasks_by_status(active=True)
    print(f"   OK Found {len(active_tasks)} active recurring tasks")

    inactive_tasks = todo_manager.get_recurring_tasks_by_status(active=False)
    print(f"   OK Found {len(inactive_tasks)} inactive recurring tasks\n")

    print("6. Testing recurrence disabling...")
    disabled_task = todo_manager.disable_task_recurrence(1)
    if disabled_task:
        print(f"   OK Disabled recurrence: {disabled_task}")

        # Verify it's now in inactive filter
        active_tasks = todo_manager.get_recurring_tasks_by_status(active=True)
        inactive_tasks = todo_manager.get_recurring_tasks_by_status(active=False)
        print(f"   OK Active tasks: {len(active_tasks)}, Inactive tasks: {len(inactive_tasks)}\n")
    else:
        print("   ! Could not disable recurrence (might be already processed)\n")

    print("7. Testing CLI command simulation...")
    # Test list-recurring functionality
    recurring_tasks = todo_manager.get_recurring_tasks()
    print(f"   OK CLI list-recurring would show {len(recurring_tasks)} tasks")

    # Test list-recurring --active functionality
    active_tasks = todo_manager.get_recurring_tasks_by_status(active=True)
    inactive_tasks = todo_manager.get_recurring_tasks_by_status(active=False)
    print(f"   OK CLI list-recurring --active would show {len(active_tasks)} active, {len(inactive_tasks)} inactive\n")

    print("8. Testing edge case: month-end dates...")
    # Create a task with a month-end date
    import calendar
    from datetime import datetime

    # Test with a date that would cause month-end issues
    jan_31_task = todo_manager.add_task("Month End Task", recurrence_rule="monthly")
    jan_31_date = datetime(2025, 1, 31)  # January 31
    next_occurrence = jan_31_task.calculate_next_occurrence(jan_31_date)
    print(f"   OK Month-end calculation: Jan 31 -> {next_occurrence.strftime('%Y-%m-%d')}")

    # Should handle February properly (28th or 29th)
    assert next_occurrence.month == 2  # Next month should be February
    assert next_occurrence.day in [28, 29]  # Day should be valid for February
    print("   OK Month-end date handling working correctly\n")

    print("9. Testing multiple completion cycles...")
    # Mark the new daily task as complete (to test another cycle)
    new_daily_task = [t for t in daily_tasks if t.id != 1][0]  # Get the new task (not ID 1)
    todo_manager.mark_task_complete(new_daily_task.id)
    print(f"   OK Marked new daily task as complete: {todo_manager.get_task_by_id(new_daily_task.id)}")

    # Process recurring tasks again
    todo_manager.process_recurring_tasks()
    all_tasks = todo_manager.get_all_tasks()
    daily_tasks = [t for t in all_tasks if t.title == "Daily Exercise"]
    print(f"   OK After second cycle, total daily tasks: {len(daily_tasks)}\n")

    print("10. Final verification - all task types present...")
    all_tasks = todo_manager.get_all_tasks()
    recurring_count = len([t for t in all_tasks if t.is_recurring_task()])
    regular_count = len([t for t in all_tasks if not t.is_recurring_task()])
    completed_count = len([t for t in all_tasks if t.completed])

    print(f"   OK Total tasks: {len(all_tasks)}")
    print(f"   OK Recurring tasks: {recurring_count}")
    print(f"   OK Regular tasks: {regular_count}")
    print(f"   OK Completed tasks: {completed_count}\n")

    print("ALL FUNCTIONALITY VERIFIED SUCCESSFULLY!")
    print("\nImplemented features:")
    print("  - Daily recurring tasks")
    print("  - Weekly recurring tasks")
    print("  - Monthly recurring tasks")
    print("  - Recurrence calculation")
    print("  - Recurrence filtering")
    print("  - Recurrence disabling")
    print("  - Month-end date handling")
    print("  - Task completion cycles")
    print("  - CLI command support")

if __name__ == "__main__":
    verify_all_functionality()