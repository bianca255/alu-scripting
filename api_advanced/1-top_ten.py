#!/usr/bin/python3
""" 1-top_ten.py """
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Send the GET request to Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Output check: non-existent subreddit
    if response.status_code != 200:
        print(None)
        return
    
    # Output check: existing subreddit
    posts = response.json()['data']['children']
    
    # Print the titles of the top 10 hot posts
    for post in posts:
        print(post['data']['title'])

