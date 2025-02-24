#!/usr/bin/python3
"""
Recursive function to count occurrences of keywords in Reddit's hot articles.
"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Queries the Reddit API, parses titles of all hot articles,
    and counts occurrences of given keywords recursively.

    :param subreddit: The subreddit to query
    :param word_list: List of keywords to count (case-insensitive)
    :param word_count: Dictionary to store keyword counts
    :param after: Token for pagination (default: None)
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    params = {"limit": 100, "after": after}  # Fetch up to 100 results per request
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if subreddit is invalid (status 404) or a redirect
    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after", None)  # Get pagination token for next batch

    # Normalize keywords (case-insensitive, avoid duplicates)
    word_list = [word.lower() for word in word_list]

    # Process each post title
    for post in posts:
        title = post["data"]["title"].lower().split()  # Convert title to lowercase & split words
        for word in word_list:
            word_count[word] = word_count.get(word, 0) + title.count(word)  # Count occurrences

    # Recursive call if there are more pages
    if after:
        return count_words(subreddit, word_list, word_count, after)

    # Print results when recursion ends
    if word_count:
        sorted_results = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_results:
            if count > 0:
                print(f"{word}: {count}")

