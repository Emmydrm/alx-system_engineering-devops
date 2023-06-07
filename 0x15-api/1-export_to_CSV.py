#!/usr/bin/python3
"""
Gather Data from an API and Export to CSV
"""

import requests
import sys
import csv


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


def export_to_csv(employee_id, employee_data, todo_data):
    """
    Export the TODO data to CSV format
    """
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            writer.writerow([employee_id, employee_data['username'], task['completed'], task['title']])

    print(f"Data exported to {filename}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_data = fetch_employee_data(employee_id)
    todo_data = fetch_todo_data(employee_id)
    display_todo_progress(employee_data, todo_data)
    export_to_csv(employee_id, employee_data, todo_data)
