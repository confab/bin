#!/usr/bin/env python3

from json import loads
from urllib.request import urlopen
from random import choice

url = 'http://www.reddit.com/r/circlejerk.json'

def get_quote():
    data = loads(urlopen(url).read().decode())
    posts = data['data']['children']
    titles = [p['data']['title'] for p in posts]
    return choice(titles)

if __name__ == '__main__':
    print(get_quote())
