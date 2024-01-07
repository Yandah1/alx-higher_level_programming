#!/usr/bin/python3
'''
This script uses the GitHub API to display the user's ID by
authenticating with a personal access token.
'''

import sys
import requests

if __name__ == "__main__":

    username = sys.argv[1]
    access_token = sys.argv[2]

    url = f"https://api.github.com/user"
    headers = {
            'Authorization': 'access_token {}'.format(access_token)
            }
    response = requests.get(url, headers=headers)
    print(response.json().get('id', 'None'))
