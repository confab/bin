#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Playing around with Markov chains"""

from random import random, choice

class StateError(Exception):
    pass

class ProbabilityError(Exception):
    pass

class ChainTermination(Exception):
    pass


class Markov:
    """A base Markov chain class."""
    
    def set_prob(self, now, nxt, prob=0):
        if (now not in self.states) or (nxt not in self.states):
            raise StateError("State does not exist")
        if (type(prob) not in (float, int)) or (prob > 100):
            raise ProbabilityError("Invalid entry for probability")
        if prob > 1:
            prob /= 100
        if prob + sum(self.states[now].values()) > 1:
            raise ProbabilityError("Total probability would be greater than one")
        
        self.states[now][nxt] = prob
    
    def add_state(self, state):
        if state not in self.states:
            self.states[state] = {}
    
    def set_state(self, state=None):
        if state is None:
            state = choice(list(self.states.keys()))
        elif state not in self.states:
            raise StateError("State does not exist")
        self.cur_state = state
            
    def get_state(self):
        return self.cur_state
        
    def step(self, choose=False):
        if choose:
            try:
                self.cur_state = choice(list(self.states[self.cur_state].keys()))
            except IndexError:
                raise ChainTermination("Chain terminated") #after %s" % self.cur_state)
        else:
            nxts = []
            probs = []
            for state in self.states[self.cur_state]:
                nxts.append(state)
                probs.append(self.states[self.cur_state][state])
            rand = random()
            run_tot = 0
            for i in range(len(probs)):
                run_tot += probs[i]
                if rand < run_tot:
                    self.cur_state = nxts[i]
                    return
            raise ChainTermination("Chain terminated") #after %s" % self.cur_state)
            
    def __init__(self):
        self.states = {}
        self.cur_state = None


class Economy(Markov):
    """An implementation of the example given on the Wikipedia page."""
    
    def __init__(self):
        self.states = {'recession': {}, 'bull market': {}, 'bear market': {}}
        self.states['recession'] = {
            'recession':    0.5,
            'bull market':  0.25,
            'bear market':  0.5
            }
        self.states['bull market'] = {
            'recession':    0.025,
            'bull market':  0.9,
            'bear market':  0.075
            }
        self.states['bear market'] = {
            'recession':    0.05,
            'bull market':  0.15,
            'bear market':  0.8
            }
        self.set_state()
