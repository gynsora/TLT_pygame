import pygame
from .constants import *
from .utilities import *

class MoveCalc(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height): 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width,height))
        #ajouter un argument pour recupérer le type de sort choisi (deplacement, sort)
        #modifier image.fill pour avoir des tile transparente 
        self.image.fill(LIGHT_YELLOW)
        self.image.set_alpha(128) #opacity
        self.rect = self.image.get_rect()
        # x_pos, y_pos = calc_pos_in_board(x,y)
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def calc_movement(self,target, range_of_spell): # faire cette fonction avec une matrice a 2 dimension pour utilisé les coordonées plus facilement
        coordinates = []
        # les 2 boucle serve à crée une zone en forme de losange
        nb_tilese = range_of_spell-1
        for z in range(target.y+1, target.y+range_of_spell+1):
            for k in range(target.x-nb_tilese, target.x+nb_tilese+1):
                self.x = k
                self.y = z
                if self.x  != target.x or self.y  != target.y:
                    coordinates.append(tuple((self.x, self.y)))
            nb_tilese -= 1

        nb_tiles = range_of_spell
        for y in range(target.y ,target.y-range_of_spell-1, -1 ):
            for x in range(target.x-nb_tiles, target.x+nb_tiles+1):
                self.x = x
                self.y = y
                if self.x  != target.x or self.y  != target.y:
                    coordinates.append(tuple((self.x, self.y)))
            nb_tiles -= 1
        
       
        return coordinates
    
    def cal_attack_options(self, target):
        coordinates = []

        # for k, v in POSSIBLE_ATTACKS.items():

        #     if k == "top":
        #         self.rect.x = target.rect.x
        #         self.rect.y = target.rect.y

        #         for _ in range(0, len(v)):
        #             self.rect.y -= TILESIZE
        #             coordinates.append(tuple((self.rect.x, self.rect.y)))

        #     elif k == "top-right":
        #         self.rect.x = target.rect.x
        #         self.rect.y = target.rect.y
        #         for _ in range(0, len(v)):

        #             self.rect.x += TILESIZE
        #             self.rect.y -= TILESIZE
        #             coordinates.append(tuple((self.rect.x, self.rect.y)))

        #     elif k == "top-left":
        #         self.rect.x = target.rect.x
        #         self.rect.y = target.rect.y
        #         for _ in range(0, len(v)):
        #             self.rect.x -= TILESIZE
        #             self.rect.y -= TILESIZE
        #             coordinates.append(tuple((self.rect.x, self.rect.y)))

        #     elif k == "right":
        #         self.rect.x = target.rect.x
        #         self.rect.y = target.rect.y
        #         for _ in range(0, len(v)):
        #             self.rect.x -= TILESIZE
        #             coordinates.append(tuple((self.rect.x, self.rect.y)))

        #     elif k == "left":
        #         self.rect.x = target.rect.x
        #         self.rect.y = target.rect.y
        #         for _ in range(0, len(v)):
        #             self.rect.x += TILESIZE
        #             coordinates.append(tuple((self.rect.x, self.rect.y)))

        #     elif k == "bottom-right":
        #         self.rect.x = target.rect.x
        #         self.rect.y = target.rect.y
        #         for _ in range(0, len(v)):
        #             self.rect.y += TILESIZE
        #             self.rect.x += TILESIZE
        #             coordinates.append(tuple((self.rect.x, self.rect.y)))

        #     elif k == "bottom-left":
        #         self.rect.x = target.rect.x
        #         self.rect.y = target.rect.y
        #         for _ in range(0, len(v)):
        #             self.rect.y += TILESIZE
        #             self.rect.x -= TILESIZE
        #             coordinates.append(tuple((self.rect.x, self.rect.y)))

        #     elif k == "bottom":
        #         self.rect.x = target.rect.x
        #         self.rect.y = target.rect.y
        #         for _ in range(0, len(v)):
        #             self.rect.y += TILESIZE
        #             coordinates.append(tuple((self.rect.x, self.rect.y)))

        return coordinates
    
    def diamond_form(self,target,range_of_spell):
        pass

    def cross_form(self):
        pass

    def front_form(self):
        pass
