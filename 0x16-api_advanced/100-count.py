#!/usr/bin/python3
"""parses module from reddit api."""


import requests


def count_words(subreddit, word_list, after='', cntr_lst={}):
    """pass the title and prints a sorted count of given keywords"""

    if not cntr_lst:
        for word in word_list:
            if word.lower() not in cntr_lst:
                cntr_lst[word.lower()] = 0

    if after is None:
        wordict = sorted(cntr_lst.items(), key=lambda x: (-x[1], x[0]))
        for word in wordict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url, headers=header, params=parameters,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hot = response.json()['data']['children']
        aft = response.json()['data']['after']
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in cntr_lst.keys():
                cntr_lst[word] += lower.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, aft, cntr_lst)