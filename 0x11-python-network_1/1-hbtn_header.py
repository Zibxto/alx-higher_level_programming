#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL
Displays the value of the X-Request-Id variable
found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        header = res.info()
    print(header["X-Request-Id"])
