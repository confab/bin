#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from markov import *
from random import choice

class Text(Markov):
    """Pseudo-random text generator."""
    
    def parse(self, text):
        """Parses text and splits it into matching pairs."""
        words = text.split(' ')
        self.matches = {}
        for i in range(len(words)-3):
            two = (words[i], words[i+1])
            if two not in self.matches:
                self.matches[two] = []
            self.matches[two].append(words[i+2])
                
    def digest(self):
        """Takes table of matching words and adds to the pool of states."""
        for w in self.matches:
            self.add_state(w)
            for m in self.matches[w]:
                self.add_state((w[1], m))
                self.set_prob(w, (w[1], m))
    
    def learn(self, text):
        self.parse(text)
        self.digest()
    
    def get_text(self, count=100):
        text = []
        self.cur_state = choice(list(self.states.keys()))
        for i in range(count):
            try:
                text.append(self.cur_state[0])
                self.step(True)
            except ChainTermination:
                self.cur_state = choice(list(self.states.keys()))
        return ' '.join(text)
    
    def __init__(self):
        Markov.__init__(self)

def test():
    t = open('/home/alan/bin/aiw').read()
    x = Text()
    x.learn(t)
    return x.get_text(1000)
    
