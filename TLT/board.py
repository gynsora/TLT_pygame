import pygame
from .constants import *
from .utilities import *

class Board:
    def __init__(self):
        self.board = [ [0 for x in range(COLS)] for y in range(ROWS)]
        # self.board[1][2] = 1
    def draw_board(self, win): #permet de dessiner les cases de l'échequier en fonction d'un élement (eau,feu, etc..)
        for row in range(ROWS):
            for col in range(COLS): 
                x,y = calc_pos_in_board(row,col)
                tile_color = GREY
                if self.board[col][row] == 0 :  #neutre == 0
                    tile_color = GREY
                if self.board[row][col] == 1 :  #eau == 1
                     tile_color = WATER
                if self.board[row][col] == 3 :  #feu == 3
                    tile_color = FIRE
                if self.board[row][col] == 5 :  #terre == 5
                    tile_color = EARTH
                if self.board[row][col] == 11 : #air == 11
                    tile_color = WIND
                if self.board[row][col] == 12 : #glace == 12
                    tile_color = ICE
                if self.board[row][col] == 6 :  #plante == 6
                    tile_color = PLANT    
                if self.board[row][col] == 8 :  #charbon == 8
                    tile_color = CHARCOAL    

                pygame.draw.rect(win, tile_color, (x,y,SQUARE_SIZE,SQUARE_SIZE))

    def draw(self,win):
        pygame.draw.rect(win, BLACK, (CHESSBOARD_X ,CHESSBOARD_Y ,CHESSBOARD_SIZE ,CHESSBOARD_SIZE ))
        self.draw_board(win)

