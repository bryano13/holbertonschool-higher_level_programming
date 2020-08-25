#!/usr/bin/python3
"""This module fetches the info on the header of a URL"""

import urllib.request
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.info()
        print(header.get("X-Request-Id"))
