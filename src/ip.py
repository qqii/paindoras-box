#!/usr/bin/python3

from requests import get

def ip():
    return get('https://api.ipify.org').text 

if __name__ == "__main__":
    print("IP: {}".format(ip()))
