#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)
"""

from urllib.request import urlopen, Request
from sys import argv
from urllib.parse import urlencode

if __name__ == "__main__":
    values = urlencode({'email':argv[2]}).encode('ascii')
    req = Request(argv[1], values)
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
