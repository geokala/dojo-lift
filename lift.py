#! /usr/bin/env python
import time
import string

class FloorOhFour(Exception):
    pass

class Lift(object):
    floor_names = [
        'ground floor', 
        'first floor',
        'second floor',
        'third floor',
        'fourth floor'
    ]

    def __init__(self, lift_shaft=0, starting_floor=0):
        self.lift_position = starting_floor
        self.lift_shaft = lift_shaft
        self.intended_floor = None

    def call(self, destination):
        if self.intended_floor is not None:
            # We already have a floor we're trying to reach, sorry!
            return False
        elif 0 <= destination < len(self.floor_names):
            self.intended_floor = destination
            return True
        else:
            raise FloorOhFour('Floor {destination} not found, cannot go there.'.format(destination=destination))

    def act(self):
        if self.intended_floor is not None:
            if self.intended_floor == self.lift_position:
                print('We have arrived!')
                self.intended_floor = None
            elif self.intended_floor < self.lift_position:
                self.lift_position -= 1
            else:
                self.lift_position += 1

def sanitize(user_input):
    return int(''.join([i for i in user_input if i in string.digits]) )

lifts = [
    Lift(starting_floor=2)
]


while True:
    user_input = input(
        'Which floor has a button press? (none for... none):'
    ).strip()

    if user_input and [ i for i in user_input if i in string.digits]:
        user_input = sanitize(user_input)
    else:
         user_input = None
    
    for lift in lifts:
        if user_input:
            lift.call(int(user_input))
        lift.act()
        print(lift.lift_position,lift.intended_floor)