#!/usr/bin/python3
"""
Module documentation
containig a lot
of lines
"""
import json
from sys import argv
import requests

if __name__ == '__main__':
    API_URL = 'https://jsonplaceholder.typicode.com'

    user_data = requests.get(f'{API_URL}/users/{argv[1]}/')
    user_tasks = requests.get(f'{API_URL}/users/{argv[1]}/todos')


    def byte_to_dict(byte):
        """
        FUNCTION
        """
        byte_str = byte.decode('utf-8')
        return json.loads(byte_str)


    if user_data.status_code == 200 and user_tasks.status_code == 200:
        user_name = byte_to_dict(user_data.content).get('name')
        user_tasks_dict = json.loads(user_tasks.content)
        tasks_done = [task for task in user_tasks_dict if task.get('completed')]

        first_line = f"Employee {user_name} is done with tasks({len(tasks_done)}/{len(user_tasks_dict)}):"

        print(first_line)
        for task in tasks_done:
            print('\t {}'.format(task.get('title')))

    else:
        print('Error:', user_data.status_code)
