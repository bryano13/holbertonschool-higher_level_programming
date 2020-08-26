#!/usr/bin/python3
"""Script that sends a request to a URL and
displays the body of the response"""

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    status = response.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(response.text)
