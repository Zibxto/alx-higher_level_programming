#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        body = res.read()
    print("Body response:")
    print("     - type:", type(body))
    print("     - content:", body)
    print("     - utf8 content:", body.decode('utf-8'))
