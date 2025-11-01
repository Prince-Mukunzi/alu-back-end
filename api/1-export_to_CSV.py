#!/usr/bin/python3
import requests
import sys
import csv

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # URLs
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    # Fetch data
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data from API.")
        sys.exit(1)

    user = user_response.json()
    todos = todos_response.json()

    employee_name = user.get("username")

    # CSV file name
    filename = "{}.csv".format(employee_id)

    # Write to CSV
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                employee_name,
                task.get("completed"),
                task.get("title")
            ])

    print("Data exported successfully to {}".format(filename))

if __name__ == "__main__":
    main()

