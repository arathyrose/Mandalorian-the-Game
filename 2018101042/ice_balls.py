''' 
Bullet of the dragon
You shall not pass
'''
'''
Ice ball is an obstacle with the ability to move only backward (the BOSS is backward in both thinking and working)
Attributes: Nothing? since it is inherited
Functions: Move back (since it is a backward community), check if it collides with the hero and decrease two of its lives
'''




import global_stuff
from obstacle import obstacle
class ball(obstacle):
    def __init__(self):
        super().__init__(0, 0, 1, 5, [['·', '░', '▒', '▓', '█']], 'Ice Ball')
        self.exist = 0

    def check_collision(self, board, h):
        if(self.exist == 1):
            try:
                for i in range(0, 5):
                    board.destroy_object(self.x, self.y+i)
                    # whatever it touches (there would be only coins :/) no need to give coins or shiz
                    # what if it touches the hero
                    for k in range(h.h):
                        if(self.exist == 0):
                            break
                        for l in range(h.w):
                            if((h.x+k, h.y-l) == (self.x, self.y+i)):
                                global_stuff.lives_remaining -= 2
                                self.exist = 0
                                break
                                # you lose two lives if that ball touches you; so be warned!!
            except:
                pass

    def move_left(self, board, h):
        if(self.exist == 1):
            try:
                self.check_collision(board, h)
                """ for i in range(-5,5):
                    board.destroy_object(self.x, self.y+i)
                    # whatever it touches (there would be only coins :/) no need to give coins or shiz
                    # what if it touches the hero
                    for k in range(h.h):
                        if(self.exist==0):
                            break
                        for l in range(h.w):
                            if((h.x+k,h.y-l)==(self.x, self.y+i)):
                                global_stuff.lives_remaining-=2
                                self.exist=0
                                break """
                # you lose two lives if that ball touches you; so be warned!!
            except:
                pass
            self.y -= 5
            if(self.y <= 0):
                self.exist = 0
            self.check_collision(board, h)

    def deploy(self, x, y):
        self.x = x
        self.y = y
        self.exist = 1
        self.print_direct()
