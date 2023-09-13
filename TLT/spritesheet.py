import pygame

class SpriteSheet():
    def __init__(self,image):
        self.sheet = image

    #spritesheet_selection format 4 * 4 16 au total 
    #recupération d'une frame du spritesheet    
    def get_image_spritesheet(self, frame, width, height, color):
        x = frame %  4
        y = frame // 4
        image = pygame.Surface((width, height))
        image.blit(self.sheet,(0,0),( width*x, height*y, width, height ))
        image.set_colorkey(color)
        
        return image
