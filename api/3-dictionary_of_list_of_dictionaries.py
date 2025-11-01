#!/usr/bin/python3
"""
Exports all employee tasks to a JSON file.
File: todo_all_employees.json
"""
import json
import requests


if __name__ == "__main__":
    # Base URLs for the API
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Get all users
    users = requests.get(users_url).json()

    # Create the main dictionary
    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # Get tasks for this user
        todos = requests.get(todos_url, params={"userId": user_id}).json()

        # Build the list of tasks
        task_list = []
        for task in todos:
            task_dict = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            task_list.append(task_dict)

        # Add to the main dictionary
        all_tasks[str(user_id)] = task_list

    # Export to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)

