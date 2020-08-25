#!/usr/bin/python3
"""This modules defines a task"""

import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))
