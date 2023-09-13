import pygame
from .board import Board
from .player import Player
from .enemy import Enemy
import os

class Game:
    def __init__(self, win, bg_image, player_attributes, enemy_attributes):
        self.win = win
        self.player_attributes = player_attributes
        self.enemy_attributes = enemy_attributes
        self.new()
        directory_bg = os.path.join(os.path.dirname(__file__), "..\Assets\img\\background")
        print(directory_bg)
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
        
        pygame.display.update()