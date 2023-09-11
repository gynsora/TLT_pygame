import pygame
from TLT.constants import WIDTH , HEIGHT
from TLT.game import Game

FPS = 60
#WIN = window, ici on crée la taille de la fenetre du jeu
WINDOW_SIZE = pygame.display.set_mode((WIDTH,HEIGHT))
#The Lost Time = nom du jeu
pygame.display.set_caption("The Lost Time")

def main():
    run = True
    #ici on crée un timer pour définir la vitesse de rafraichissement du jeu (FPS)
    clock = pygame.time.Clock()
    #on initialise le jeu
    game = Game(WINDOW_SIZE)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # arret de la boucle du jeu, quand on quitte le jeu (on appuie sur la croix pour fermer le jeu)
                run = False
            
           
        #dessin de l'échequier
        game.update()
    
    pygame.quit()

main()