#!usr/bin/env python3
# -*- coding: utf-8 -*-

'''Say Problem'''

import argparse
import os

# Global definitions for phrase substitution
LOW_ORDER = dict(zip(range(20),
                     ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
                      'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
                      'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                      'nineteen']))
HIGH_ORDER = dict(zip(range(2, 10),
                      ['twenty', 'thirty', 'forty', 'fifty', 'sixty',
                       'seventy', 'eighty', 'ninety']))
MAGNITUDE = ['', 'thousand', 'million', 'billion']

def say(number):
    '''Return a string representation of a number'''
    if number < 0 or number >= 1e12:
        raise AttributeError('Invalid number option: Must be 0-999,999,999,999')
    if number == 0:
        return 'zero'
    build = []
    cnt = 0
    while number > 0:
        number, remainder = divmod(number, 1000)
        position = remainder > 0
        addand = (cnt == 0 and 0 < remainder < 100 and number > 0)
        build = ['and'] * addand + __hundreds(remainder) + [MAGNITUDE[cnt]] \
                * position + build
        cnt += 1
    return ' '.join((' '.join(build)).split()).strip()

def __hundreds(number):
    '''Return a string representaiton of a hundreds-order number'''
    hundreds, tens = divmod(number, 100)
    return [LOW_ORDER[hundreds], "hundred" * (hundreds > 0),
            "and" * (hundreds * tens > 0), __tens(tens)]

def __tens(number):
    '''Return a string representation of a tens-order number'''
    if number < 20:
        return LOW_ORDER[number]
    tens, ones = divmod(number, 10)
    return '{}{}{}'.format(HIGH_ORDER[tens], '-' * (ones > 0), LOW_ORDER[ones])

def main():
    '''Main wrapper'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', dest='say', action='store_true', default=False,
                        help='tag this to feed to \'say\' utility')
    parser.add_argument('number', type=int, help='number for conversion')
    args = parser.parse_args()
    try:
        response = say(args.number)
    except (ValueError, AttributeError):
        exit("Number must be in range 0-999,999,999,999")
    if args.say:
        print(response)
        os.system('say "{}"'.format(response))
    else:
        print(response)

if __name__ == '__main__':
    main()
