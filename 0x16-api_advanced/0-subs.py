#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """query a subreddit and retrive no of subscribers"""

    # Reddit API endpoint for getting subreddit informatiom
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set a custom User-Agent to avoid too many requests error
    headers = {'User-Agent': 'subs'}

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
