import pygame
import sys
from TLT.constants import WIDTH , HEIGHT
from Data.playerData import PLAYER_LIST
from Data.enemyData import ENEMY_LIST
from TLT.game import Game


FPS = 60
#WINDOW_SIZE = window, ici on crée la taille de la fenetre du jeu
WINDOW_SIZE = pygame.display.set_mode((WIDTH,HEIGHT))
#The Lost Time = nom du jeu
pygame.display.set_caption("The Lost Time")

# pygame.font.init()

def main():
    run = True
    #ici on crée un timer pour définir la vitesse de rafraichissement du jeu (FPS)
    clock = pygame.time.Clock()

    #on initialise le temps en cours
    current_time = 0
    #on initialise le jeu
    game = Game(WINDOW_SIZE,"terrainPlaine.jpg", PLAYER_LIST["Gynsora"], ENEMY_LIST["Dragoon"],current_time)
    

    while run:
        #Frame du jeu
        clock.tick(FPS)
        #Temps courant du jeu mis a jour pour le jeu
        current_time = pygame.time.get_ticks()
        game.current_time = current_time

        for event in pygame.event.get():
            # arret de la boucle du jeu, quand on quitte le jeu (on appuie sur la croix pour fermer le jeu)
            if event.type == pygame.QUIT:  
                run = False
                
            #test heatlthbar
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.player.health.gain_health(200)
                    game.player.health.gain_endurance(1)
                if event.key == pygame.K_DOWN:
                    game.player.health.lost_health(200)
                    game.player.health.lost_endurance(1)
                    
                if event.key == pygame.K_RIGHT:
                    game.enemy.health.gain_health(200)
                    game.enemy.health.gain_endurance(1)
                if event.key == pygame.K_LEFT:
                    game.enemy.health.lost_health(200)
                    game.enemy.health.lost_endurance(1)
            
                
           
        #update du jeu
        game.update()
    pygame.quit()
    sys.exit()

main()