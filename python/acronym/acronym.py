#!usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Acronym Problem

Dependencies:
re for regex substitution to prune the strings
'''

import re
import argparse

def abbreviate(inpstr):
    '''Convert a phrase to an acronym'''
    buffer = re.sub(r'[^\w]', r' ', inpstr)
    words = re.sub(r'([A-Z])[a-z]', r' \1', buffer).split()
    acronym = ''
    for word in words:
        acronym += word[0].upper()
    return acronym

def main():
    '''Main wrapper'''
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='A string to turn into an acronym')
    args = parser.parse_args()
    print(abbreviate(args.input))

if __name__ == '__main__':
    main()
