#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def rot13(text):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    abc = alpha*2+alpha.upper()*2
    new = ''
    for i in text:
        if i in abc:
            new += abc[abc.find(i)+13]
        else:
            new += i
    return new

def passwd(text):
    abc = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    nums = []
    for i in range(0, len(text), 2):
        n = 0
        if text[i] in abc:
            n += abc[text[i]]*16
        else:
            n += int(text[i])*16
        if text[i+1] in abc:
            n += abc[text[i+1]]
        else:
            n += int(text[i+1])
        nums.append(n)
    return nums

def main():
    from sys import argv
    rot = ' '.join(argv[1:])
    new = rot13(rot)
    print(new)

if __name__ == '__main__':
    main()
