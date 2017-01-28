#!usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Anagram Problem

Dependencies:
collections for Counter comparison
'''

from collections import Counter
import argparse

def detect_anagrams(orig, testcases):
    '''Determine if a set of solutions are anagrams to a given string'''
    build = []
    for testcase in testcases:
        if Counter(orig.lower()) == Counter(testcase.lower()) \
        and orig.lower() != testcase.lower():
            build.append(testcase)
    return build

def main():
    '''Main wrapper'''
    parser = argparse.ArgumentParser()
    parser.add_argument('word', help='original word to test against')
    parser.add_argument('wlist', help='space separated string of words to test')
    args = parser.parse_args()
    for anagram in detect_anagrams(args.word, args.wlist.split()):
        print(anagram)

if __name__ == '__main__':
    main()
