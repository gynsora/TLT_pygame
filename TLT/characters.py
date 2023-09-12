import pygame
from .constants import *
from .utilities import *

class Characters(pygame.sprite.Sprite):#stat des personnages du jeu
    
    def __init__(self, characters_attributes):
        pygame.sprite.Sprite.__init__(self)
        #attribut des perosnnages du jeu
        self.atk = characters_attributes["name"]
        self.x = characters_attributes["x"]
        self.y = characters_attributes["y"]
        self.hp = characters_attributes["hp"]
        self.width = characters_attributes["width"]
        self.height = characters_attributes["height"]
        self.name = characters_attributes["name"]
        self.color = characters_attributes["color"]
        self.atk = characters_attributes["atk"]
        self.hp = characters_attributes["hp"]
        self.endurance = characters_attributes["endurance"]
        self.critical = characters_attributes["critical"]
        self.defCritical = characters_attributes["defCritical"]
        #image du personnage (a changer)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        x_pos,y_pos = calc_pos_in_board(self.x,self.y)
        self.rect.x = x_pos
        self.rect.y = y_pos
        #self.squares = []

        #self.image = pygame.Surface((width,height), pygame.SRCALPHA)
        #self.image.fill((255,255,255,32))

        #faire des rectangles semi transparent pour la portée des sorts
        #s = pygame.Surface((1000,750), pygame.SRCALPHA)   # per-pixel alpha
        #s.fill((255,255,255,128))                         # notice the alpha value in the color
        #windowSurface.blit(s, (0,0))