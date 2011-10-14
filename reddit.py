#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import loads
from urllib.request import urlopen
from urllib.error import HTTPError
from http.client import HTTPResponse
from random import choice

USER_URL = 'http://www.reddit.com/user/{}/about.json'
SUB_URL = 'http://www.reddit.com/r/{}.json'

def user(name):
    url = USER_URL.format(name)
    try:
        response = urlopen(url).readall().decode('utf-8')
    except HTTPError:
        return (name, None, None)
    data = loads(response)['data']
    return (name, data['link_karma'], data['comment_karma'])

def rand_item(sub='all'):
    result = []
    url = SUB_URL.format(sub)
    try:
        data = loads(urlopen(url).read().decode('utf-8'))
    except ValueError:
        return None
    posts = data['data']['children']
    post_data = choice(posts)['data']
    title = post_data['title']
    if sub == 'all':
        sub = post_data['subreddit']
        title = '[{}] {}'.format(sub, title)
    link = post_data['url']
    return title, link
                


#def main():


if __name__ == '__main__':
	main()

