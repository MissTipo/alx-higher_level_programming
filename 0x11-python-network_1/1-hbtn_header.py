#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id
"""
from urllib.request import urlopen, Request
from sys import argv

if __name__ == "__main__":
    req = Request(argv[1])
    with urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
