""" 
Denotes moneyy!

It inherits from OBSTACLES and has the following attributes

- value
- how it looks like

and the following functions

- be collected
- display it 
"""

from obstacle import obstacle
import global_stuff


class coins(obstacle):
    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos, 1, 1, ['0'], 'Coin')

    def collect(self, board):
        super().destroy_self(board)
        global_stuff.coins_collected += 1
