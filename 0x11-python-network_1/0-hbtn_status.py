#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
and displays the body response in a specific format.
"""

import urllib.request

def fetch_url(url):
    """Fetches the given URL using urllib."""
    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')
        print("Body response:")
        print("    - type:", type(content))
        print("    - content:", content)
        print("    - utf8 content:", utf8_content)

if __name__ == "__main__":
    fetch_url("https://alx-intranet.hbtn.io/status")

