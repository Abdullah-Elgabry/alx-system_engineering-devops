#!/usr/bin/python3
""" Get [] of emp from api """

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    result_js = requests.get(url)
    emp = result_js.json()

    users_dict = {}
    for user in emp:
        EMP_PK = user.get('id')
        EMP_UN = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(EMP_PK)
        url = url + '/todos/'
        result_js = requests.get(url)

        tasks = result_js.json()
        users_dict[EMP_PK] = []
        for task in tasks:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            users_dict[EMP_PK].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": EMP_UN
            })
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
