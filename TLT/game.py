import pygame
from .board import Board
from .player import Player
from .enemy import Enemy
class Game:
    def __init__(self, win,player_attributes, enemy_attributes):
        self.win = win
        self.player_attributes = player_attributes
        self.enemy_attributes = enemy_attributes
        self.new()
    
    def new(self):
        #création du board du jeu
        self.board = Board()

        #création du groupe de sprite présent dans le jeu
        self.all_sprites = pygame.sprite.Group() 

        #on passe en parametre tout les attributs du joueur
        self.player = Player(self.player_attributes)
        self.enemy = Enemy(self.enemy_attributes)

        #self.all_sprites.add(self.player)
        
        
    def update(self):
        self.board.draw(self.win)
        #self.all_sprites.draw(self.win)
        self.player.update(self.win)
        self.enemy.update(self.win)
        pygame.display.update()