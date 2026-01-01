"""
Todo CLI Application
Command-line interface for managing a todo list in memory
"""

import sys
import argparse
from src.services.todo_manager import TodoManager
import colorama
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)


def create_parser():
    """Create and configure the argument parser for the CLI"""
    parser = argparse.ArgumentParser(
        description="Todo CLI Application - Manage your tasks from the command line"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", nargs="?", help="Task title")
    add_parser.add_argument("description", nargs="?", default="", help="Task description")
    add_parser.add_argument("--priority", "-p", default="medium", help="Task priority (high, medium, low or h, m, l)")
    add_parser.add_argument("--tags", help="Comma-separated list of tags for the task")
    add_parser.add_argument("--due-date", help="Due date in YYYY-MM-DD format")
    add_parser.add_argument("--recur", choices=["daily", "weekly", "monthly"], help="Recurrence pattern for the task (daily, weekly, monthly)")

    # List command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("--priority", help="Filter tasks by priority (high, medium, low or h, m, l)")
    list_parser.add_argument("--tag", help="Filter tasks by tag")
    list_parser.add_argument("--status", choices=["complete", "incomplete"], help="Filter tasks by completion status")
    list_parser.add_argument("--sort", choices=["priority", "due_date", "title", "status"], help="Sort tasks by specified criteria")

    # Search command
    search_parser = subparsers.add_parser("search", help="Search tasks by keyword")
    search_parser.add_argument("keyword", help="Keyword to search for in title and description")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as complete")
    complete_parser.add_argument("id", type=int, help="Task ID to mark as complete")

    # Incomplete command
    incomplete_parser = subparsers.add_parser("incomplete", help="Mark a task as incomplete")
    incomplete_parser.add_argument("id", type=int, help="Task ID to mark as incomplete")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int, help="Task ID to update")
    update_parser.add_argument("title", nargs="?", help="New task title")
    update_parser.add_argument("description", nargs="?", help="New task description")

    # Update-priority command
    update_priority_parser = subparsers.add_parser("update-priority", help="Update task priority")
    update_priority_parser.add_argument("id", type=int, help="Task ID to update")
    update_priority_parser.add_argument("priority", help="New priority level (high, medium, low or h, m, l)")

    # Add-tag command
    add_tag_parser = subparsers.add_parser("add-tag", help="Add a tag to a task")
    add_tag_parser.add_argument("id", type=int, help="Task ID to update")
    add_tag_parser.add_argument("tag", help="Tag to add to the task")

    # Remove-tag command
    remove_tag_parser = subparsers.add_parser("remove-tag", help="Remove a tag from a task")
    remove_tag_parser.add_argument("id", type=int, help="Task ID to update")
    remove_tag_parser.add_argument("tag", help="Tag to remove from the task")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID to delete")

    # Disable recurrence command
    disable_recurrence_parser = subparsers.add_parser("disable-recurrence", help="Disable recurrence for a task")
    disable_recurrence_parser.add_argument("id", type=int, help="Task ID to disable recurrence for")

    # List recurring tasks command
    list_recurring_parser = subparsers.add_parser("list-recurring", help="List all recurring tasks")
    list_recurring_parser.add_argument("--active", choices=["true", "false"], help="Filter by recurrence active status (true/false)")

    # Interactive mode command
    subparsers.add_parser("interactive", help="Run the application in interactive mode")

    return parser


def handle_add_command(todo_manager, args):
    """Handle the 'add' command to add a new task"""
    try:
        if not args.title:
            print(f"{Fore.RED}Error: Task title cannot be empty{Style.RESET_ALL}")
            return

        if len(args.title) > 200:
            print(f"{Fore.RED}Error: Task title cannot exceed 200 characters{Style.RESET_ALL}")
            return

        if len(args.description) > 500:
            print(f"{Fore.RED}Error: Task description cannot exceed 500 characters{Style.RESET_ALL}")
            return

        # Process tags from comma-separated string
        tags = None
        if args.tags:
            tags = [tag.strip() for tag in args.tags.split(",") if tag.strip()]

        # Process recurrence option
        recurrence_rule = args.recur

        task = todo_manager.add_task(args.title, args.description, args.priority, tags, args.due_date, recurrence_rule)
        print(f"{Fore.GREEN}+ Task added successfully!{Style.RESET_ALL}")
        print(f"  {Fore.CYAN}ID:{Style.RESET_ALL} {task.id}")
        print(f"  {Fore.CYAN}Title:{Style.RESET_ALL} {task.title}")
        if task.recurrence_rule:
            print(f"  {Fore.CYAN}Recurrence:{Style.RESET_ALL} {Fore.MAGENTA}{task.recurrence_rule}{Style.RESET_ALL} {Fore.GREEN}(active){Style.RESET_ALL}")
    except ValueError as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Unexpected error: {str(e)}{Style.RESET_ALL}")


