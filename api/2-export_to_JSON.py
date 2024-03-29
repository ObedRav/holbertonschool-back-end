#!/usr/bin/python3
"""
Module documentation
containig a lot
of lines
"""
import json
import requests
from sys import argv

API_URL = 'https://jsonplaceholder.typicode.com'

user_id = argv[1]
response = \
    requests.get(
        f'{API_URL}/users/{user_id}/todos',
        params={'_expand': 'user'}
    )

if response.status_code == 200:
    data = response.json()

    dictionary = {user_id: []}

    with open(f'{user_id}.json', 'w', encoding='utf-8') as f:
        for task in data:
            current_dict = {
                'task': task['title'],
                'completed': task['completed'],
                'username': task['user']['username']
            }
            dictionary[user_id].append(current_dict)
        json.dump(dictionary, f)
else:
    print(f"Error: {response.status_code}")
