#!/usr/bin/python3
"""
Recursive function to get all hot article titles from a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of all hot article titles.

    :param subreddit: The subreddit to query
    :param hot_list: List of titles collected so far (default: empty list)
    :param after: Token for pagination (default: None)
    :return: List of hot article titles, or None if subreddit is invalid
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    params = {"limit": 100, "after": after}  # Fetch up to 100 posts per request
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Handle invalid subreddit (e.g., 404 error)
    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after", None)  # Get next page token

    # Append titles to hot_list
    for post in posts:
        hot_list.append(post["data"]["title"])

    # Recursively fetch more posts if `after` is not None
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list if hot_list else None  # Return None if no posts found