def handle_list_command(todo_manager, args):
    """Handle the 'list' command to display all tasks"""
    try:
        # Apply filters based on arguments
        tasks = todo_manager.get_all_tasks()

        # Apply status filter
        if args.status:
            status_bool = args.status == "complete"
            tasks = [task for task in tasks if task.completed == status_bool]

        # Apply priority filter
        if args.priority:
            tasks = todo_manager.filter_tasks(priority=args.priority)

        # Apply tag filter
        if args.tag:
            tasks = [task for task in tasks if args.tag in task.tags]

        # Apply sorting
        if args.sort:
            tasks = todo_manager.sort_tasks(sort_by=args.sort)

        # If no filters were applied, just get all tasks
        if not (args.status or args.priority or args.tag or args.sort):
            tasks = todo_manager.get_all_tasks()

        if not tasks:
            print(f"{Fore.YELLOW}No tasks found.{Style.RESET_ALL}")
            return

        print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Task List ({len(tasks)} task{'s' if len(tasks) != 1 else ''}):{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")

        for i, task in enumerate(tasks, 1):
            print(f"  {Fore.WHITE}{i}.{Style.RESET_ALL} {task}")

        print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error listing tasks: {str(e)}{Style.RESET_ALL}")


def handle_search_command(todo_manager, args):
    """Handle the 'search' command to search tasks by keyword"""
    try:
        tasks = todo_manager.search_tasks(args.keyword)

        if not tasks:
            print(f"{Fore.YELLOW}No tasks found containing '{Fore.CYAN}{args.keyword}{Fore.YELLOW}'.{Style.RESET_ALL}")
            return

        print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Search Results for '{Fore.MAGENTA}{args.keyword}{Fore.CYAN}' ({len(tasks)} task{'s' if len(tasks) != 1 else ''}):{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")

        for i, task in enumerate(tasks, 1):
            print(f"  {Fore.WHITE}{i}.{Style.RESET_ALL} {task}")

        print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error searching tasks: {str(e)}{Style.RESET_ALL}")


def handle_complete_command(todo_manager, args):
    """Handle the 'complete' command to mark a task as complete"""
    try:
        success = todo_manager.mark_task_complete(args.id)
        if success:
            print(f"{Fore.GREEN}+ Task {Fore.CYAN}{args.id}{Fore.GREEN} marked as complete.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}- Task with ID {Fore.CYAN}{args.id}{Fore.RED} not found.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error marking task as complete: {str(e)}{Style.RESET_ALL}")


def handle_incomplete_command(todo_manager, args):
    """Handle the 'incomplete' command to mark a task as incomplete"""
    try:
        success = todo_manager.mark_task_incomplete(args.id)
        if success:
            print(f"{Fore.YELLOW}-> Task {Fore.CYAN}{args.id}{Fore.YELLOW} marked as incomplete.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}- Task with ID {Fore.CYAN}{args.id}{Fore.RED} not found.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error marking task as incomplete: {str(e)}{Style.RESET_ALL}")


def handle_update_priority_command(todo_manager, args):
    """Handle the 'update-priority' command to update task priority"""
    try:
        # Validate priority input
        if args.priority.lower() not in ['high', 'medium', 'low', 'h', 'm', 'l']:
            print(f"{Fore.RED}Error: Invalid priority level. Use 'high', 'medium', or 'low'.{Style.RESET_ALL}")
            return

        updated_task = todo_manager.update_task_priority(args.id, args.priority)
        if updated_task:
            priority_color = Fore.RED if updated_task.priority == 'high' else Fore.YELLOW if updated_task.priority == 'medium' else Fore.GREEN
            print(f"{Fore.GREEN}+ Priority updated successfully for task {Fore.CYAN}{args.id}{Fore.GREEN} to {priority_color}{updated_task.priority}{Fore.GREEN}.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}- Task with ID {Fore.CYAN}{args.id}{Fore.RED} not found.{Style.RESET_ALL}")
    except ValueError as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error updating task priority: {str(e)}{Style.RESET_ALL}")


def handle_add_tag_command(todo_manager, args):
    """Handle the 'add-tag' command to add a tag to a task"""
    try:
        updated_task = todo_manager.add_tag_to_task(args.id, args.tag)
        if updated_task:
            print(f"{Fore.GREEN}+ Tag '{Fore.CYAN}{args.tag}{Fore.GREEN}' added to task {Fore.CYAN}{args.id}{Fore.GREEN}.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}- Task with ID {Fore.CYAN}{args.id}{Fore.RED} not found.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error adding tag to task: {str(e)}{Style.RESET_ALL}")


def handle_remove_tag_command(todo_manager, args):
    """Handle the 'remove-tag' command to remove a tag from a task"""
    try:
        updated_task = todo_manager.remove_tag_from_task(args.id, args.tag)
        if updated_task:
            print(f"{Fore.YELLOW}- Tag '{Fore.CYAN}{args.tag}{Fore.YELLOW}' removed from task {Fore.CYAN}{args.id}{Fore.YELLOW}.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}- Task with ID {Fore.CYAN}{args.id}{Fore.RED} not found.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error removing tag from task: {str(e)}{Style.RESET_ALL}")


def handle_update_command(todo_manager, args):
    """Handle the 'update' command to update a task"""
    try:
        # Determine which values to update
        title_to_update = args.title
        description_to_update = args.description

        # Validate inputs if they are provided
        if title_to_update is not None:
            if not title_to_update or not title_to_update.strip():
                print(f"{Fore.RED}Error: Task title cannot be empty{Style.RESET_ALL}")
                return
            if len(title_to_update) > 200:
                print(f"{Fore.RED}Error: Task title cannot exceed 200 characters{Style.RESET_ALL}")
                return

        if description_to_update is not None and len(description_to_update) > 500:
            print(f"{Fore.RED}Error: Task description cannot exceed 500 characters{Style.RESET_ALL}")
            return

        updated_task = todo_manager.update_task(args.id, title_to_update, description_to_update)
        if updated_task:
            print(f"{Fore.GREEN}+ Task {Fore.CYAN}{args.id}{Fore.GREEN} updated successfully!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}- Task with ID {Fore.CYAN}{args.id}{Fore.RED} not found.{Style.RESET_ALL}")
    except ValueError as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error updating task: {str(e)}{Style.RESET_ALL}")


def handle_delete_command(todo_manager, args):
    """Handle the 'delete' command to delete a task"""
    try:
        success = todo_manager.delete_task(args.id)
        if success:
            print(f"{Fore.RED}- Task {Fore.CYAN}{args.id}{Fore.RED} deleted successfully.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}- Task with ID {Fore.CYAN}{args.id}{Fore.RED} not found.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error deleting task: {str(e)}{Style.RESET_ALL}")


def handle_disable_recurrence_command(todo_manager, args):
    """Handle the 'disable-recurrence' command to disable recurrence for a task"""
    try:
        updated_task = todo_manager.disable_task_recurrence(args.id)
        if updated_task:
            print(f"{Fore.RED}- Recurrence disabled for task {Fore.CYAN}{args.id}{Fore.RED}.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}- Task with ID {Fore.CYAN}{args.id}{Fore.RED} not found or is not a recurring task.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error disabling recurrence: {str(e)}{Style.RESET_ALL}")


def handle_list_recurring_command(todo_manager, args):
    """Handle the 'list-recurring' command to list recurring tasks"""
    try:
        if args.active is not None:
            # Filter by active status
            active_status = args.active.lower() == "true"
            tasks = todo_manager.get_recurring_tasks_by_status(active=active_status)
            status_text = "active" if active_status else "inactive"
        else:
            # Get all recurring tasks
            tasks = todo_manager.get_recurring_tasks()
            status_text = "all"

        if not tasks:
            print(f"{Fore.YELLOW}No {status_text} recurring tasks found.{Style.RESET_ALL}")
            return

        print(f"{Fore.MAGENTA}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}Recurring Task List ({len(tasks)} {status_text} task{'s' if len(tasks) != 1 else ''}):{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{'='*50}{Style.RESET_ALL}")

        for i, task in enumerate(tasks, 1):
            print(f"  {Fore.WHITE}{i}.{Style.RESET_ALL} {task}")

        print(f"{Fore.MAGENTA}{'='*50}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error listing recurring tasks: {str(e)}{Style.RESET_ALL}")


def run_interactive_mode(todo_manager):
    """Run the application in interactive mode with a menu-driven interface"""
    print(f"{Fore.CYAN}")
    print("="*60)
    print("           TODO CLI APPLICATION - INTERACTIVE MODE")
    print("="*60)
    print(f"{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Welcome to the interactive Todo application!{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}You can manage your tasks step by step.{Style.RESET_ALL}")

    while True:
        print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}MAIN MENU:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}1.{Style.RESET_ALL} Add a new task")
        print(f"{Fore.GREEN}2.{Style.RESET_ALL} List all tasks")
        print(f"{Fore.GREEN}3.{Style.RESET_ALL} Search tasks")
        print(f"{Fore.GREEN}4.{Style.RESET_ALL} Complete a task")
        print(f"{Fore.GREEN}5.{Style.RESET_ALL} Mark task as incomplete")
        print(f"{Fore.GREEN}6.{Style.RESET_ALL} Update task")
        print(f"{Fore.GREEN}7.{Style.RESET_ALL} Update task priority")
        print(f"{Fore.GREEN}8.{Style.RESET_ALL} Add tag to task")
        print(f"{Fore.GREEN}9.{Style.RESET_ALL} Remove tag from task")
        print(f"{Fore.GREEN}10.{Style.RESET_ALL} Delete a task")
        print(f"{Fore.GREEN}11.{Style.RESET_ALL} List recurring tasks")
        print(f"{Fore.GREEN}12.{Style.RESET_ALL} Disable recurrence")
        print(f"{Fore.RED}13.{Style.RESET_ALL} Exit")
        print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")

        try:
            choice = input(f"\n{Fore.CYAN}Enter your choice (1-13): {Style.RESET_ALL}").strip()

            if choice == '1':
                # Add task
                title = input(f"{Fore.CYAN}Enter task title: {Style.RESET_ALL}")
                if not title:
                    print(f"{Fore.RED}Error: Task title cannot be empty{Style.RESET_ALL}")
                    continue

                description = input(f"{Fore.CYAN}Enter task description (optional): {Style.RESET_ALL}")

                print(f"{Fore.YELLOW}Choose priority:{Style.RESET_ALL}")
                print(f"  {Fore.GREEN}1.{Style.RESET_ALL} High")
                print(f"  {Fore.YELLOW}2.{Style.RESET_ALL} Medium")
                print(f"  {Fore.GREEN}3.{Style.RESET_ALL} Low")
                priority_choice = input(f"{Fore.CYAN}Enter priority (1-3, default 2): {Style.RESET_ALL}").strip()

                priority_map = {'1': 'high', '2': 'medium', '3': 'low'}
                priority = priority_map.get(priority_choice, 'medium')

                tags_input = input(f"{Fore.CYAN}Enter tags (comma-separated, optional): {Style.RESET_ALL}").strip()
                tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()] if tags_input else None

                print(f"{Fore.YELLOW}Set recurrence?{Style.RESET_ALL}")
                print(f"  {Fore.GREEN}1.{Style.RESET_ALL} Daily")
                print(f"  {Fore.GREEN}2.{Style.RESET_ALL} Weekly")
                print(f"  {Fore.GREEN}3.{Style.RESET_ALL} Monthly")
                print(f"  {Fore.YELLOW}4.{Style.RESET_ALL} None")
                recurrence_choice = input(f"{Fore.CYAN}Enter choice (1-4, default 4): {Style.RESET_ALL}").strip()

                recurrence_map = {'1': 'daily', '2': 'weekly', '3': 'monthly', '4': None}
                recurrence_rule = recurrence_map.get(recurrence_choice)

                try:
                    task = todo_manager.add_task(title, description, priority, tags, recurrence_rule=recurrence_rule)
                    print(f"{Fore.GREEN}+ Task added successfully!{Style.RESET_ALL}")
                    print(f"  {Fore.CYAN}ID:{Style.RESET_ALL} {task.id}")
                    print(f"  {Fore.CYAN}Title:{Style.RESET_ALL} {task.title}")
                    if task.recurrence_rule:
                        print(f"  {Fore.CYAN}Recurrence:{Style.RESET_ALL} {Fore.MAGENTA}{task.recurrence_rule}{Style.RESET_ALL} {Fore.GREEN}(active){Style.RESET_ALL}")
                except ValueError as e:
                    print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")

            elif choice == '2':
                # List tasks
                tasks = todo_manager.get_all_tasks()

                if not tasks:
                    print(f"{Fore.YELLOW}No tasks found.{Style.RESET_ALL}")
                    continue

                print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Task List ({len(tasks)} task{'s' if len(tasks) != 1 else ''}):{Style.RESET_ALL}")
                print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")

                for i, task in enumerate(tasks, 1):
                    print(f"  {Fore.WHITE}{i}.{Style.RESET_ALL} {task}")

                print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")

            elif choice == '3':
                # Search tasks
                keyword = input(f"{Fore.CYAN}Enter keyword to search: {Style.RESET_ALL}").strip()
                if not keyword:
                    print(f"{Fore.RED}Error: Keyword cannot be empty{Style.RESET_ALL}")
                    continue

                tasks = todo_manager.search_tasks(keyword)

                if not tasks:
                    print(f"{Fore.YELLOW}No tasks found containing '{Fore.CYAN}{keyword}{Fore.YELLOW}'.{Style.RESET_ALL}")
                    continue

                print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Search Results for '{Fore.MAGENTA}{keyword}{Fore.CYAN}' ({len(tasks)} task{'s' if len(tasks) != 1 else ''}):{Style.RESET_ALL}")
                print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")

                for i, task in enumerate(tasks, 1):
                    print(f"  {Fore.WHITE}{i}.{Style.RESET_ALL} {task}")

                print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")

            elif choice == '4':
                # Complete task
                try:
                    task_id = int(input(f"{Fore.CYAN}Enter task ID to mark as complete: {Style.RESET_ALL}"))
                    success = todo_manager.mark_task_complete(task_id)
                    if success:
                        print(f"{Fore.GREEN}+ Task {Fore.CYAN}{task_id}{Fore.GREEN} marked as complete.{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}- Task with ID {Fore.CYAN}{task_id}{Fore.RED} not found.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}Error: Please enter a valid task ID (number){Style.RESET_ALL}")

            elif choice == '5':
                # Mark incomplete
                try:
                    task_id = int(input(f"{Fore.CYAN}Enter task ID to mark as incomplete: {Style.RESET_ALL}"))
                    success = todo_manager.mark_task_incomplete(task_id)
                    if success:
                        print(f"{Fore.YELLOW}-> Task {Fore.CYAN}{task_id}{Fore.YELLOW} marked as incomplete.{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}- Task with ID {Fore.CYAN}{task_id}{Fore.RED} not found.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}Error: Please enter a valid task ID (number){Style.RESET_ALL}")

            elif choice == '6':
                # Update task
                try:
                    task_id = int(input(f"{Fore.CYAN}Enter task ID to update: {Style.RESET_ALL}"))
                    current_task = None
                    for task in todo_manager.get_all_tasks():
                        if task.id == task_id:
                            current_task = task
                            break

                    if not current_task:
                        print(f"{Fore.RED}- Task with ID {Fore.CYAN}{task_id}{Fore.RED} not found.{Style.RESET_ALL}")
                        continue

                    print(f"{Fore.YELLOW}Current task:{Style.RESET_ALL} {current_task}")
                    new_title = input(f"{Fore.CYAN}Enter new title (leave empty to keep current): {Style.RESET_ALL}").strip()
                    new_description = input(f"{Fore.CYAN}Enter new description (leave empty to keep current): {Style.RESET_ALL}").strip()

                    # Use existing values if user doesn't provide new ones
                    title_to_update = new_title if new_title else None
                    description_to_update = new_description if new_description else None

                    updated_task = todo_manager.update_task(task_id, title_to_update, description_to_update)
                    if updated_task:
                        print(f"{Fore.GREEN}+ Task {Fore.CYAN}{task_id}{Fore.GREEN} updated successfully!{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}- Task with ID {Fore.CYAN}{task_id}{Fore.RED} not found.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}Error: Please enter a valid task ID (number){Style.RESET_ALL}")

            elif choice == '7':
                # Update priority
                try:
                    task_id = int(input(f"{Fore.CYAN}Enter task ID to update priority: {Style.RESET_ALL}"))
                    print(f"{Fore.YELLOW}Choose new priority:{Style.RESET_ALL}")
                    print(f"  {Fore.RED}1.{Style.RESET_ALL} High")
                    print(f"  {Fore.YELLOW}2.{Style.RESET_ALL} Medium")
                    print(f"  {Fore.GREEN}3.{Style.RESET_ALL} Low")
                    priority_choice = input(f"{Fore.CYAN}Enter priority (1-3): {Style.RESET_ALL}").strip()

                    priority_map = {'1': 'high', '2': 'medium', '3': 'low'}
                    priority = priority_map.get(priority_choice)

                    if not priority:
                        print(f"{Fore.RED}Error: Invalid priority choice{Style.RESET_ALL}")
                        continue

                    updated_task = todo_manager.update_task_priority(task_id, priority)
                    if updated_task:
                        priority_color = Fore.RED if updated_task.priority == 'high' else Fore.YELLOW if updated_task.priority == 'medium' else Fore.GREEN
                        print(f"{Fore.GREEN}+ Priority updated successfully for task {Fore.CYAN}{task_id}{Fore.GREEN} to {priority_color}{updated_task.priority}{Fore.GREEN}.{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}- Task with ID {Fore.CYAN}{task_id}{Fore.RED} not found.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}Error: Please enter a valid task ID (number){Style.RESET_ALL}")

            elif choice == '8':
                # Add tag
                try:
                    task_id = int(input(f"{Fore.CYAN}Enter task ID to add tag: {Style.RESET_ALL}"))
                    tag = input(f"{Fore.CYAN}Enter tag to add: {Style.RESET_ALL}").strip()
                    if not tag:
                        print(f"{Fore.RED}Error: Tag cannot be empty{Style.RESET_ALL}")
                        continue

                    updated_task = todo_manager.add_tag_to_task(task_id, tag)
                    if updated_task:
                        print(f"{Fore.GREEN}+ Tag '{Fore.CYAN}{tag}{Fore.GREEN}' added to task {Fore.CYAN}{task_id}{Fore.GREEN}.{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}- Task with ID {Fore.CYAN}{task_id}{Fore.RED} not found.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}Error: Please enter a valid task ID (number){Style.RESET_ALL}")

            elif choice == '9':
                # Remove tag
                try:
                    task_id = int(input(f"{Fore.CYAN}Enter task ID to remove tag: {Style.RESET_ALL}"))
                    tag = input(f"{Fore.CYAN}Enter tag to remove: {Style.RESET_ALL}").strip()
                    if not tag:
                        print(f"{Fore.RED}Error: Tag cannot be empty{Style.RESET_ALL}")
                        continue

                    updated_task = todo_manager.remove_tag_from_task(task_id, tag)
                    if updated_task:
                        print(f"{Fore.YELLOW}- Tag '{Fore.CYAN}{tag}{Fore.YELLOW}' removed from task {Fore.CYAN}{task_id}{Fore.YELLOW}.{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}- Task with ID {Fore.CYAN}{task_id}{Fore.RED} not found.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}Error: Please enter a valid task ID (number){Style.RESET_ALL}")

            elif choice == '10':
                # Delete task
                try:
                    task_id = int(input(f"{Fore.CYAN}Enter task ID to delete: {Style.RESET_ALL}"))
                    success = todo_manager.delete_task(task_id)
                    if success:
                        print(f"{Fore.RED}- Task {Fore.CYAN}{task_id}{Fore.RED} deleted successfully.{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}- Task with ID {Fore.CYAN}{task_id}{Fore.RED} not found.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}Error: Please enter a valid task ID (number){Style.RESET_ALL}")

            elif choice == '11':
                # List recurring tasks
                print(f"{Fore.YELLOW}Filter recurring tasks?{Style.RESET_ALL}")
                print(f"  {Fore.GREEN}1.{Style.RESET_ALL} All recurring tasks")
                print(f"  {Fore.GREEN}2.{Style.RESET_ALL} Active recurring tasks")
                print(f"  {Fore.GREEN}3.{Style.RESET_ALL} Inactive recurring tasks")
                filter_choice = input(f"{Fore.CYAN}Enter choice (1-3, default 1): {Style.RESET_ALL}").strip()

                if filter_choice == '2':
                    tasks = todo_manager.get_recurring_tasks_by_status(active=True)
                    status_text = "active"
                elif filter_choice == '3':
                    tasks = todo_manager.get_recurring_tasks_by_status(active=False)
                    status_text = "inactive"
                else:
                    tasks = todo_manager.get_recurring_tasks()
                    status_text = "all"

                if not tasks:
                    print(f"{Fore.YELLOW}No {status_text} recurring tasks found.{Style.RESET_ALL}")
                    continue

                print(f"{Fore.MAGENTA}{'='*50}{Style.RESET_ALL}")
                print(f"{Fore.MAGENTA}Recurring Task List ({len(tasks)} {status_text} task{'s' if len(tasks) != 1 else ''}):{Style.RESET_ALL}")
                print(f"{Fore.MAGENTA}{'='*50}{Style.RESET_ALL}")

                for i, task in enumerate(tasks, 1):
                    print(f"  {Fore.WHITE}{i}.{Style.RESET_ALL} {task}")

                print(f"{Fore.MAGENTA}{'='*50}{Style.RESET_ALL}")

            elif choice == '12':
                # Disable recurrence
                try:
                    task_id = int(input(f"{Fore.CYAN}Enter task ID to disable recurrence: {Style.RESET_ALL}"))
                    updated_task = todo_manager.disable_task_recurrence(task_id)
                    if updated_task:
                        print(f"{Fore.RED}- Recurrence disabled for task {Fore.CYAN}{task_id}{Fore.RED}.{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}- Task with ID {Fore.CYAN}{task_id}{Fore.RED} not found or is not a recurring task.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}Error: Please enter a valid task ID (number){Style.RESET_ALL}")

            elif choice == '13':
                # Exit
                print(f"{Fore.GREEN}Thank you for using the Todo CLI Application!{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Goodbye!{Style.RESET_ALL}")
                break

            else:
                print(f"{Fore.RED}Invalid choice. Please enter a number between 1-13.{Style.RESET_ALL}")

        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}\nExiting application...{Style.RESET_ALL}")
            break
        except Exception as e:
            print(f"{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}")


