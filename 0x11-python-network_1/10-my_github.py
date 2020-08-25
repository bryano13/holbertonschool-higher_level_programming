#!/usr/bin/python3
"""This modules defines a task"""

import requests
from sys import argv

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    try:
        req = requests.get('https://api.github.com/user', auth=(
            argv[1], argv[2])).json()
        print(req.get('id'))
    except:
        print("None")
