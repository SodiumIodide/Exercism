#!usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Atbash Cipher Problem

Dependencies:
string for lowercase alphabet list
'''

from string import ascii_lowercase

# Global dictionary for encoding and decoding
# Letters:
ENCODING = dict(zip(ascii_lowercase, reversed(ascii_lowercase)))
# Numbers:
for num in range(10):
    ENCODING[str(num)] = str(num)

def encode(inpstr):
    '''Method for encoding a string by the Atbash Cipher'''
    initial = inpstr.lower().replace(' ', '')
    build = ''
    for character in initial:
        build += ENCODING.get(character, '')
    result = ' '.join([build[i:i+5] for i in range(0, len(build), 5)])
    return result

def decode(inpstr):
    '''Method for decoding a string by the Atbash Cipher'''
    initial = inpstr.lower().replace(' ', '')
    build = ''
    for character in initial:
        build += ENCODING.get(character, '')
    return build
