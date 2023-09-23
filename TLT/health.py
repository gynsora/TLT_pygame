import pygame
from .fonts import TEXT_FONT_MONO_20

class Health():
    def __init__(self, x, y, character_image, character_name, max_health, endurance,color,dark_color):
        #position basique de Health
        self.x = x
        self.y = y
        
        #attribut de Health
        self.portrait = character_image
        self.name = character_name
        self.color = color
        self.dark_color = dark_color
        
        self.endurance = endurance
        self.max_endurance = endurance+2

        self.current_health = max_health
        self.max_health = max_health
        self.health_bar_length = 100
        self.health_ratio = self.max_health / self.health_bar_length
    
    #permet réduire les pdv
    def lost_health(self,amount):
        if self.current_health > 0:
            self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0

    #permet d'augmenter les pdv  
    def gain_health(self,amount):
        if self.current_health < self.max_health:
            self.current_health += amount
        if self.current_health >= self.max_health:
            self.current_health = self.max_health
    
    #permet de remettre l'endurance à son état de base (fin de tour)
    def set_endurance(self,amount):
        self.endurance = amount
        
    #permet réduire l'endurance
    def lost_endurance(self,amount):
        if self.endurance > 0:
            self.endurance -= amount
        if self.endurance <= 0:
            self.endurance = 0

    #permet d'augmenter l'endurance
    def gain_endurance(self,amount):
        if self.endurance < self.max_health:
            self.endurance += amount
        if self.endurance >= self.max_endurance:
            self.endurance = self.max_endurance


    def draw(self,win):
        win.blit(self.portrait,(self.x ,self.y,self.health_bar_length,137))
        pygame.draw.rect(win, self.dark_color, (self.x, self.y+71, self.health_bar_length,15) )
        pygame.draw.rect(win, self.color, (self.x, self.y+71, self.current_health/self.health_ratio, 15) )
        diamond = pygame.image.load("Assets/img/utilities/diamond.png").convert_alpha()
        diamond = pygame.transform.scale(diamond, (32*1.1,32*1.1))
        win.blit(diamond, (self.x + 34, self.y+95 , 32*1.1 ,32*1.1))
        endurance = TEXT_FONT_MONO_20.render(str(self.endurance), 1, (0,0,0))
        win.blit(endurance, (self.x + 43, self.y+98))