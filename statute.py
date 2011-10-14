# -*- coding: utf-8 -*-

import urllib.request
import http.client
import re
from html.parser import HTMLParser

class StatuteParser(HTMLParser):
    def handle_data(self, data):
        print(data)


def getStatute(query):
    act, section = query.split(' ')
    num, yr = act.split('/')
    key = 'zza' + num + 'y' + yr + 's' + section[1:]
    url_num = num
    while len(num) < 4:
        num = '0' + num
    section = section[1:]
    while len(section) < 4:
        section = '0' + section
    url = 'http://www.irishstatutebook.ie/'+yr+'/en/act/pub/'+num+'/sec'+section+'.html'
    connect = urllib.request.urlopen(url)
    out = connect.read().decode('utf-8')
    start = out.find(key)
    end = out.find('<!--End Content-->')
    new_out = out[start:end]
    parsed_out = re.findall(r'>(.+?)<', new_out)
    for i in parsed_out:
        if i[0] == '<' and i[-1] == '>':
            parsed_out[parsed_out.index(i)] = 'TAG'
    while 'TAG' in parsed_out:
        parsed_out.remove('TAG')
    while '[GA]' in parsed_out:
        parsed_out.remove('[GA]')
    print(''.join(parsed_out))
