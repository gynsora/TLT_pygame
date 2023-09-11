import pygame
from .board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def _init(self):
        #creation du board du jeu
        self.board = Board()
        
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()