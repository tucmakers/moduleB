from solid import *
from solid.utils import *

TILE_WIDTH = 30 # mm
BASE_THICK = 8 # mm
TILE_THICK = 2 # mm
BOARD_THICK = BASE_THICK + TILE_THICK

def next_color():
    global current_color
    current_color = not current_color
    return White if current_color == True else BlackPaint

def new_tile(x_translate, y_translate, tile_color):
    tile = cube([TILE_WIDTH, TILE_WIDTH, TILE_THICK])
    return color(tile_color)(translate([x_translate,y_translate,0])(tile))

current_color = True # True for White & False for Black
board = color(Oak)(cube([TILE_WIDTH*8, TILE_WIDTH*8, BASE_THICK]))
tiles = cube(0)
for row in range(8):
    next_color() # Start each line with different color
    for col in range(8):
        tiles += new_tile(col*TILE_WIDTH,row*TILE_WIDTH,next_color())

board += up(BASE_THICK)(tiles)

# scad_render_to_file(board, "./chess_board.scad")