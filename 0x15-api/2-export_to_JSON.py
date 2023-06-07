#!/usr/bin/python3
"""
Gather Data from an API and Export to JSON
"""

import requests
import sys
import json


def fetch_employee_data(employee_id):
    """
    Fetch employee data from the API based on the provided employee ID
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    employee_data = response.json()
    return employee_data


def fetch_todo_data(employee_id):
    """
    Fetch TODO data from the API based on the provided employee ID
    """
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    todo_data = response.json()
    return todo_data


def display_todo_progress(employee_data, todo_data):
    """
    Display the TODO list progress for the employee
    """
    employee_name = employee_data['name']
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])

    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")


def export_to_json(employee_id, employee_data, todo_data):
    """
    Export the TODO data to JSON format
    """
    filename = f"{employee_id}.json"
    employee_username = employee_data['username']
    data = {
        str(employee_id): [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_username
            }
            for task in todo_data
        ]
    }

    with open(filename, mode='w') as file:
        json.dump(data, file)

    print(f"Data exported to {filename}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_data = fetch_employee_data(employee_id)
    todo_data = fetch_todo_data(employee_id)
    display_todo_progress(employee_data, todo_data)
    export_to_json(employee_id, employee_data, todo_data)
