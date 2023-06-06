#!/usr/bin/python3
"""This module makes a request to the reddit api"""
import requests


def top_ten(subreddit):
    """gets the top ten posts of a subreddit"""
    headers = {
        'User-Agent': 'My User Agent 1.0',
    }
    try:
        res = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10", headers=headers, allow_redirects=False)
        subreddit_data = res.json()
    except Exception:
        print('None')
        return
    
    if 'error' in subreddit_data:
        print('None')
    else:
        details = subreddit_data['data']['children']
        for detail in details:
            print(detail['data']['title'])
