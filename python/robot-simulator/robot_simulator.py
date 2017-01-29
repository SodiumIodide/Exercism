#!usr/bin/env python3
# -*- coding: utf-8 -*-
'''Robot Simulator Problem'''

# Global variables (arbitrary values)
NORTH = 'n'
SOUTH = 's'
EAST = 'e'
WEST = 'w'

class Robot():
    '''Robot class: turns and moves on taxicab geometry'''
    def __init__(self, bearing=NORTH, xcoord=0, ycoord=0):
        self.coordinates = (xcoord, ycoord)
        self.bearing = bearing

    def turn_right(self):
        '''Turn robot right'''
        directions = {
            NORTH: EAST,
            EAST: SOUTH,
            SOUTH: WEST,
            WEST: NORTH,
        }
        self.bearing = directions.get(self.bearing)

    def turn_left(self):
        '''Turn robot left'''
        directions = {
            NORTH: WEST,
            WEST: SOUTH,
            SOUTH: EAST,
            EAST: NORTH,
        }
        self.bearing = directions.get(self.bearing)

    def advance(self):
        '''Move robot forward one unit'''
        xbearings = {
            EAST: 1,
            WEST: -1,
        }
        ybearings = {
            NORTH: 1,
            SOUTH: -1,
        }
        if self.bearing in xbearings:
            self.coordinates = (self.coordinates[0] +
                                xbearings.get(self.bearing), self.coordinates[1])
        else:
            self.coordinates = (self.coordinates[0], self.coordinates[1] +
                                ybearings.get(self.bearing))

    def simulate(self, program):
        '''Run orders based on program using first-class functions'''
        orders = {
            'A': self.advance,
            'L': self.turn_left,
            'R': self.turn_right,
        }
        for term in program:
            orders.get(term)()
