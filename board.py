import os
from time import sleep

class Board():
    def __init__(self):
        print("Board created")
        self.board = []
        with open('initial_board.txt') as f:
            l = f.read()
            l = l.split('\n')
            self.board = l
        for line in self.board:
            print(line,end='\r')
            sleep(1)
        self.updated = False

    # Function to replace blocks of the grid
    def update(self, bot_x, bot_y, top_x, top_y, new_arr):
        self.updated = True
        self.board[top_x:bot_x][top_y:bot_y] = new_arr
    
    def draw(self):
        if self.updated:
            print("Draw board function")