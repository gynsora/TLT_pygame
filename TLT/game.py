import pygame
import os

from .constants import *
from .board import Board
from .player import Player
from .enemy import Enemy


class Game:
    def __init__(self, win, bg_image, player_attributes, enemy_attributes):
        self.win = win
        #gestion des tours 
        self.characters = [player_attributes["name"],enemy_attributes["name"],"Animation"]
        self.current_turn = 0
        self.turn = 0
        self.characters_turn = self.characters[0]
        self.phase = "Mouvement"
        self.player_attributes = player_attributes
        self.enemy_attributes = enemy_attributes
        self.new()
        directory_bg = os.path.join(os.path.dirname(__file__), "../Assets/img/background")
        self.bg = pygame.image.load(os.path.join(directory_bg, bg_image)).convert_alpha()

    def new(self):
        #création du board du jeu
        self.board = Board()

        #création du groupe de sprite présent dans le jeu pour l'affichage du joueur et de l'ennemi dans le board
        self.all_sprites = pygame.sprite.Group() 

        # on passe en paramètre tout les attributs du joueur
        self.player = Player(self.player_attributes)
        # on passe en paramètre tout les attributs de l'ennemi
        self.enemy = Enemy(self.enemy_attributes)

        self.all_sprites.add(self.player)
        self.all_sprites.add(self.enemy)

    #modifie la phase du jeu
    def set_phase(self,phase):
       self.phase = phase

    #modifie le tour de jeu (switch entre joueur, ennemi et "animation")
    def set_turn(self,turn):
       self.turn = turn
       self.characters_turn = self.characters[turn]

    
    def update(self):
        #création du background du jeu
        self.win.blit(self.bg,(-300,-200))#(0,0) quand bonne image trouvé

        #dessin du board du jeu
        self.board.draw(self.win)

        #dessin du joueur et de l'ennemi dans le board
        self.all_sprites.draw(self.win)

        #dessin de la heathbar du joueur et de l'ennemi
        self.player.update(self.win)
        self.enemy.update(self.win)

        #texte indiquant les différentes phase de jeu pour le joueur 
        self.player.turn_indicator(self.win, self.characters_turn , self.phase)

        #bouton pour finir un tour de jeu
        self.player.update_end_turn_button(self)

        pygame.display.update()