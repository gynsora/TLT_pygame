import pygame
from .characters import *
from .constants import *

class Enemy(Characters):
    def __init__(self, enemy_attributes):
        super().__init__(enemy_attributes)
        self.index = 0
       
    def update(self,win): # permet de mettre à jour l'animation d'un enemie
        pygame.draw.rect(win, self.color, (self.rect.x ,self.rect.y,SQUARE_SIZE,SQUARE_SIZE))