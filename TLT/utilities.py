from .constants import CHESSBOARD_X, CHESSBOARD_Y, MARGIN_SQUARE, SQUARE_SIZE, COLS, ROWS

#calcule la position exacte dans le board du jeu en fonction d'une position x,y
def calc_pos_in_board(pos_x,pos_y): 
    x = CHESSBOARD_X + MARGIN_SQUARE + (pos_x * MARGIN_SQUARE) + (pos_x * SQUARE_SIZE)
    y = CHESSBOARD_Y + MARGIN_SQUARE + (pos_y * MARGIN_SQUARE) + (pos_y * SQUARE_SIZE)
    return x,y

#renvoi vrai si x et y sont dans le board sinon renvoi faux
def coordinates_in_board(x,y):
    if x > -1 and x < ROWS and  y > -1 and y < COLS :
        return True
    else:
        return False