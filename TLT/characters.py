import pygame
from .constants import *
from .utilities import *
from .moveCalc import MoveCalc

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
        #liste des cases ou le  joueur pourrais agir (attaque , deplacement, mouvement)
        self.squares = []
        #creation la portee des spell (s'affiche lorsque l'on selectionne un sort)
        #self.range = []
        #creation la zone des spell (s'affiche lorsque l'on selectionne un sort et que l'on "hover" une case de la "range")
        #self.zone = []

    # Affiche la porteé du sort
    def show_posibilities_move(self, win):
        self.calculation = MoveCalc(self.x, self.y, SQUARE_SIZE, SQUARE_SIZE)#on calcule la portée de mouvement du joueur
        for top, left in self.calculation.calc_movement(self):#ici la portée de mouvement se calcule avec une cible, cette cible (target) est le joueur lui même
            print(top , left)
            rect_x,rect_y = calc_pos_in_board(top, left)
            self.square = MoveCalc(rect_x, rect_y,SQUARE_SIZE,SQUARE_SIZE)
            self.all_sprites = pygame.sprite.Group()
            self.all_sprites.add(self.square)
            self.all_sprites.draw(win)
            self.squares.append(self.square)
