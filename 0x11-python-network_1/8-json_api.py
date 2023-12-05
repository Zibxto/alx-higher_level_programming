#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        data = {"q": ""}
    else:
        data = {"q": argv[1]}
    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    result = r.json()
    if result == {}:
        print("No result")
    else:
        try:
            print("[{}] {}".format(result.get('id'), result.get('name')))
        except KeyError:
            print("Not a valid JSON")
