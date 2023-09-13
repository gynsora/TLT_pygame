import pygame
import os
from .characters import *
from .constants import *
from .spritesheet import SpriteSheet
from .health import Health

class Enemy(Characters):
    def __init__(self, enemy_attributes):
        super().__init__(enemy_attributes)
        self.index = 0
        #chemin vers le spritesheet de l'ennemi
        directory_spritesheet_img = os.path.join(os.path.dirname(__file__), "../Assets/img/spritesheet")
        #chargement de l'image spritesheet à partie du chemin de la ligne précédante
        spritesheet_image = pygame.image.load(os.path.join(directory_spritesheet_img, self.name+".png")).convert_alpha()
        #création d'une classe spritesheet (pour selectionné la frame de l'ennemi)
        self.spritesheet = SpriteSheet(spritesheet_image)
        #selection de l'image l'ennemi sur le board (les frames l'ennemi)
        self.image = self.spritesheet.get_image_spritesheet( 12 , self.width, self.height,BLACK)

        directory_portrait_img = os.path.join(os.path.dirname(__file__), "../Assets/img/portrait")
        portrait_image = pygame.image.load(os.path.join(directory_portrait_img, self.name+".png")).convert_alpha()
        
        self.health = Health(900,0, portrait_image, self.name , self.hp , self.endurance,RED, DARK_RED)
       
    def update(self,win): # permet d'afficher la health bar
        self.health.draw(win)