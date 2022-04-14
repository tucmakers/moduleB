from solid import *
from solid.utils import *
from Pieces import *

HALF_TILE = TILE_WIDTH/2

def place_piece(i,j):
    return translate([i*TILE_WIDTH+HALF_TILE, j*TILE_WIDTH+HALF_TILE, BOARD_THICK])

pieces = [rook, knight, bishop, king, queen, bishop, knight, rook,
          pawn, pawn, pawn, pawn, pawn, pawn, pawn, pawn]

game_set = board
for i, piece in enumerate(pieces):
    game_set += color(White)(place_piece(i//8,i%8)(piece))
    if piece == king:
        piece = queen
    elif piece == queen:
        piece = king
    elif piece == knight:
        piece = rotate([0,0,180])(knight)
    game_set += color(BlackPaint)(place_piece((63-i)//8,(63-i)%8)(piece))

scad_render_to_file(game_set, "./game_set.scad")