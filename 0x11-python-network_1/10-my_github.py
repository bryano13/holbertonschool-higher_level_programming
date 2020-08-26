#!/usr/bin/python3
"""Script that authenticates a github user and
returns the id of the user"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) >= 3:
        user = argv[1]
        password = argv[2]
    else:
        user = ""
        password = ""

    response = requests.get(
        'https://api.github.com/user', auth=(user, password))
    try:
        my_dict = response.json()
        print(my_dict["id"])
    except Exception:
        print("None")
