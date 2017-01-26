#!usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Word Count Problem

Dependencies:
collections for defaultdict counting method
re for regex substitution on non-alphanumerics
'''

from collections import defaultdict
import re
import argparse

def word_count(inp):
    '''Word counting function'''
    nuinp = re.sub(r'[\W_]', r' ', inp)
    words = nuinp.split()
    dictcount = defaultdict(int)
    for word in words:
        dictcount[word.lower()] += 1
    return dictcount

def main():
    '''Main wrapper'''
    parser = argparse.ArgumentParser()
    parser.add_argument('string', help='String to count words in', action='store')
    args = parser.parse_args()
    count = word_count(args.string)
    print(dict(count))

if __name__ == '__main__':
    try:
        main()
    finally:
        print("\nProgram terminated\n")
