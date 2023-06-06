#!/usr/bin/python3
"""This module makes a request to the reddit api"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """recursively calls the reddit api to fetch all hot articles"""
    headers = {
            'User-Agent': 'My User Agent 1.0',
    }
    try:
        if after is None:
            return hot_list
        if after == '':
            res = requests.get('https://www.reddit.com/r/'+subreddit
                               + '/hot.json', headers=headers,
                               allow_redirects=False)
        else:
            res = requests.get('https://www.reddit.com/r/'+subreddit
                               + '/hot.json?after={}'.format(after),
                               headers=headers, allow_redirects=False)
        subreddit_data = res.json()
    except Exception:
        return (None)
    if 'error' in subreddit_data.keys():
        return (None)
    details = subreddit_data['data']['children']
    for detail in details:
        hot_list.append(detail['data']['title'])
    after = subreddit_data['data']['after']
    return (recurse(subreddit, hot_list, after))
