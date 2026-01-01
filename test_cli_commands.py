#!/usr/bin/env python
"""
Test CLI commands for recurring tasks functionality
"""
import subprocess
import sys

def test_cli_commands():
    print("=== Testing CLI Commands for Recurring Tasks ===\n")

    # Test 1: Add recurring tasks
    print("1. Testing add command with recurrence:")
    result = subprocess.run([sys.executable, "main.py", "add", "CLI Daily Task", "--recur", "daily"],
                          capture_output=True, text=True)
    print(f"   Command: python main.py add CLI Daily Task --recur daily")
    print(f"   Output: {result.stdout.strip()}")
    if result.stderr:
        print(f"   Error: {result.stderr.strip()}")
    print()

    result = subprocess.run([sys.executable, "main.py", "add", "CLI Weekly Task", "--recur", "weekly"],
                          capture_output=True, text=True)
    print(f"   Command: python main.py add CLI Weekly Task --recur weekly")
    print(f"   Output: {result.stdout.strip()}")
    print()

    result = subprocess.run([sys.executable, "main.py", "add", "CLI Monthly Task", "--recur", "monthly"],
                          capture_output=True, text=True)
    print(f"   Command: python main.py add CLI Monthly Task --recur monthly")
    print(f"   Output: {result.stdout.strip()}")
    print()

    # Test 2: Add a regular task
    result = subprocess.run([sys.executable, "main.py", "add", "CLI Regular Task"],
                          capture_output=True, text=True)
    print(f"   Command: python main.py add CLI Regular Task")
    print(f"   Output: {result.stdout.strip()}")
    print()

    # Test 3: Mark a task as complete
    result = subprocess.run([sys.executable, "main.py", "complete", "1"],
                          capture_output=True, text=True)
    print(f"   Command: python main.py complete 1")
    print(f"   Output: {result.stdout.strip()}")
    print()

    # Test 4: Test disable-recurrence command
    result = subprocess.run([sys.executable, "main.py", "disable-recurrence", "1"],
                          capture_output=True, text=True)
    print(f"   Command: python main.py disable-recurrence 1")
    print(f"   Output: {result.stdout.strip()}")
    print()

    # Test 5: Test list-recurring command
    result = subprocess.run([sys.executable, "main.py", "list-recurring"],
                          capture_output=True, text=True)
    print(f"   Command: python main.py list-recurring")
    print(f"   Output: {result.stdout.strip()}")
    print()

    # Test 6: Test list-recurring with active filter
    result = subprocess.run([sys.executable, "main.py", "list-recurring", "--active", "true"],
                          capture_output=True, text=True)
    print(f"   Command: python main.py list-recurring --active true")
    print(f"   Output: {result.stdout.strip()}")
    print()

    result = subprocess.run([sys.executable, "main.py", "list-recurring", "--active", "false"],
                          capture_output=True, text=True)
    print(f"   Command: python main.py list-recurring --active false")
    print(f"   Output: {result.stdout.strip()}")
    print()

    print("CLI COMMANDS TEST COMPLETED!")

if __name__ == "__main__":
    test_cli_commands()