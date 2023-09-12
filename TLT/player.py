import pygame
from .characters import *
from .constants import *

class Player(Characters):
    def __init__(self, players_attributes):
        super().__init__(players_attributes)
        self.index = 0
       
    def update(self,win): # permet de mettre à jour l'animation du joueur
        pygame.draw.rect(win, self.color, (self.rect.x ,self.rect.y,SQUARE_SIZE,SQUARE_SIZE))
       
       