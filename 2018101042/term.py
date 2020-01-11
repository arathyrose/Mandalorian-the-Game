import subprocess as sp


def clrscr():
    '''
    function to clear the terminal screen
    '''
    sp.call('clear', shell=True)


def next_play():
    ''' 
    function to reposition the pointer
    '''
    print("\033[0;0H", end="")
