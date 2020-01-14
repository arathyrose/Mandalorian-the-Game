'''
Bullet is an obstacle with the ability to move only foreward (why would anyone shoot backward, duh)
Attributes: Nothing? since it is inherited
Functions: Move front, check if it collides with anything and destroy what it collides with and destroy self too
'''
import global_stuff
from obstacle import obstacle


class bullet(obstacle):
    def __init__(self):
        super().__init__(0, 0, 1, 2, [['≡', '>']], 'Bullet')
        self.exist = 0
        self.deployable = 0

    def move_right(self, board):
        if(self.exist == 1):
            no_destroy_anything = 0
            try:
                for i in range(-1, 4):
                    what_is_destroyed = board.destroy_object(self.x, self.y+i)
                    if(what_is_destroyed == 'Coin'):
                        global_stuff.score += 5  # 5 for coin collectino by slave
                    elif (what_is_destroyed == 'Hbeam' or what_is_destroyed == 'Vbeam' or what_is_destroyed == 'Dbeam1' or what_is_destroyed == 'Dbeam2'):
                        global_stuff.score += 20  # 20 per beam destroyed
                        self.exist = 0
                    elif(what_is_destroyed == 'Magnet'):
                        self.exist = 0
                        no_destroy_anything = 1
            except:
                pass
            try:
                board.board[self.x][self.y][0] = ' '
                board.board[self.x][self.y][1] = 'Normal'
                if(no_destroy_anything == 0):
                    board.board[self.x][self.y+1][0] = ' '
                    board.board[self.x][self.y+1][1] = 'Normal'
                board.board[self.x][self.y-1][0] = ' '
                board.board[self.x][self.y-1][1] = 'Normal'
                self.y += 2
                if(self.y+1 >= board.columns):
                    self.exist = 0
                elif(self.exist == 1):
                    board.board[self.x][self.y][0] = '≡'
                    board.board[self.x][self.y][1] = 'Bullet'
                    board.board[self.x][self.y+1][0] = '>'
                    board.board[self.x][self.y+1][1] = 'Bullet'
                    if(global_stuff.debug == 1):
                        print("BULLET", self.x, self.y)
            except:
                self.exist = 0
                self.deployable = 0

    def deploy(self, hero):
        if(self.deployable == 0):
            return 0
        elif(self.deployable == 1):
            try:
                self.x = hero.x
                self.y = hero.y+4
                self.exist = 1
                self.deployable = 0
                global_stuff.bullets_left -= 1
                return 1
            except:
                return 0

    def display(self, board):
        if(self.exist == 1):
            self.write_self_on_board(board)
