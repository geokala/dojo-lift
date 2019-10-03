#! /usr/bin/env python
# Disclaimer: No liability for loss of income or limbs accepted. Or torsos.
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
        self.intended_floors = []

    def call(self, destination):
        if len(self.intended_floors) > 3:
            # We already have a floor we're trying to reach, sorry!
            return False
        elif 0 <= destination < len(self.floor_names):
            self.intended_floors.append(destination)
            return True
        else:
            raise FloorOhFour('Floor {destination} not found, cannot go there.'.format(destination=destination))

    def act(self):
        if len(self.intended_floors) > 0:
            if self.lift_position in self.intended_floors:
                print('We have arrived at the {floor}!'.format(floor=self.floor_names[self.lift_position]))
                self.intended_floors.remove(self.lift_position)
            elif self.intended_floors[0] < self.lift_position:
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
        if user_input is not None:
            lift.call(int(user_input))
        lift.act()
        print(lift.lift_position,lift.intended_floors)
