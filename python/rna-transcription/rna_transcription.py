#!usr/bin/env python3
# -*- coding: utf-8 -*-
'''RNA Transcription Problem'''

import argparse

def to_rna(inp):
    '''RNA complement of given DNA strand'''
    rnatrans = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }
    outp = ''
    for nuc in inp:
        outp += rnatrans.get(nuc, '')
    if len(outp) != len(inp):
        outp = ''
    return outp

def main():
    '''Main wrapper'''
    parser = argparse.ArgumentParser()
    parser.add_argument('dna', help='DNA string to convert', action='store')
    args = parser.parse_args()
    print(to_rna(args.dna))

if __name__ == '__main__':
    try:
        main()
    finally:
        print("\nProgram terminated\n")
