import pygame
import os

from .characters import *
from .constants import *
from .spritesheet import SpriteSheet
from .health import Health


class Enemy(Characters):
    def __init__(self, enemy_attributes):
        super().__init__(enemy_attributes)
        #le nom de la personne qui peut joueur
        self.index_entities  = ""
        self.game_phase = ""

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

        #creation du chemin pour l'animation du déplacement joueur
        self.mouvPath = [[self.x,self.y]]
        #permet de déterminé la position de l'ennemi
        self.player_pos = []

        # creation d'une liste de coordonée pour la zone de chaque attaque / défense enregistrera la zone selectionné au clique
        self.spell_zone = []
        #contient le nom de la zone de spell et la portee de la zone de spell (A SUPPRIMER SI BESOIN)
        self.spell_register = []
        #création d'une liste contenant l'attaque ou la défense selectionné
        self.spell_selected = []
    
    def actions(self, game):
        if self.index_entities == self.name  and self.game_phase == "Mouvement":
            self.move_choice(game)
        elif self.index_entities == self.name  and self.game_phase == "Attaque":
            self.attack_choice(game) 
        elif self.index_entities == self.name  and self.game_phase == "Défense":
            self.defense_choice(game)

    #permet à l'ennemi de choisir un chemin pour se déplacer en fonction de la position de sont adversaire (player) A AMELIORER
    def move_choice(self,game ):
        print(self.name, "choisi son déplacement" )
        #améliorer la fonction pour choisir différent sort en fonction des situations
        self.spell_selected = self.spells_List[0]
        #si l'ennemi et le joueur sont des ordonées différentes
        if self.y != self.player_pos[1]:
            self.x = self.player_pos[0]
            
            rect_x, rect_y = calc_pos_in_board(self.x, self.y)     
            self.rect.x = rect_x
            self.rect.y = rect_y
            print(self.name, "se déplace en ", self.x, self.y)
            self.health.lost_health(self.spell_selected["cost"]["hp"])
            self.health.lost_endurance(self.spell_selected["cost"]["endurance"])
        else:
            print(self.name, " décide de ne pas bouger")    
        
        game.phase_manager()

    #permet à l'ennemi de choisir une attaque en fonction de la position de sont adversaire (player) A AMELIORER
    def attack_choice(self,game ):
        print(self.name, "choisi son Attaque" )
        #améliorer la fonction pour choisir différent sort en fonction des situations
        self.spell_selected = self.spells_List[1]
        self.spell_register = self.spells_List[1]
        #si l'ennemi et le joueur sont des ordonées différentes
        if self.y != self.player_pos[1]:
            for i in range(1,ROWS):
                self.spell_zone.append(tuple((self.x, i)))
        else:
            for i in range(ROWS):
                if i != self.x:
                    self.spell_zone.append(tuple((i, self.y)))    
        # # print(self.spell_zone)  
        
        game.phase_manager()

    #permet à l'ennemi de choisir une défense en fonction de la position de sont adversaire (player) A AMELIORER
    def defense_choice(self,game):
        print(self.name, "choisi sa Défense" )
        #améliorer la fonction pour choisir différent sort en fonction des situations
        self.spell_selected = self.spells_List[2]
        self.spell_register = self.spells_List[2]
        #si l'ennemi et le joueur sont des ordonées différentes
       
        self.spell_zone.append(tuple((self.x, self.y)))    
        # print(self.spell_zone)
        game.phase_manager()

         
    def update(self,win): # permet d'afficher la health bar
        self.health.draw(win)