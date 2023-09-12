from .constants import CHESSBOARD_X, CHESSBOARD_Y, MARGIN_SQUARE, SQUARE_SIZE

def calc_pos_in_board(pos_x,pos_y): #calcule la position exacte dans le board en fonction d'une position x,y
    x = CHESSBOARD_X + MARGIN_SQUARE + (pos_x * MARGIN_SQUARE) + (pos_x * SQUARE_SIZE)
    y = CHESSBOARD_Y + MARGIN_SQUARE + (pos_y * MARGIN_SQUARE) + (pos_y * SQUARE_SIZE)
    return x,y