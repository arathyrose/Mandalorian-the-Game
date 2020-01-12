'''
Bullet is an obstacle with the ability to move only foreward (why would anyone shoot backward, duh)
Attributes: Nothing? since it is inherited
Functions: Move front, check if it collides with anything and destroy what it collides with and destroy self too
'''

from obstacle import obstacle 
class bullet(obstacle):
    def __init__(self):
        super().__init__(0, 0, 2, 1, ['≡','>'], 'Bullet')
        self.exist=0
        self.deployable=0
    
    def move_left(self,board):
        if(self.exist==1):
            self.destroy_self(board)
            self.y+=1
            self.write_self_on_board(board)
    
    def deploy(self,hero):
        if(self.deployable==0):
            return 0
        else:
            self.x=hero.x
            self.y=hero.y
            self.exist=1
            self.deployable=0
            return 1
    
    def display(self,board):
        if(self.exist==1):
            self.write_self_on_board(board)
    