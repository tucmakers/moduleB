from solid import *
from solid.utils import *
from Pieces import *

HALF_TILE = TILE_WIDTH/2

def place_piece(i,j):
    return translate([i*TILE_WIDTH+HALF_TILE+BORDER, j*TILE_WIDTH+HALF_TILE+BORDER, BOARD_THICK])

def init_game():
    for i, piece in enumerate(pieces):
        available_pieces.append(piece(i//8, i%8, White))
        if piece == King:
            piece = Queen
        elif piece == Queen:
            piece = King
        available_pieces.append(piece((63-i)//8, (63-i)%8, BlackPaint))
    render_game()

def render_game():
    game_set = board
    for piece in available_pieces:
        game_set += color(piece.color)(place_piece(piece.coordinates[0], piece.coordinates[1])(piece.object))
    scad_render_to_file(game_set, "./game_set.scad")

def search_piece(coord):
    for p in available_pieces:
        if p.coordinates == coord:
            return p
    return None

def coord_to_tuple(coord):
    return (int(coord[1])-1, letter_map[coord[0].upper()])

letter_map = {
    'A' : 7,
    'B' : 6,
    'C' : 5,
    'D' : 4,
    'E' : 3,
    'F' : 2,
    'G' : 1,
    'H' : 0}

pieces = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook,
          Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn]

available_pieces = []
init_game()
player = White
while True:
    print(("White" if player == White else "Black") + " Player")
    
    piece_coord = input("Select Piece to move: ")
    piece = search_piece(coord_to_tuple(piece_coord))
    
    target = input("Select Target Position: ")
    target_piece = search_piece(coord_to_tuple(target))
    
    if target_piece:
        available_pieces.remove(target_piece)
    piece.coordinates = (coord_to_tuple(target))
    render_game()
    player = BlackPaint if player == White else White