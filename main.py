import pygame
from TLT.constants import WIDTH , HEIGHT
from Data.playerData import PLAYER_LIST
from Data.enemyData import ENEMY_LIST
from TLT.game import Game

FPS = 60
#WINDOW_SIZE = window, ici on crée la taille de la fenetre du jeu
WINDOW_SIZE = pygame.display.set_mode((WIDTH,HEIGHT))
#The Lost Time = nom du jeu
pygame.display.set_caption("The Lost Time")

def main():
    run = True
    #ici on crée un timer pour définir la vitesse de rafraichissement du jeu (FPS)
    clock = pygame.time.Clock()
    #on initialise le jeu
    game = Game(WINDOW_SIZE, PLAYER_LIST["Gynsora"], ENEMY_LIST["Dragoon"])

    while run:
        #Frame du jeu
        clock.tick(FPS)

        for event in pygame.event.get():
            # arret de la boucle du jeu, quand on quitte le jeu (on appuie sur la croix pour fermer le jeu)
            if event.type == pygame.QUIT:  
                run = False
            
           
        #update du jeu
        game.update()
    
    pygame.quit()

main()