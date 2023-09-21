import pygame
import os
from .characters import *
from .constants import *
from .spritesheet import SpriteSheet
from .health import Health
from .fonts import TEXT_FONT_ARIAL_25
from .buttons import Button_Phase_Switcher, Button_Spell
from .utilities import *

class Player(Characters):
    def __init__(self, players_attributes):
        super().__init__(players_attributes)
        # self.index = 0
        # permet d'identifier si le joueur est entrain de joueur ou non. CELA permet d'activé ou non le clique des boutons spell
        self.index_entities = ""
        self.game_phase = ""

        # self.test_portee = [[0,1],[0,2]]

        #chemin vers le spritesheet du joueur et chargement de l'image spritesheet
        directory_spritesheet_img = os.path.join(os.path.dirname(__file__), "../Assets/img/spritesheet")
        spritesheet_image = pygame.image.load(os.path.join(directory_spritesheet_img, self.name+".png")).convert_alpha()

        #création d'une classe spritesheet (pour sélectionner la frame du joueur)
        self.spritesheet = SpriteSheet(spritesheet_image)
        #selection de l'image du joueur sur le board (les frames du joueur)
        self.image = self.spritesheet.get_image_spritesheet( 4, self.width, self.height, BLACK)

        #chargement du portrait du joueur
        directory_portrait_img = os.path.join(os.path.dirname(__file__), "../Assets/img/portrait")
        portrait_image = pygame.image.load(os.path.join(directory_portrait_img, self.name+".png")).convert_alpha()
        #Création de la health bar du joueur
        self.health = Health(0,0, portrait_image, self.name, self.hp, self.endurance, BLUE, DARK_BLUE)

        #chargement des boutons "spell" du joueur
        directory_spells_img = os.path.join(os.path.dirname(__file__), "../Assets/img/spells")
        #Création des boutons "spell" du joueur
        self.spells_Buttons = []
        for i, spell_attributes in enumerate(self.spells_List):
            self.spells_Buttons.append(Button_Spell(directory_spells_img, spell_attributes, 20+(i * 70), 700, 64, 64))

        #création du bouton de "fin de tour"
        self.end_turn_button = Button_Phase_Switcher("", 65, 65, (700,600))

        #création du chemin pour l'animation du déplacement joueur, animation du prochain chemin
        #par défaut, le chemin est identique à la case de départ du joueur
        #création d'une liste de de coordonnée pour le chemin de déplacement joueur 
        self.nextPath = [[self.x,self.y]]
        # creation d'une liste de coordonée pour la zone de chaque attaque / défense enregistrera la zone selectionné au clique
        self.spell_zone = []
        #contient le nom de la zone de spell et la portee de la zone de spell
        self.spell_zone_selected = []
        #création d'une liste contenant l'attaque ou la défense selectionné
        self.spell_selected = []
        
        #permet de déterminé la position de l'ennemi
        self.enemy_pos = []
        #liste des cases ou le joueur pourrais agir (attaque , deplacement, mouvement)
        self.squares = []
               
    #fonction permettant d'afficher  les différentes phase du jeu
    def turn_indicator(self, win, turn, phase):
        turn_indicator = ""

        if turn == self.name :
            turn_indicator = "A votre tour"
            text_color = BLUE
        elif turn == "Animation" :
            turn_indicator = "Animation"
            text_color = YELLOW
        else:
            turn_indicator = "Tour adverse"
            text_color = RED

        pygame.draw.rect(win, (40,43,43), (CHESSBOARD_X , CHESSBOARD_Y + CHESSBOARD_SIZE + 10 , CHESSBOARD_SIZE, 40) )
        text_turn_indication = TEXT_FONT_ARIAL_25.render(turn_indicator+" - "+phase , 1, text_color)
        win.blit(text_turn_indication, (CHESSBOARD_X+5 , CHESSBOARD_Y + CHESSBOARD_SIZE + 10))

    #met à jour le bouton de "fin de tour"
    def update_end_turn_button(self,game):
        if game.characters_turn == self.name:
            text = "Fin de \ntour"
        elif game.characters_turn == "Animation" :
            text = "Animation"
        else:
            text = "Tour \nadverse"

        self.end_turn_button.draw(game,text)

    #remet a faux tout les boutons de sort appuyer ou non
    def false_pressed_spells_Buttons(self):
        for spell in self.spells_Buttons:
            spell.pressed  = False
            spell.selected = False
        
        print('all unpressed all unselected')

        # for i, spell in enumerate(self.spells_Buttons):
        #     spell.pressed = False
        #     spell.selected = False
        #     print("effacement numero :"+str(i))

    #permet de determine quelle sort à été choisi par le player
    def switch_spell_selected(self):
        for spell in self.spells_Buttons:
            if spell.selected and self.game_phase == spell.spell_attributes["type"]:
                self.spell_selected = spell.spell_attributes

                self.spell_zone_selected = spell.spell_attributes
                # print(self.spell_selected["name"])
                break
    
    #permet d'afficher la zone et la portée d'un spell (la zone "d'action" du joueur)
    def action_posibility(self, screen): 
        #si un sort a été selectionné par le joueur pendant son tour de jeu alors
        if self.spell_selected and self.index_entities == self.name :
            if self.game_phase == "Mouvement":
                # print(self.spell_selected["name"])
                self.show_posibilities_move(screen , self.spell_selected["range"])
            elif self.game_phase == "Attaque" or self.game_phase == "Défense":
                # # self.squares = [0]
                # self.squares.clear()
                # print(self.squares)
                self.show_posibilities_attack_defense(screen , self.spell_selected["range"], self.spell_selected["rangeForm"])

    #décrit les actions faite lorsque le joueur à selectionné une case d'un sort activer
    def actions(self,game):
        mouse_pos = pygame.mouse.get_pos()
        for squa in self.squares:
            rect_x, rect_y = calc_pos_in_board(squa["x"],squa["y"])     
            top_rect = pygame.Rect((rect_x, rect_y),(SQUARE_SIZE, SQUARE_SIZE))
            if top_rect.collidepoint(mouse_pos) :
                ## ici gerer laffichage de la zone d'un spell
                # spell_zone = self.spell_selected["zone"]
                zone_of_spell = form_of_spell_range(squa["x"], squa["y"] ,self.spell_zone_selected["zone"] , self.spell_zone_selected["zoneForm"],self.x,self.y)
                
                for left, top in zone_of_spell:
                    if coordinates_in_board(left, top) :
                        rect_zone_x, rect_zone_y = calc_pos_in_board(left, top)    
                        range_tile = pygame.Surface((SQUARE_SIZE,SQUARE_SIZE), pygame.SRCALPHA)   
                        range_tile.fill(PURPLE)              
                        game.win.blit(range_tile, (rect_zone_x ,rect_zone_y ,SQUARE_SIZE ,SQUARE_SIZE))

                if pygame.mouse.get_pressed()[0]:   
                    squa["pressed"] = True
                else:
                    if squa["pressed"] == True:    
                        if self.index_entities == self.name  and self.game_phase == "Mouvement":
                            print("le joueur se déplace vers ", squa["x"] , squa["y"] )
                            #changer les 4 prochaine ligne pour une fonction qui animera le personnage
                            self.rect.x = rect_x
                            self.rect.y = rect_y
                            self.x = squa["x"]
                            self.y = squa["y"]
                            self.health.lost_health(self.spell_selected["cost"]["hp"])
                            self.health.lost_endurance(self.spell_selected["cost"]["endurance"])
                            game.phase_manager()
                            break
                        if self.index_entities == self.name  and self.game_phase == "Attaque":
                            print("Le joueur attaque avec ",self.spell_selected["name"])
                            print("zone du sort d'attaque: ",zone_of_spell)
                            self.spell_zone = zone_of_spell
                            game.phase_manager()
                            break
                        if self.index_entities == self.name  and self.game_phase == "Défense":
                            print("Le joueur défend avec ",self.spell_selected["name"])
                            print("zone du sort de défense: ",zone_of_spell)
                            self.spell_zone = zone_of_spell
                            game.phase_manager()
                            break
                            
                            
    
    # Affiche la porteé du sort de moouvement
    def show_posibilities_move(self, win, range_of_spell):
        for left, top in diamond_form(self.x,self.y,range_of_spell):
            if coordinates_in_board(left, top) and (self.enemy_pos[0] != left or self.enemy_pos[1] != top):
                if self.x  != left or self.y  != top:
                    range_tile = pygame.Surface((SQUARE_SIZE,SQUARE_SIZE), pygame.SRCALPHA)   
                    range_tile.fill(LIGHT_YELLOW)      
                    x, y = calc_pos_in_board(left ,top)   
                    self.squares.append({"x": left,"y" :top, "pressed" :False})         
                    win.blit(range_tile, (x ,y ,SQUARE_SIZE ,SQUARE_SIZE))
    
    # Affiche la portée d'un sort d'attack ou de défense
    def show_posibilities_attack_defense(self, win, range_of_spell,form_of_range):
        range_of_spell = form_of_spell_range(self.x, self.y , range_of_spell, form_of_range)
        for left, top in range_of_spell:
            if coordinates_in_board(left, top) :
                if form_of_range == "Target": #on dessine un tile "jaune" sur nous si le sort nous cible (soin sur soi meme)
                    range_tile = pygame.Surface((SQUARE_SIZE,SQUARE_SIZE), pygame.SRCALPHA)   
                    range_tile.fill(LIGHT_YELLOW)      
                    x, y = calc_pos_in_board(left ,top)   
                    self.squares.append({"x": left,"y" :top, "pressed" :False})         
                    win.blit(range_tile, (x ,y ,SQUARE_SIZE ,SQUARE_SIZE))
                else:
                    if self.x  != left or self.y  != top : # on vérifie si la case est différente de la notre (le sort ne doit pas nous cibler)
                        range_tile = pygame.Surface((SQUARE_SIZE,SQUARE_SIZE), pygame.SRCALPHA)   
                        range_tile.fill(LIGHT_YELLOW)      
                        x, y = calc_pos_in_board(left ,top)   
                        self.squares.append({"x": left,"y" :top, "pressed" :False})         
                        win.blit(range_tile, (x ,y ,SQUARE_SIZE ,SQUARE_SIZE))
    
        
    
    def update(self,win): 
        # permet d'afficher la health bar
        self.health.draw(win)
        for spell in self.spells_Buttons:
            spell.draw(win,self)

        
        
        
       