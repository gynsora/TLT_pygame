import pygame
from .constants import *
from .utilities import *

class Board:
    def __init__(self):
        self.board = [[0,0,0,0,0,0],
                      [0,0,0,0,0,0],
                      [0,0,0,0,0,0],
                      [0,0,0,0,0,0],
                      [0,0,0,0,0,0],
                      [0,0,0,0,0,0]
                      ]
        
    def draw_squares(self, win): #permet de dessiner les cases de l'échequier en fonction d'un élement (eau,feu, etc..)
        ROWS = len(self.board)
        COLS = len(self.board[0])
        for row in range(ROWS):
            for col in range(COLS): 
                x,y = calc_pos_in_board(row,col)
                tile_color = GREY
                if self.board[row][col] == 0 :
                    tile_color = GREY
                if self.board[row][col] == 1 :
                    tile_color = WATER
                if self.board[row][col] == 3 :
                    tile_color = FIRE
                if self.board[row][col] == 5 :
                    tile_color = EARTH
                if self.board[row][col] == 11 :
                    tile_color = WIND
                if self.board[row][col] == 12 :
                    tile_color = ICE
                if self.board[row][col] == 6 :
                    tile_color = PLANT    
                if self.board[row][col] == 8 :
                    tile_color = CHARCOAL    

                pygame.draw.rect(win, tile_color, (x,y,SQUARE_SIZE,SQUARE_SIZE))

    def draw(self,win):
        win.fill(WIND) #on remplit la surface du jeu "win" en blanc
        pygame.draw.rect(win, BLACK, (CHESSBOARD_X ,CHESSBOARD_Y ,CHESSBOARD_SIZE ,CHESSBOARD_SIZE ))
        self.draw_squares(win)

