import pygame
import os

from .utilities import *
from .constants import *
from .board import Board
from .player import Player
from .enemy import Enemy

class Game:
    def __init__(self, win, bg_image, player_attributes, enemy_attributes,current_time):
        self.win = win

        self.current_time = current_time
        self.beginning_fight_time = 0

        self.defense_fight = True
        self.attack_fight = False

        self.end_fight = False

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
        #activation de phase_manager pour débuter le combat
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
                # self.set_phase("Mouvement")
            if self.characters_turn == self.enemy.name:
                print("l'ennemi prépare son mouvement")
                self.enemy.thinking_time = pygame.time.get_ticks()  
                print(self.enemy.thinking_time)
            self.set_phase("Mouvement")
                    
        elif self.phase == "Mouvement":
            # print(self.characters_turn , "Mouvement")
            if self.characters_turn == self.player.name:
                self.player.spell_selected = ""
                self.player.squares = []
                self.player.spell_zone = []
            if self.characters_turn == self.enemy.name:
                self.enemy.spell_selected = ""
                self.enemy.spell_zone = []
                self.enemy.thinking_time = pygame.time.get_ticks()  
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
                self.enemy.thinking_time = pygame.time.get_ticks()  
                
            # self.player.spell_selected = ""
            self.set_pos()
            self.set_phase("Défense")

        elif self.phase == "Défense":
            print("Combat ?")
            #spell choisi par le player
            # print(self.player.spell_selected, "a")
            #zone du spell choisi par le player
            # print(self.player.spell_zone)

            self.player.squares = []
            print("sort du joueur : \n", self.player.spell_register )
            print("zone sort joueur ", self.player.spell_zone)
            print("sort de l'ennemi : \n", self.enemy.spell_register )
            print("zone sort de l'ennemi  ", self.enemy.spell_zone)
            self.set_turn(2)
            # on détermine le temps du début de la phase de combat
            self.beginning_fight_time = pygame.time.get_ticks()  
            self.set_phase("Combat")
            # on appel la fonction permettant de gérer la phase de combat
            self.fight_manager()
        
    
        else:#phase combat
            self.set_pos()
            print("Fin combat ?")


    #Gére les phase de combat
    def fight_manager(self):
        # print("temps courrant", self.current_time, "temps début combat ",self.beginning_fight_time )   
        if  self.current_time - self.beginning_fight_time  > 200 and self.defense_fight:
            #Déterminer qui défend
            if self.characters[(self.current_turn+1)%2] == self.player.name and self.player.spell_register and self.player.spell_zone:    
                #cree une fonction de défense avec le joueur comme paramètre
                self.fight_defensive_actions(self.player.name)
            elif self.characters[(self.current_turn+1)%2] == self.enemy.name and self.enemy.spell_register and self.enemy.spell_zone:
                #cree une fonction de défense avec l'ennemi comme paramètre
                self.fight_defensive_actions(self.enemy.name)
            else:
                print("pas de défense")
                self.defense_fight = False
                self.attack_fight = True

        elif self.current_time - self.beginning_fight_time  > 700 and self.attack_fight:    
            #Déterminer qui attaque
            if self.characters[(self.current_turn)%2] == self.player.name and self.player.spell_register and self.player.spell_zone: 
                #cree une fonction d'attaque avec le joueur comme paramètre
                self.fight_offensive_actions(self.player.name)
            elif self.characters[(self.current_turn)%2] == self.enemy.name and self.enemy.spell_register and self.enemy.spell_zone:
                #cree une fonction d'attaque avec l'ennemi comme paramètre
                self.fight_offensive_actions(self.enemy.name)
            else:
                print("pas d'attaque")
                self.attack_fight = False
            
           
        elif  self.current_time - self.beginning_fight_time  > 1300:  
            print("delay of fight") 

            self.defense_fight = True
            self.attack_fight = False  
 
            self.player.squares = []
            self.player.spell_register = []
            self.player.spell_selected = []
            # a utiliser quand le joueur récuperer toute son endurance
            # self.player.health.set_endurance(self.player.endurance)

            self.enemy.spell_selected = ""
            self.enemy.spell_register = []
            self.enemy.spell_selected = []
            self.enemy.spell_zone = []
            # a utiliser quand l'ennemi récuperer toute son endurance
            # self.enemy.health.set_endurance(self.player.endurance)

            if self.end_fight:
                self.set_phase("est le vainqueur")
                next_turn = self.current_turn  % 2
                self.set_turn(next_turn)
            else :
                self.current_turn += 1
                next_turn = self.current_turn  % 2
                self.set_turn(next_turn)
                if self.characters_turn == self.enemy.name :
                    self.enemy.thinking_time = pygame.time.get_ticks()  
                self.set_phase("Mouvement")
    
    #détermine les actions  défensive faite pendant la phase de combat SI LA PERSONNE DECIDE DE DEFENDRE
    def fight_defensive_actions(self,defender_name):
        print(defender_name, " défend !!!!!!!!!!!!!!!!!!!!!!!!!!!")
        #Faire les mouvements de défense
        if self.player.name == defender_name:
            # print(self.player.spell_selected)
            # print(self.player.spell_zone)
            #faire les animations de sort défensif
            # if self.player.spell_selected["rangeForm"] == "Target":
            #     pass

            #Payer le prix du sort de défense
            self.player.health.lost_health(self.player.spell_register["cost"]["hp"])
            self.player.health.lost_endurance(self.player.spell_register["cost"]["endurance"])
            #Gain du sort défensif
            self.player.health.gain_health(self.player.spell_register["gain"]["hp"])
            self.player.health.gain_endurance(self.player.spell_register["gain"]["endurance"])

           

        elif self.enemy.name == defender_name:
            # print(self.enemy.spell_selected)
            # print(self.enemy.spell_zone)
            #faire les animations de sort défensif
            # if self.player.spell_selected["rangeForm"] == "Target":
            #     pass

            #Payer le prix du sort de défense
            self.enemy.health.lost_health(self.enemy.spell_register["cost"]["hp"])
            self.enemy.health.lost_endurance(self.enemy.spell_register["cost"]["endurance"])
            #Gain du sort défensif
            self.enemy.health.gain_health(self.enemy.spell_register["gain"]["hp"])
            self.enemy.health.gain_endurance(self.enemy.spell_register["gain"]["endurance"])
        
        #Finir les actions défensive et commencer les actions offensive (durant la phase de combat)
        self.defense_fight = False
        self.attack_fight = True

    #détermine les actions  offensive faite pendant la phase de combat SI LA PERSONNE DECIDE D'ATTAQUER
    def fight_offensive_actions(self, attacker_name):
        print(attacker_name, " Attaque !!!!!!!!!!!!!!!!!!!!!!!!!!!")
        if self.player.name == attacker_name:
            #Faire les mouvement d'attaque
            # 
            # 
            #Changer le board si besoin A CHANGER
            for tile in self.player.spell_zone:
                x , y  = tile
                if coordinates_in_board(x, y):
                    self.board.board[x][y]= element_number(self.player.spell_register["element"])
            #Déterminer si l'attaquant touche son adversaire
            for tile in self.player.spell_zone:
                x, y = tile
                if x == self.enemy.x and y == self.enemy.y:
                    self.enemy.health.lost_health(self.player.spell_register["damage"]+self.player.atk)
                    if self.enemy.health.current_health == 0:
                        self.end_fight = True
                    break
            #Consommer les ressource de l'attaque
            self.player.health.lost_health(self.player.spell_register["cost"]["hp"])
            self.player.health.lost_endurance(self.player.spell_register["cost"]["endurance"])
            #Gain du sort défensif
            self.player.health.gain_health(self.player.spell_register["gain"]["hp"])
            self.player.health.gain_endurance(self.player.spell_register["gain"]["endurance"])
            # 
            

        if self.enemy.name == attacker_name:
            #Faire les mouvement d'attaque
            # 
            # 
            #Changer le board si besoin A CHANGER
            for tile in self.enemy.spell_zone:
                x , y  = tile
                if coordinates_in_board(x, y):
                    self.board.board[x][y]= element_number(self.enemy.spell_register["element"])
            #Déterminer si l'attaquant touche son adversaire
            for tile in self.enemy.spell_zone:
                x, y = tile
                if x == self.player.x and y == self.player.y:
                    self.player.health.lost_health(self.enemy.spell_register["damage"]+self.enemy.atk)
                    if self.player.health.current_health == 0:
                        self.end_fight = True
                    break
            #Consommer les ressource de l'attaque
            self.enemy.health.lost_health(self.enemy.spell_register["cost"]["hp"])
            self.enemy.health.lost_endurance(self.enemy.spell_register["cost"]["endurance"])
            #Gain du sort défensif
            self.enemy.health.gain_health(self.enemy.spell_register["gain"]["hp"])
            self.enemy.health.gain_endurance(self.enemy.spell_register["gain"]["endurance"])
        
        #Finir les actions offensive et finir la phase de combat 
        self.attack_fight = False

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

        if(self.phase == "Combat"):
            self.fight_manager()

        pygame.display.update()