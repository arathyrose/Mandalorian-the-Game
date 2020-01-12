'''
A base class that denotes all the possible obstacles in the game

It has the following attributes

- length
- width
- x position
- y position
- shape

and the following functions:

- Display it
'''
from obj import obj


class obstacle(obj):
    def __init__(self, xpos, ypos, length, width, shape, style):
        super().__init__(xpos, ypos, length, width, shape, style)
