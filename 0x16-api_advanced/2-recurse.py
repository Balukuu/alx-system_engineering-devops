import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    if after is None:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for post in posts:
            title = post.get('data', {}).get('title', '')
            hot_list.append(title)

        after = data.get('data', {}).get('after', None)
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"Error: Subreddit '{subreddit}' not found.")
            return None
        else:
            print(f"Error: {e}")
            return None

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")

