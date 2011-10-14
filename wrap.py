#!/usr/bin/env python3

def word_wrap(text, width=80):
    """Wrap a single line of text, returning a string with newlines
    inserted as appropriate.
    No line is more than 'width' characters long, and newlines in the
    middle of words are avoided if possible.
    Line are stripped of trailing and leading whitespace.
    Words longer than 'width' are character-wrapped."""
    if width >= len(text):
        return text
    buff = []
    while True:
        found_space = False
        for i in range(width, 0, -1):
            if text[i].isspace():
                buff.append(text[:i])
                text = text[i:].strip()
                found_space = True
                break
        if not found_space:
            buff.append(text[:width])
            text = text[width:].strip()
        if len(text) <= width:
            buff.append(text)
            return '\n'.join(buff)
