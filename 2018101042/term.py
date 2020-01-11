import subprocess as sp


def clrscr():
    '''
    function to clear the terminal screen
    '''
    sp.call('clear', shell=True)