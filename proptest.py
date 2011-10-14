#!/usr/bin/env python

class test:
    def __init__(self):
        self._name = 'testing'

    @property
    def name(self):
        print('getting name!')
        return self._name
    
    @name.setter
    def name(self, name):
        print('setting name!')
        self._name = name
    
    @name.deleter
    def name(self):
        print('Nooooo...')
        del self._name
