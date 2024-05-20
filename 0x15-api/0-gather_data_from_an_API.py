#!/usr/bin/python3
"""get emp data from down below api link"""


import re
import requests
import sys

URL = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            util = requests.get('{}/users/{}'.format(URL, id)).json()
            dn_task = requests.get('{}/todos'.format(URL)).json()
            emp_name = util.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, dn_task))
            task_done = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(task_done),
                    len(tasks)
                )
            )
            if len(task_done) > 0:
                for task in task_done:
                    print('\t {}'.format(task.get('title')))
