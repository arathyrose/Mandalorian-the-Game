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

class person(obj):
    def __init__(self, x, y, h, w, style,ty):
        super().__init__(x,y,h,w,style,ty)

    
    
