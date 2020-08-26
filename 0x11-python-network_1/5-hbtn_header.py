#!/usr/bin/python3
"""This module displays the value of X-Request-Id from the
header of an URL"""

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    print(response.headers["X-Request-Id"])
