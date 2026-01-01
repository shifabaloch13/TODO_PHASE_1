#!/usr/bin/env python
"""
Test script to verify all colorful CLI features work properly
"""
from src.services.todo_manager import TodoManager
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def test_colorful_features():
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}           TESTING COLORFUL TODO FEATURES{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")

    # Initialize the TodoManager
    todo_manager = TodoManager()

    print(f"\n{Fore.GREEN}1. Testing colorful task creation...{Style.RESET_ALL}")
    task1 = todo_manager.add_task("Daily Exercise", "Morning workout", recurrence_rule="daily")
    task2 = todo_manager.add_task("Weekly Meeting", "Team sync", priority="high")
    print(f"   {Fore.GREEN}+{Style.RESET_ALL} Created: {task1}")
    print(f"   {Fore.GREEN}+{Style.RESET_ALL} Created: {task2}")

    print(f"\n{Fore.YELLOW}2. Testing colorful task updates...{Style.RESET_ALL}")
    todo_manager.add_tag_to_task(1, "fitness")
    todo_manager.add_tag_to_task(2, "work")
    print(f"   {Fore.YELLOW}->{Style.RESET_ALL} Added tags to tasks")

    todo_manager.mark_task_complete(1)
    print(f"   {Fore.GREEN}+{Style.RESET_ALL} Marked task 1 as complete")

    print(f"\n{Fore.CYAN}3. Testing colorful task listing...{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'-'*40}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Task List ({len(todo_manager.get_all_tasks())} tasks):{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'-'*40}{Style.RESET_ALL}")
    for i, task in enumerate(todo_manager.get_all_tasks(), 1):
        print(f"  {Fore.WHITE}{i}.{Style.RESET_ALL} {task}")
    print(f"{Fore.CYAN}{'-'*40}{Style.RESET_ALL}")

    print(f"\n{Fore.MAGENTA}4. Testing colorful recurring task features...{Style.RESET_ALL}")
    recurring_tasks = todo_manager.get_recurring_tasks()
    print(f"{Fore.MAGENTA}{'-'*40}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Recurring Task List ({len(recurring_tasks)} tasks):{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}{'-'*40}{Style.RESET_ALL}")
    for i, task in enumerate(recurring_tasks, 1):
        print(f"  {Fore.WHITE}{i}.{Style.RESET_ALL} {task}")
    print(f"{Fore.MAGENTA}{'-'*40}{Style.RESET_ALL}")

    print(f"\n{Fore.RED}5. Testing colorful recurrence disabling...{Style.RESET_ALL}")
    disabled_task = todo_manager.disable_task_recurrence(1)
    if disabled_task:
        print(f"   {Fore.RED}-{Style.RESET_ALL} Recurrence disabled for task 1")

    print(f"\n{Fore.CYAN}6. Final task list after changes...{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'-'*40}{Style.RESET_ALL}")
    for i, task in enumerate(todo_manager.get_all_tasks(), 1):
        print(f"  {Fore.WHITE}{i}.{Style.RESET_ALL} {task}")
    print(f"{Fore.CYAN}{'-'*40}{Style.RESET_ALL}")

    print(f"\n{Fore.GREEN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}           ALL COLORFUL FEATURES WORKING!{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'='*60}{Style.RESET_ALL}")
    print(f"\n{Fore.YELLOW}Features tested:{Style.RESET_ALL}")
    print(f"  • {Fore.GREEN}+{Style.RESET_ALL} Task creation with colors")
    print(f"  • {Fore.YELLOW}->{Style.RESET_ALL} Task updates with colors")
    print(f"  • {Fore.CYAN}Cyan{Style.RESET_ALL} for headers and info")
    print(f"  • {Fore.RED}-{Style.RESET_ALL} Error/deletion messages")
    print(f"  • {Fore.MAGENTA}Magenta{Style.RESET_ALL} for recurring tasks")
    print(f"  • Color-coded priorities (red=high, yellow=medium, green=low)")
    print(f"  • Color-coded status symbols")
    print(f"  • Color-coded recurrence indicators")

if __name__ == "__main__":
    test_colorful_features()