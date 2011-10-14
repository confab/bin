#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def gen_bf(text):
    bf = []
    
    for c in text:
        pos = ord(c)
        bf.append('> {0} .'.format('+'*pos))
    
    return bf



def main():
	from sys import argv
	print(gen_bf(argv[1]))

if __name__ == '__main__':
	main()

