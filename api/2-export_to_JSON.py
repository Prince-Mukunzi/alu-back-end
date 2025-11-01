#!/usr/bin/python3
"""
Exports all tasks of a given employee ID to a JSON file.
Usage: python3 2-export_to_JSON.py <USER_ID>
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <USER_ID>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]

    # Base URLs for the API
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Get user info
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)
    user = user_response.json()
    username = user.get("username")

    # Get todos for this user
    todos = requests.get(todos_url, params={"userId": user_id}).json()

    # Build the list of task dictionaries
    task_list = []
    for task in todos:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        task_list.append(task_dict)

    # Export to JSON file named USER_ID.json
    data = {user_id: task_list}
    filename = "{}.json".format(user_id)
    with open(filename, "w") as json_file:
        json.dump(data, json_file)

