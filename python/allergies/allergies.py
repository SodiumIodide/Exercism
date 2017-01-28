#!usr/bin/env python3
# -*- coding: utf-8 -*-
'''Allergies Problem'''

class Allergies:
    '''
    Allergies class:
    Given a score, determine what user is allergic to
    '''
    comp = {
        1: 'eggs',
        2: 'peanuts',
        3: 'shellfish',
        4: 'strawberries',
        5: 'tomatoes',
        6: 'chocolate',
        7: 'pollen',
        8: 'cats',
    }

    def __init__(self, score):
        self.score = score
        self.lst = self.build_allergies()

    def build_allergies(self):
        '''Return a list of things user is allergic to'''
        build = []
        pos = 0
        for digit in reversed(bin(self.score)[2:]):
            pos += 1
            if digit == '1':
                build.append(self.comp.get(pos))
        return [x for x in build if x is not None]

    def is_allergic_to(self, allergen):
        '''Return true if user is allergic to given allergen'''
        return allergen in self.lst

def main():
    '''Main wrapper'''
    try:
        allergynum = int(input("Enter the allergy score number\n>>> "))
    except ValueError:
        exit("Must be a number")
    for allergen in Allergies(allergynum).lst:
        print(allergen)

if __name__ == '__main__':
    main()
