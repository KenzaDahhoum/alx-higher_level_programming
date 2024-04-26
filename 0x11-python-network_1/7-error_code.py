#!/usr/bin/python3
"""
This script takes a URL as input, sends a request to the URL, displays the body
of the response, and handles HTTP status codes.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)

