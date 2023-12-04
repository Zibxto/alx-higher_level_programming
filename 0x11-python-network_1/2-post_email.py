#!/usr/bin/python3
"""
a Python script that takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    email = {"email": argv[2]}
    url = argv[1]

    email = urllib.parse.urlencode(email)
    email = email.encode('ascii')
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as res:
        body = res.read()
    print(body.decode('utf-8'))
