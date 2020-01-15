'''
Denotes power-ups: shield ░ and speed-boost A and extra life + and snake $

It inherits from OBSTACLES and has the following attributes

- value
- how it looks like
- type of the power-up
- time for which it stays active

and the following functions

- be collected
- display it
'''


from obstacle import obstacle
import global_stuff
import time


class powerup(obstacle):
    def __init__(self, xpos, ypos, ty):
        self._type = ty
        if(ty == 'sh' or ty == 'shield' or ty == 'ShieldPU'):
            super().__init__(xpos, ypos, 1, 1, '░', 'ShieldPU')
        elif(ty == 'sp'or ty == 'speed' or ty == 'SpeedBoost'):
            super().__init__(xpos, ypos, 1, 1, 'A', 'SpeedBoost')
        elif(ty == 'xl' or ty == 'extra life' or ty == 'ExtraLife'):
            super().__init__(xpos, ypos, 1, 1, '+', 'ExtraLife')
        elif(ty == 's'or ty == 'snek' or ty == 'Snek'):
            super().__init__(xpos, ypos, 1, 1, '$', 'Snek')

    def collect(self, board):
        if(global_stuff.debug == 1):
            print(self._type)
        super().destroy_self(board)
        if(self._type == 'sh' or self._type == 'shield'or self._type == 'ShieldPU'):
            global_stuff.shielded_power_up_counter = 0
            global_stuff.shielded = 1
        elif(self._type == 'sp'or self._type == 'speed'or self._type == 'SpeedBoost'):
            global_stuff.speeded_power_up_counter = 0
            if(global_stuff.speeded==0):
                global_stuff.move_left_time /= 2
                global_stuff.speeded = 1
        elif(self._type == 'xl' or self._type == 'extra life'or self._type == 'ExtraLife'):
            global_stuff.lives_remaining += 1
            if(global_stuff.lives_remaining >= global_stuff.total_life):
                global_stuff.lives_remaining = global_stuff.total_life
        elif(self._type == 's'or self._type == 'snek'or self._type == 'Snek'):
            global_stuff.snek = 1
