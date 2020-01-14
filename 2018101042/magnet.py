'''
This is a magnet
This is cute
Be like a magnet
Attract the hero
Make him trust you
Betray his trust
Let him die
'''

from obstacle import obstacle


class magnet(obstacle):
    def __init__(self, xpos, ypos):
        k = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', '\x1b[1;31m█', '\x1b[1;31m█', '\x1b[1;31m█', '\x1b[1;31m█',
                 '\x1b[1;31m█', '\x1b[1;31m█', '\x1b[1;31m█', ' '],
             [' ', '\x1b[1;31m█', '\x1b[1;30m░', '\x1b[1;30m░', '\x1b[1;30m░',
                 '\x1b[1;30m░', '\x1b[1;30m░', '\x1b[1;31m█', ' '],
             [' ', '\x1b[1;31m█', '\x1b[1;30m░', '\x1b[1;30m░', '\x1b[1;30m░',
                 '\x1b[1;30m░', '\x1b[1;30m░', '\x1b[1;31m█', ' '],
             [' ', '\x1b[1;37m█', '\x1b[1;30m░', '\x1b[1;30m░', '\x1b[1;30m░',
                 '\x1b[1;30m░', '\x1b[1;30m░', '\x1b[1;37m█', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        super().__init__(xpos, ypos, 6, 9, k, 'Magnet')
