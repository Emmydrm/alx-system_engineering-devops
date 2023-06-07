#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
using a REST API.
"""

import sys
import requests


def get_employee_info(employee_id):
    """Retrieve employee TODO list progress from the API."""
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos"

    # Retrieve employee name
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data.get("name")

    # Retrieve employee's completed tasks
    todos_response = requests.get(todos_url, params={"userId": employee_id})
    todos_data = todos_response.json()
    completed_tasks = [task for task in todos_data if task.get("completed")]

    return employee_name, completed_tasks, todos_data


def display_todo_progress(employee_name, completed_tasks, total_tasks):
    """Display the employee's TODO list progress."""
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        task_title = task.get("title")
        print(f"\t{task_title}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an employee ID as a parameter.")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    employee_name, completed_tasks, all_tasks = get_employee_info(employee_id)
    display_todo_progress(employee_name, completed_tasks, len(all_tasks))

