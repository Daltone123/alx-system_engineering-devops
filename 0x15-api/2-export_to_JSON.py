#!/usr/bin/python3
"""
Python script that exports data in the JSON format.
"""
import json
from requests import get
from sys import argv

if __name__ == "__main__":
    # Fetch the to-do data
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    # Fetch the user data
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    u_name = None
    id_no = None

    # Find the username and ID for the given user ID
    for i in data2:
        if i['id'] == int(argv[1]):
            u_name = i['username']
            id_no = i['id']

    if u_name is None or id_no is None:
        # User ID was not found in the user data
        print(f"User ID {argv[1]} not found.")
        exit(1)

    row = []

    # Collect tasks for the given user ID
    for i in data:
        if i['userId'] == int(argv[1]):
            new_dict = {
                'username': u_name,
                'task': i['title'],
                'completed': i['completed']
            }
            row.append(new_dict)

    final_dict = {id_no: row}
    json_obj = json.dumps(final_dict, indent=4)

    # Write the JSON data to a file
    with open(f"{argv[1]}.json", "w") as f:
        f.write(json_obj)
#!/usr/bin/python3
"""
Python script that exports data in the JSON format.
"""

import json
from requests import get
from sys import argv

if __name__ == "__main__":
    # Fetch the to-do data
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    # Fetch the user data
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    u_name = None
    id_no = None

    # Find the username and ID for the given user ID
    for i in data2:
        if i['id'] == int(argv[1]):
            u_name = i['username']
            id_no = i['id']

    if u_name is None or id_no is None:
        # User ID was not found in the user data
        print(f"User ID {argv[1]} not found.")
        exit(1)

    row = []

    # Collect tasks for the given user ID
    for i in data:
        if i['userId'] == int(argv[1]):
            new_dict = {
                'username': u_name,
                'task': i['title'],
                'completed': i['completed']
            }
            row.append(new_dict)

    final_dict = {id_no: row}
    json_obj = json.dumps(final_dict, indent=4)

    # Write the JSON data to a file
    with open(f"{argv[1]}.json", "w") as f:
        f.write(json_obj)

