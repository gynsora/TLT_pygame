import pygame
import os
from .characters import *
from .constants import *
from .spritesheet import SpriteSheet
from .health import Health


class Player(Characters):
    def __init__(self, players_attributes):
        super().__init__(players_attributes)
        # self.index = 0

        #chemin vers le spritesheet du joueur et chargement de l'image spritesheet
        directory_spritesheet_img = os.path.join(os.path.dirname(__file__), "../Assets/img/spritesheet")
        spritesheet_image = pygame.image.load(os.path.join(directory_spritesheet_img, self.name+".png")).convert_alpha()

        #création d'une classe spritesheet (pour sélectionner la frame du joueur)
        self.spritesheet = SpriteSheet(spritesheet_image)
        #selection de l'image du joueur sur le board (les frames du joueur)
        self.image = self.spritesheet.get_image_spritesheet( 4, self.width, self.height, BLACK)

        directory_portrait_img = os.path.join(os.path.dirname(__file__), "../Assets/img/portrait")
        portrait_image = pygame.image.load(os.path.join(directory_portrait_img, self.name+".png")).convert_alpha()
        
        self.health = Health(0,0, portrait_image, self.name , self.hp , self.endurance, BLUE, DARK_BLUE)
       


    def update(self,win): # permet d'afficher la health bar
        self.health.draw(win)
        
       