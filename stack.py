#!/usr/bin/env python3

class stack:
    def __init__(self, iterable=[]):
        self.stack = list(iterable)
    
    def push(self, new):
        self.stack.append(new)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]

    @property
    def stack(self):
        print('getting')
        #return self.stack
    
    @stack.setter
    def stack(self, new):
        print('setting')
        #self.stack = new
    
