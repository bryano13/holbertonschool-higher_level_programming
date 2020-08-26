#!/usr/bin/python3
"""Script that takes a letter and sends a 
POST request to a URL with the letter as a 
parameter"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        data = {"q": argv[1]}
    else:
        data = {"q": ""}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data)
    dict1 = response.json()
    if type(dict1) == dict:
        if dict1:
            print("[{}] {}".format(dict1["id"], dict1["name"]))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
