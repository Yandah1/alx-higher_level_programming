#!/usr/bin/python3
'''
This script retrieves the value of the X-Request-Id variable
from the header of the response.
'''


if __name__ == "__main__":

    import sys
    import urllib.request

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        X_Request_Id = response.getheader('X-Request-Id')
        print(X_Request_Id)
