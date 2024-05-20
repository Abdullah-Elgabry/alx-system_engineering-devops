#!/usr/bin/python3
""" get the api into csv file """


import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_cs = 'https://jsonplaceholder.typicode.com/users/' + user
    ret_tsk = requests.get(url_cs)
    user_name = ret_tsk.json().get('username')
    task = url_cs + '/todos'
    ret_tsk = requests.get(task)
    tasks = ret_tsk.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            title_task = task.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_task))
