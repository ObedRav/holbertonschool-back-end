#!/usr/bin/python3
"""
Module documentation
containig a lot
of lines
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    API_URL = 'https://jsonplaceholder.typicode.com'

    response = \
        requests.get(
            f'{API_URL}/todos',
            params={'_expand': 'user'}
        )

    if response.status_code == 200:
        data = response.json()

        dictionary = dict()

        for task in data:
            dictionary[task['userId']] = []

        with open('todo_all_employees.json', 'w', encoding='utf-8') as f:
            for task in data:
                current_dict = {
                    'username': task['user']['username'],
                    'task': task['title'],
                    'completed': task['completed']
                }
                dictionary[task['userId']].append(current_dict)
            json.dump(dictionary, f, indent=4)
    else:
        print(f"Error: {response.status_code}")
