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

