#!/usr/bin/python3
"""
Module documentation
containig a lot
of lines
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    API_URL = 'https://jsonplaceholder.typicode.com'

    user_id = argv[1]
    response = \
        requests.get(
            f'{API_URL}/users/{user_id}/todos',
            params={'_expand': 'user'}
        )

    if response.status_code == 200:
        data = response.json()
        username = data[0]['user']['username']

        with open(f"{user_id}.csv", "w", encoding='utf-8', newline="") as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for task in data:
                writer.writerow(
                    [
                        f"{user_id}",
                        f"{username}",
                        f"{task['completed']}",
                        f"{task['title']}"
                    ]
                )
    else:
        print(f"Error: {response.status_code}")
