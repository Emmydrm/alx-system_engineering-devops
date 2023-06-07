#!/usr/bin/python3
"""
Python script that uses REST API to get information about employee tasks
and exports the data in JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    url_users = "https://jsonplaceholder.typicode.com/users"
    url_todos = "https://jsonplaceholder.typicode.com/todos"
    users = requests.get(url_users).json()
    todos = requests.get(url_todos).json()

    user_tasks = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        user_tasks[user_id] = []

        for todo in todos:
            if todo.get('userId') == user_id:
                task_title = todo.get('title')
                completed = todo.get('completed')
                task = {
                    "username": username,
                    "task": task_title,
                    "completed": completed
                }
                user_tasks[user_id].append(task)

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_tasks, json_file)

