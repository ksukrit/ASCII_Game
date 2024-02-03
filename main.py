import numpy as np
import colorama
from time import sleep

from board import Board
from player import Player
from game import Game
# The main game file

if __name__ == "__main__":
    print("Starting game loop")
    board = Board()
    player = Player()
    game = Game()
    while(True):
        board.draw()

        sleep(1)