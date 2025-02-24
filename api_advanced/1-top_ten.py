#!/usr/bin/python3
"""
This script queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

Usage:
Call the `top_ten` function with a subreddit name as a parameter.

Example:
top_ten('programming')
"""

import requests


def top_ten(subreddit):
    """Print the top 10 hot posts from a subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'myapp'}
    
    # Send the GET request to Reddit API
    response = requests.get(url, headers=headers)

    # Check if the subreddit exists (valid subreddit)
    if response.status_code == 200:
        # Parse the response data
        posts = response.json()['data']['children']
        
        # Print the titles of the top 10 hot posts
        for post in posts:
            print(post['data']['title'])
    else:
        # Print None if the subreddit is invalid
        print(None)

