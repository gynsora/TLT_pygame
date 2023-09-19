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
    
#représente de la portée ou la zone d'un sort - en forme de losange
def diamond_form(target,range_of_spell):
    coordinates = []
    # les 2 boucle serve à crée une zone en forme de losange
    nb_tilese = range_of_spell-1
    for z in range(target.y+1, target.y+range_of_spell+1):
        for k in range(target.x-nb_tilese, target.x+nb_tilese+1):
            coordinates.append(tuple((k, z)))
        nb_tilese -= 1

    nb_tiles = range_of_spell
    for y in range(target.y ,target.y-range_of_spell-1, -1 ):
        for x in range(target.x-nb_tiles, target.x+nb_tiles+1):
            coordinates.append(tuple((x, y)))
        nb_tiles -= 1

    return coordinates

#représente de la portée ou la zone d'un sort - sur un case cible
def target_form(target,range_of_spell):
    coordinates = []
    coordinates.append(tuple((target.x, target.y)))
    return coordinates

#représente de la portée ou la zone d'un sort - en forme de croix 
def cross_form(target,range_of_spell):
    coordinates = []
    coordinates.append(tuple((target.x, target.y)))

    for new_x_plus in range(target.x, target.x+range_of_spell+1):
        y = target.y
        x = new_x_plus
        coordinates.append(tuple((x, y)))
    for new_x_minus in range(target.x-range_of_spell, target.x):
        y = target.y
        x = new_x_minus
        coordinates.append(tuple((x, y)))
    for new_y_plus in range(target.y, target.y+range_of_spell+1):
        y = new_y_plus
        x = target.x
        coordinates.append(tuple((x, y)))
    for new_y_minus in range(target.y-range_of_spell, target.y):
        y = new_y_minus
        x = target.x
        coordinates.append(tuple((x, y)))
    return coordinates

   