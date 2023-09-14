import pygame

from .fonts import TEXT_FONT_ARIAL_15

#bouton pour gerer la fin de tour du joueur
class Button_Switch_Phase:
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
                        if game.phase == "Mouvement":
                            game.set_phase("Attaque")
                        elif game.phase == "Attaque":
                            game.set_phase("Défense")
                        else:
                            game.set_phase("Mouvement")
                            game.set_turn(1)
                            
                        self.pressed = False


        
