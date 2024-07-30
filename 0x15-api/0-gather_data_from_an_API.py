#!/usr/bin/python3

import sys
import requests

def get_employee_todo_progress(employee_id):
    # Define API endpoints
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Fetch employee details
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Employee not found")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch todos
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error: Could not retrieve TODOs")
        return

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]

    number_of_done_tasks = len(done_tasks)
    total_number_of_tasks = total_tasks

    # Output result
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: EMPLOYEE_ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

