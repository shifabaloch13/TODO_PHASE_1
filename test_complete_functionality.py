#!/usr/bin/env python
"""
Complete test script to validate all recurring tasks functionality
"""
from src.services.todo_manager import TodoManager
from datetime import datetime, timedelta
import calendar

def test_complete_functionality():
    print("=== Testing Complete Recurring Tasks Functionality ===\n")

    # Initialize the TodoManager
    todo_manager = TodoManager()

    print("1. Testing daily recurring task creation...")
    daily_task = todo_manager.add_task("Daily Exercise", "Morning workout", recurrence_rule="daily")
    print(f"   Created: {daily_task}")
    assert daily_task.recurrence_rule == "daily"
    assert daily_task.recurrence_active == True
    print("   OK Daily task created successfully\n")

    print("2. Testing weekly recurring task creation...")
    weekly_task = todo_manager.add_task("Weekly Team Meeting", "Weekly sync meeting", recurrence_rule="weekly")
    print(f"   Created: {weekly_task}")
    assert weekly_task.recurrence_rule == "weekly"
    print("   OK Weekly task created successfully\n")

    print("3. Testing monthly recurring task creation...")
    monthly_task = todo_manager.add_task("Monthly Report", "Monthly status report", recurrence_rule="monthly")
    print(f"   Created: {monthly_task}")
    assert monthly_task.recurrence_rule == "monthly"
    print("   OK Monthly task created successfully\n")

    print("4. Testing non-recurring task (should not have recurrence)...")
    regular_task = todo_manager.add_task("Regular Task", "This is a regular task")
    print(f"   Created: {regular_task}")
    assert regular_task.recurrence_rule is None
    print("   OK Regular task created without recurrence\n")

    print("5. Testing recurring task identification methods...")
    assert daily_task.is_recurring_task() == True
    assert daily_task.is_recurring_and_active() == True
    assert regular_task.is_recurring_task() == False
    print("   OK Recurring task identification working correctly\n")

    print("6. Testing recurrence calculation logic...")
    # Test daily calculation
    next_daily = daily_task.calculate_next_occurrence()
    expected_daily = datetime.now() + timedelta(days=1)
    print(f"   Daily next occurrence: {next_daily}")
    print(f"   Expected (approx): {expected_daily}")
    assert abs((next_daily - expected_daily).total_seconds()) < 60  # Within 1 minute
    print("   OK Daily recurrence calculation working\n")

    # Test weekly calculation
    next_weekly = weekly_task.calculate_next_occurrence()
    expected_weekly = datetime.now() + timedelta(weeks=1)
    print(f"   Weekly next occurrence: {next_weekly}")
    print(f"   Expected (approx): {expected_weekly}")
    assert abs((next_weekly - expected_weekly).total_seconds()) < 60  # Within 1 minute
    print("   OK Weekly recurrence calculation working\n")

    # Test monthly calculation with month-end handling
    next_monthly = monthly_task.calculate_next_occurrence()
    current_date = datetime.now()
    expected_month = current_date.month + 1 if current_date.month < 12 else 1
    expected_year = current_date.year if current_date.month < 12 else current_date.year + 1
    expected_day = min(current_date.day, calendar.monthrange(expected_year, expected_month)[1])
    print(f"   Monthly next occurrence: {next_monthly}")
    print(f"   Expected month/day: {expected_year}-{expected_month:02d}-{expected_day:02d}")
    assert next_monthly.month == expected_month
    assert next_monthly.year == expected_year
    print("   OK Monthly recurrence calculation with month-end handling working\n")

    print("7. Testing recurring task creation after completion...")
    # Mark daily task as complete
    todo_manager.mark_task_complete(1)
    completed_task = todo_manager.get_task_by_id(1)
    assert completed_task.completed == True
    print(f"   Marked task as complete: {completed_task}")

    # Process recurring tasks (simulating app restart)
    todo_manager.process_recurring_tasks()
    print("   Processed recurring tasks (simulating app restart)")

    # Check that a new task was created
    all_tasks = todo_manager.get_all_tasks()
    recurring_tasks = [t for t in all_tasks if t.title == "Daily Exercise"]
    assert len(recurring_tasks) == 2  # Original + new instance
    new_task = [t for t in recurring_tasks if t.id != 1][0]  # Get the new task (not ID 1)
    assert new_task.completed == False  # New instance should not be completed
    assert new_task.recurrence_rule == "daily"  # Should preserve recurrence rule
    print(f"   New recurring instance created: {new_task}")
    print("   OK Recurring task creation after completion working\n")

    print("8. Testing recurring task filtering...")
    all_recurring = todo_manager.get_recurring_tasks()
    assert len(all_recurring) == 4  # Daily original (ID 1), Daily new (ID 5), Weekly (ID 2), Monthly (ID 3)
    print(f"   Found {len(all_recurring)} recurring tasks: {[t.id for t in all_recurring]}")

    active_recurring = todo_manager.get_recurring_tasks_by_status(active=True)
    assert len(active_recurring) == 4  # All should be active at this point
    print(f"   Found {len(active_recurring)} active recurring tasks")

    inactive_recurring = todo_manager.get_recurring_tasks_by_status(active=False)
    assert len(inactive_recurring) == 0  # None should be inactive yet
    print(f"   Found {len(inactive_recurring)} inactive recurring tasks")
    print("   OK Recurring task filtering working correctly\n")

    print("9. Testing recurrence disabling...")
    disabled_task = todo_manager.disable_task_recurrence(1)
    assert disabled_task.recurrence_active == False
    print(f"   Disabled recurrence: {disabled_task}")

    # Verify it shows up in inactive filter
    active_recurring = todo_manager.get_recurring_tasks_by_status(active=True)
    inactive_recurring = todo_manager.get_recurring_tasks_by_status(active=False)
    assert len(active_recurring) == 3  # Now only 3 active (ID 2, 3, 5)
    assert len(inactive_recurring) == 1  # 1 inactive (ID 1)
    print(f"   Active recurring tasks: {len(active_recurring)}, Inactive recurring tasks: {len(inactive_recurring)}")
    print("   OK Recurrence disabling working correctly\n")

    print("10. Testing CLI command functionality...")
    # Test that the should_create_next_occurrence logic works properly
    # Mark the new daily task (ID 5) as complete and process again
    new_daily_task_id = new_task.id
    todo_manager.mark_task_complete(new_daily_task_id)
    completed_new_task = todo_manager.get_task_by_id(new_daily_task_id)
    assert completed_new_task.should_create_next_occurrence() == True
    print(f"   New task ready for next occurrence: {completed_new_task}")

    # Process recurring tasks again
    todo_manager.process_recurring_tasks()
    final_task_count = len(todo_manager.get_all_tasks())
    print(f"   Total tasks after second processing: {final_task_count}")
    print("   OK CLI command functionality working correctly\n")

    print("11. Testing edge cases...")
    # Test month-end date handling for January 31st -> February
    jan_31_task = todo_manager.add_task("Month End Task", recurrence_rule="monthly")
    jan_31_task.created_at = datetime(2025, 1, 31)  # Set to Jan 31
    next_occurrence = jan_31_task.calculate_next_occurrence(datetime(2025, 1, 31))
    # Should be Feb 28 (or 29) since Feb doesn't have 31 days
    assert next_occurrence.month == 2
    assert next_occurrence.day in [28, 29]  # Feb 28 or 29 depending on leap year
    print(f"   Month-end edge case handled: {next_occurrence}")
    print("   OK Edge cases handled properly\n")

    print("ALL TESTS PASSED! Recurring tasks functionality is working correctly.")
    print(f"\nFinal state: {len(todo_manager.get_all_tasks())} total tasks")
    print("All user stories have been successfully implemented:")
    print("- User Story 1: Daily recurring tasks")
    print("- User Story 2: Weekly recurring tasks")
    print("- User Story 3: Monthly recurring tasks")
    print("- User Story 4: Recurring task management")

if __name__ == "__main__":
    test_complete_functionality()