import pygame
import os
from .characters import *
from .constants import *
from .spritesheet import SpriteSheet
from .health import Health
from .fonts import TEXT_FONT_ARIAL_25
from .buttons import Button_Switch_Phase

class Player(Characters):
    def __init__(self, players_attributes):
        super().__init__(players_attributes)
        # self.index = 0

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
        self.health = Health(0,0, portrait_image, self.name , self.hp , self.endurance, BLUE, DARK_BLUE)

        #création du bouton de "fin de tour"
        self.end_turn_button = Button_Switch_Phase("plop", 65, 65, (700,600))



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


    def update(self,win): 
        # permet d'afficher la health bar
        self.health.draw(win)
        
        
       