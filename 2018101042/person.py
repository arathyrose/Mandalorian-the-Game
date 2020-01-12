'''
The person class: 

This is a base class for the charcters in the game  

He has the following attributes:

- x position on the screen
- y position on the screen
- height
- width
- character for filling him/her/it

and the following functions:

- initialize itself
- render itself to the screen
- kill itself
'''
from gameboard import gameboard
from obj import obj
import global_stuff


class person(obj):
    def __init__(self, x, y, h, w, style, ty):
        super().__init__(x, y, h, w, style, ty)

    def move(self, direction):
        if(direction == "w" or direction == "up"):
            if(self.x > 2):
                self.x -= 1
        elif (direction == "s" or direction == "down"):
            if(self.x < global_stuff.screen_height-5):
                self.x += 1
        elif(direction == "a" or direction == "left"):
            if(self.y > 0):
                self.y -= 1
        elif(direction == "d" or direction == "right"):
            if(self.y < global_stuff.screen_length-2):
                self.y += 1
        # print(self.x,self.y)
