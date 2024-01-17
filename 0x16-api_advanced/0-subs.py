#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """query a subreddit and retrive no of subscribers"""

    # Reddit API endpoint for getting subreddit informatiom
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid too many requests error
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}

    # send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        # parse JSON response to extract no of subscribers(data field)
        data = response.json().get('data', {})
        sub_count = data.get('subscribers', 0)
        return sub_count
    else:
        return 0
