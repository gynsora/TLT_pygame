import pygame
from .constants import GREY ,BLACK ,WHITE ,ROWS ,COLS ,CHESSBOARD_SIZE ,SQUARE_SIZE ,MARGIN_SQUARE ,CHESSBOARD_X ,CHESSBOARD_Y

class Board:
    def __init__(self):
        self.board = [[0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0]
                      ]
        
    def draw_squares(self, win): #permet de dessiner les cases de l'échequier
        for row in range(ROWS):
            for col in range(COLS): 
                x = CHESSBOARD_X + MARGIN_SQUARE + (row * MARGIN_SQUARE) + (row * SQUARE_SIZE)
                y = CHESSBOARD_Y + MARGIN_SQUARE + (col * MARGIN_SQUARE) + (col * SQUARE_SIZE)
                if self.board[row][col] == 0 :
                    pygame.draw.rect(win, GREY, (x,y,SQUARE_SIZE,SQUARE_SIZE))

    def draw(self,win):
        win.fill(WHITE) #on remplit la surface du jeu "win" en blanc
        pygame.draw.rect(win, BLACK, (CHESSBOARD_X ,CHESSBOARD_Y ,CHESSBOARD_SIZE ,CHESSBOARD_SIZE ))
        self.draw_squares(win)