def main():
    """Main function to run the Todo CLI application"""
    parser = create_parser()
    args = parser.parse_args()

    # Initialize the TodoManager
    todo_manager = TodoManager()

    # Process recurring tasks at startup (T006)
    todo_manager.process_recurring_tasks()

    # If no command is provided, show help
    if not args.command:
        print(f"{Fore.CYAN}")
        print("="*60)
        print("           TODO CLI APPLICATION")
        print("="*60)
        print(f"{Style.RESET_ALL}")
        parser.print_help()
        print(f"{Fore.CYAN}")
        print("="*60)
        print("           Use --help for more info")
        print("="*60)
        print(f"{Style.RESET_ALL}")
        return

    # Route to the appropriate command handler
    if args.command == "add":
        handle_add_command(todo_manager, args)
    elif args.command == "list":
        handle_list_command(todo_manager, args)
    elif args.command == "search":
        handle_search_command(todo_manager, args)
    elif args.command == "complete":
        handle_complete_command(todo_manager, args)
    elif args.command == "incomplete":
        handle_incomplete_command(todo_manager, args)
    elif args.command == "update":
        handle_update_command(todo_manager, args)
    elif args.command == "update-priority":
        handle_update_priority_command(todo_manager, args)
    elif args.command == "add-tag":
        handle_add_tag_command(todo_manager, args)
    elif args.command == "remove-tag":
        handle_remove_tag_command(todo_manager, args)
    elif args.command == "delete":
        handle_delete_command(todo_manager, args)
    elif args.command == "disable-recurrence":
        handle_disable_recurrence_command(todo_manager, args)
    elif args.command == "list-recurring":
        handle_list_recurring_command(todo_manager, args)
    elif args.command == "interactive":
        run_interactive_mode(todo_manager)


if __name__ == "__main__":
    main()