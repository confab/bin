#!/usr/bin/env python3

from collections import deque
from operator import add, mod, mul, sub, truediv

class InputError(Exception): pass

operators = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': truediv,
            '**': pow,
            '^': pow,
            '%': mod
            }

def eval_rpn(*seq):
    seq = deque(seq)
    stack = []
    while len(seq) > 0:
        token = seq.popleft()
        try:
            token = float(token)
            stack.append(token)
        except ValueError:
            try:
                b, a = float(stack.pop()), float(stack.pop())
            except IndexError:
                raise InputError('Insufficient operands.')
            try:
                oper = operators[token]
            except KeyError:
                raise InputError('Invalid operator: {}'.format(token))
            stack.append(oper(a, b))

    if len(stack) > 1:
        raise InputError('Too many operands.')
    try:
        return stack[0]
    except IndexError:
        raise InputError('No sequence given.')

if __name__ == '__main__':
    from sys import argv
    print(eval_rpn(' '.join(argv[1:])))
