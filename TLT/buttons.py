import pygame
import os

from .fonts import TEXT_FONT_ARIAL_15

#bouton pour gerer la fin de tour du joueur
class Button_Phase_Switcher:
    def __init__(self, text, width, height, pos):
        self.pressed = False

        #top rectangle
        self.top_rect = pygame.Rect(pos,(width, height))
        self.top_color = "#475F77"

        #text
        self.text_surf = TEXT_FONT_ARIAL_15.render(text,True, "#FFFFFF")
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    # permet de changer  le text du bouton
    def set_text_surf(self,text):
        self.text_surf = TEXT_FONT_ARIAL_15.render(text,True, "#FFFFFF")
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
    
    # permet de dessiner le bouton
    def draw(self,game,text):
        self.set_text_surf(text)
        pygame.draw.rect(game.win, self.top_color, self.top_rect)
        game.win.blit(self.text_surf, self.text_rect)
        self.check_click(game)

    #permet de finir le tour du joueur en fonction des différentes phases du jeu
    def check_click(self, game):
        if game.characters_turn == game.player.name:
            mouse_pos = pygame.mouse.get_pos()
            if self.top_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.pressed = True
                else:
                    if self.pressed == True:
                        #CREER UNE FONCTION POU GERER LE CHANGEMENT DE PHASE
                        game.phase_manager()
                        self.pressed = False

class Button_Spell:
    def __init__(self, directory_spell_img, spell_attributes, x, y, width, height):
        self.pressed = False
        self.selected = False
        self.spell_image = pygame.image.load(os.path.join(directory_spell_img, spell_attributes["image"]+".png")).convert_alpha()

        self.spell_attributes = spell_attributes

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.top_rect = pygame.Rect((x,y),(width, height))

        

    
    def draw(self,win,player):
        win.blit(self.spell_image,(self.x ,self.y ,self.width ,self.height))
        self.check_click(player)

    #permet de modifier le board en fonctions des sort cliquer
    def check_click(self, player):
        if player.index_entities == player.name:
            mouse_pos = pygame.mouse.get_pos()
            if self.top_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    player.false_pressed_spells_Buttons()
                    self.pressed = True
                else:
                    if self.pressed == True:
                        #CREER UNE FONCTION POUR AFFICHER LA ZONE DU SORT
                        self.selected = True
                        print(self.spell_attributes["name"])
                        self.pressed = False



        
