import pygame
from .constants import *
from .utilities import *

class Characters(pygame.sprite.Sprite):#stat des personnages du jeu
    
    def __init__(self, characters_attributes):
        pygame.sprite.Sprite.__init__(self)
        #attribut des personnages du jeu
        self.name = characters_attributes["name"]
        self.x = characters_attributes["x"]
        self.y = characters_attributes["y"]
        self.atk = characters_attributes["atk"]
        self.width = characters_attributes["width"]
        self.height = characters_attributes["height"]
        
        self.hp = characters_attributes["hp"]
        self.endurance = characters_attributes["endurance"]

        self.critical = characters_attributes["critical"]
        self.defCritical = characters_attributes["defCritical"]

        self.spells_List = characters_attributes["spells_List"]
        
        self.color = characters_attributes["color"]
        
        
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        x_pos,y_pos = calc_pos_in_board(self.x,self.y)
        self.rect.x = x_pos
        self.rect.y = y_pos
      

    
