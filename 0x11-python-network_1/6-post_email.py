#!/usr/bin/python3
"""
a Python script that takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    r = requests.post(url, data={'email': argv[2]})
    print(r.text)
