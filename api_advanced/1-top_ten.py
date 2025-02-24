#!/usr/bin/python3
""" 1-top_ten.py """
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print("OK")
        return
    
    posts = response.json()['data']['children']
    
    if len(posts) == 0:
        print("OK")
        return
    
    for post in posts:
        print(post['data']['title'])

