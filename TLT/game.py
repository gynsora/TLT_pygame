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
        self.current_turn = 0
        self.turn = self.current_turn
        self.characters_turn = self.characters[self.turn]
        self.phase = "Début"
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
        self.player.index_entities =  self.characters[self.turn]
        self.enemy.index_entities =  self.characters[self.turn]

        #on indique au joueur et à l'ennemi que la première phase est le mouvement 
        self.player.game_phase =  self.phase
        self.enemy.game_phase =  self.phase

        #on indique les position respective du joueur pour l'ennemi et de l'ennemi pour le joueur
        self.player.enemy_pos = [self.enemy.x, self.enemy.y]
        self.enemy.player_pos = [self.player.x, self.player.y]
        # print(self.player.nextPath)
        #activation de phase_manager
        self.phase_manager()

    #permet au 2 characters d'avoir la position de son adversaire
    def set_pos(self):
        self.player.enemy_pos = [self.enemy.x, self.enemy.y]
        self.enemy.player_pos = [self.player.x, self.player.y]

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
        if self.phase == "Début":
            print("début")
            if self.characters_turn == self.player.name:
                print("le joueur prépare son mouvement")
                self.set_phase("Mouvement")
            if self.characters_turn == self.enemy.name:
                print("l'ennemi prépare son mouvement")
                self.set_phase("Mouvement")
                    
        elif self.phase == "Mouvement":
            print(self.characters_turn , "Mouvement")
            if self.characters_turn == self.player.name:
                self.player.spell_selected = ""
                self.player.squares = []
            if self.characters_turn == self.enemy.name:
                self.enemy.spell_selected = ""
            self.set_pos()
            self.set_phase("Attaque")
                       
        elif self.phase == "Attaque":
            print(self.characters_turn , "Attaque")
            self.turn = (self.current_turn +1) % 2
            self.set_turn(self.turn)

            if self.characters_turn == self.player.name:
                #remettre self.player.squares à vide apres avoir selectionnée (la zone d'attaque du joueur)
                self.player.squares = []
            if self.characters_turn == self.enemy.name:
                print("defense enemy")
                
            # self.player.spell_selected = ""
            self.set_pos()
            self.set_phase("Défense")

        elif self.phase == "Défense":
            print("Défense ?")
            #spell choisi par le player
            # print(self.player.spell_selected, "a")
            #zone du spell choisi par le player
            # print(self.player.spell_zone)

            self.player.squares = []
            print("sort du joueur : \n", self.player.spell_selected )
            print("zone sort joueur ", self.player.spell_zone)
            print("sort de l'ennemi : \n", self.enemy.spell_selected )
            print("zone sort de l'ennemi  ", self.enemy.spell_zone)
            self.set_turn(2)
            self.set_phase("Combat")

        else:#phase combat
            self.set_pos()
            print("Fin combat ?")
            #spell choisi par le player
            print(self.player.spell_selected)
            #zone du spell choisi par le player
            print(self.player.spell_zone)

            self.player.squares = []
            self.set_turn(0)
            print(self.characters_turn)
            self.set_phase("Mouvement")
            

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
        #determine les actions possible de l'ennemi (déplacement ,attaque ,défense)
        self.enemy.actions(self)

        pygame.display.update()