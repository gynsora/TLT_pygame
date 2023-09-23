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
def diamond_form(target_x,target_y, range_of_spell):
    coordinates = []
    # les 2 boucle serve à crée une zone en forme de losange
    nb_tilese = range_of_spell-1
    for z in range(target_y+1, target_y+range_of_spell+1):
        for k in range(target_x-nb_tilese, target_x+nb_tilese+1):
            coordinates.append(tuple((k, z)))
        nb_tilese -= 1

    nb_tiles = range_of_spell
    for y in range(target_y ,target_y-range_of_spell-1, -1 ):
        for x in range(target_x-nb_tiles, target_x+nb_tiles+1):
            coordinates.append(tuple((x, y)))
        nb_tiles -= 1

    return list(set(coordinates))

#représente de la portée ou la zone d'un sort - sur un case cible
def target_form(target_x,target_y):
    coordinates = []
    coordinates.append(tuple((target_x , target_y)))
    return coordinates

#représente de la portée ou la zone d'un sort - en forme de croix 
def cross_form(target_x,target_y,range_of_spell):
    coordinates = []
    coordinates.append(tuple((target_x, target_y)))

    for new_x_plus in range(target_x, target_x+range_of_spell+1):
        y = target_y
        x = new_x_plus
        coordinates.append(tuple((x, y)))
    for new_x_minus in range(target_x-range_of_spell, target_x):
        y = target_y
        x = new_x_minus
        coordinates.append(tuple((x, y)))
    for new_y_plus in range(target_y, target_y+range_of_spell+1):
        y = new_y_plus
        x = target_x
        coordinates.append(tuple((x, y)))
    for new_y_minus in range(target_y-range_of_spell, target_y):
        y = new_y_minus
        x = target_x
        coordinates.append(tuple((x, y)))
    return list(set(coordinates))

#représente de la portée ou la zone d'un sort - en forme de ligne normal (attaque frontale) 
def normal_line_form(target_x,target_y, range_of_spell,player_x,player_y):
    coordinates = []
    #south
    if target_x == player_x and target_y > player_y:
        for i in range(target_y , target_y + range_of_spell):
            coordinates.append(tuple((target_x, i)))
    #north        
    if target_x == player_x and target_y < player_y:
        for i in range(target_y , target_y - range_of_spell,-1):
            coordinates.append(tuple((target_x, i)))
    #east
    if target_y == player_y and target_x > player_x:
        for i in range(target_x , target_x + range_of_spell):
            coordinates.append(tuple((i, target_y)))
    #west
    if target_y == player_y and target_x < player_x:
        for i in range(target_x , target_x - range_of_spell,-1):
            coordinates.append(tuple((i, target_y)))
    
    return coordinates
        

#permet de determine sous quel forme 
# player_x et player_y sont utilisé pour le cas ou la forme du spell correspond à une zone de sort (pas une portee)
def form_of_spell_range(target_x, target_y, range_of_spell,form_of_range_spell, player_x = 55, player_y = 55):
        # print(form_of_range_spell) 
        if form_of_range_spell == "Diamond":
            return diamond_form(target_x,target_y, range_of_spell)
        elif form_of_range_spell == "Target": 
            return target_form(target_x,target_y)
        elif form_of_range_spell == "Cross":
            return cross_form(target_x,target_y, range_of_spell)
        elif form_of_range_spell == "NormalLine" and player_x != 55 and player_y != 55:
            return normal_line_form(target_x,target_y, range_of_spell,player_x,player_y)
        

#fonction permettant de gérer les réactions élementaire A UTILISER PLUS TARD
def set_element_on_board(spell_type):
    pass

# fonction permettant de retourner le numéro d'un élément 
def element_number(spell_type):
    if spell_type == "eau" :
        return 1
    elif spell_type == "feu" :
        return 3
    elif spell_type == "terre" :
        return 5
    elif spell_type == "air" :
        return 11
    elif spell_type == "glace" :
        return 12
    elif spell_type == "plante" :
        return 6
    elif spell_type == "charbon" :
        return 8
