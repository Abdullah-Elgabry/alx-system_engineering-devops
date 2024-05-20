#!/usr/bin/python3
""" convert api to Json data """
import csv
import json
import requests
import sys


if __name__ == '__main__':
    EMP_PK = sys.argv[1]
    url_json = 'https://jsonplaceholder.typicode.com/users/' + EMP_PK
    ret_tsk = requests.get(url_json)
    EMP_UN = ret_tsk.json().get('username')
    tsk_ptr = url_json + '/todos'
    ret_tsk = requests.get(tsk_ptr)
    tasks = ret_tsk.json()
    repo_sc = {EMP_PK: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        repo_sc[EMP_PK].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": EMP_UN})
    with open('{}.json'.format(EMP_PK), 'w') as f:
        json.dump(repo_sc, f)
