'''
hero
====

This class denotes the Mandalorian who is controlled by the player.
He is small; he is cute.
He looks different based on the powerups he is on

It inherits from person class.

Additional Data Members
-----------------------

NONE

Additional/Re-written Member Functions
--------------------------------------

- Constructor

Initialises the person with the characteristics of a hero
Style:
[▄
||

- print_direct

Checks how high the hero is currently (that is, which all power-ups are active atm)
Then prints the hero directly onto the screen

- collision_manager

Manages the collision of the hero with the beams, coins, magnet and powerups on the board

- magnet_attraction

Manages the attraction of the hero towards the magnet if the magnet is on the screen

'''


from person import person
import global_stuff
from powerUp import powerup


class hero(person):

    def __init__(self):
        '''
        Initialises the person with the characteristics of a hero
        '''
        super().__init__(global_stuff.screen_height - 5,
                         0, 2, 2, [['▄', '['], ['|', '|']], 'Hero')

    def print_direct(self):
        '''
        Checks how high the hero is currently (that is, which all power-ups are active atm)
        Then prints the hero directly onto the screen
        '''
        if(global_stuff.shielded == 1):
            self.change_type('ShieldedHero')
            super().print_direct()
        elif(global_stuff.speeded == 1):
            self.change_type('SpeededHero')
            super().print_direct()
        else:
            self.change_type('Hero')
            super().print_direct()

    def collision_manager(self, board):
        '''
        Manages the collision of the hero with the beams, coins, magnet and powerups on the board
        '''
        for i in range(self._h):
            for j in range(self._w):
                what_is_destroyed = board.destroy_object(self._x+i, self._y+j)
                if(global_stuff.debug == 1):
                    if(what_is_destroyed != 'No collision'):
                        print(what_is_destroyed)
                # coins
                if(what_is_destroyed == 'Coin'):
                    global_stuff.coins_collected += 1
                    global_stuff.score += 10
                # beams
                elif what_is_destroyed in ['Hbeam', 'Vbeam', 'Dbeam1', 'Dbeam2']:
                    if(global_stuff.shielded == 1):
                        global_stuff.shielded = 0
                        global_stuff.shielded_power_up_counter = -1
                    else:
                        global_stuff.lives_remaining -= 1
                # power-ups
                elif what_is_destroyed in ['ExtraLife', 'ShieldPU', 'SpeedBoost', 'Snek']:
                    p = powerup(self._x+i, self._y+j, what_is_destroyed)
                    p.collect(board)
                # magnets
                elif(what_is_destroyed == 'Magnet'):
                    global_stuff.hit_by_a_magnet = 1

    def magnet_attraction(self, board):
        '''
        Manages the attraction of the hero towards the magnet if the magnet is on the screen
        '''
        is_magnet_on_screen = board.is_magnet_on_screen()
        if(is_magnet_on_screen != 'NOT ON SCREEN'):
            if(global_stuff.debug == 1):
                print('Moving the guy close to ', is_magnet_on_screen)
            if(is_magnet_on_screen+4-1 > self._y):
                self.move('right')
            elif(is_magnet_on_screen+4-1 < self._y):
                self.move('left')
            self.collision_manager(board)
