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
        self.characters = [enemy_attributes["name"],player_attributes["name"],"Animation"]
        self.current_turn = 1
        self.turn = 1
        self.characters_turn = self.characters[1]
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

        #on indique au joueur et à l'ennemi que le premier à jouer est le joueur
        self.player.index_entities =  self.characters[1]
        self.enemy.index_entities =  self.characters[1]

        #on indique au joueur et à l'ennemi que la première phase est le mouvement 
        self.player.game_phase =  "Mouvement"
        self.enemy.game_phase =  "Mouvement"

        # print(self.player.nextPath)

    #modifie la phase du jeu
    def set_phase(self,phase):
        self.phase = phase
        #on indique au joueur et à l'ennemi que la phase de jeu
        self.player.game_phase = phase
        self.enemy.game_phase = phase

    #modifie le tour de jeu (switch entre joueur, ennemi et "animation")
    def set_turn(self,turn):
        self.turn = turn
        self.characters_turn = self.characters[turn]
        #on indique au joueur et à l'ennemi que le premier à jouer est le joueur
        self.player.index_entities =  self.characters[turn]
        self.enemy.index_entities =  self.characters[turn]

    #permet de changer la phase du jeu, cette fonction est appeler par le joueur, l'ennemi et le jeu sous certaines conditions
    def phase_manager(self):
        if self.phase == "Mouvement":
            self.set_phase("Attaque")
        elif self.phase == "Attaque":
            self.set_phase("Défense")
        else:
            self.set_phase("Mouvement")
            self.set_turn(0)

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

        #bouton pour finir un tour de jeu du joueur
        self.player.update_end_turn_button(self)

        #dessin des zones d'actions du joueur (si il a selectionné un sort)
        self.player.action_posibility(self.win)

        #determine les actions possible du joueur (déplacement ,attaque ,défense)
        self.player.actions(self)

        pygame.display.update()