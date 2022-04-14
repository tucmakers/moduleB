from solid import *
from solid.utils import *

TILE_WIDTH = 30 # mm
BASE_THICK = 8 # mm
TILE_THICK = 2 # mm
BORDER = 10 # mm
BOARD_THICK = BASE_THICK + TILE_THICK

def next_color():
    global current_color
    current_color = not current_color
    return White if current_color == True else BlackPaint

def new_tile(x_translate, y_translate, tile_color):
    tile = cube([TILE_WIDTH, TILE_WIDTH, TILE_THICK])
    return color(tile_color)(translate([x_translate,y_translate,0])(tile))

def prepare_char(char, x, y, zrotate):
    letter = label(char)
    letter = rotate([0,0,zrotate])(letter)
    letter = resize([5,5,0])(letter)
    letter = translate([x, y, 0])(letter)
    letter = color(White)(letter)
    return letter

def generate_notation():
    notation = cube(0)
    for num, letter in enumerate(list("HGFEDCBA")):
        notation += prepare_char(letter, 3, num*TILE_WIDTH+BORDER+18, -90)
        notation += prepare_char(letter, 8*TILE_WIDTH+17, num*TILE_WIDTH+BORDER+12, 90)
        notation += prepare_char(str(num+1), num*TILE_WIDTH+BORDER+18, 2, 90)
        notation += prepare_char(str(num+1), num*TILE_WIDTH+BORDER+12, 8*TILE_WIDTH+18, -90)
    return notation
    
current_color = True # True for White & False for Black
board = color(Oak)(cube([TILE_WIDTH*8+BORDER*2, TILE_WIDTH*8+BORDER*2, BASE_THICK]))
board += up(BASE_THICK)(generate_notation())
tiles = cube(0)
for row in range(8):
    next_color() # Start each line with different color
    for col in range(8):
        tiles += new_tile(col*TILE_WIDTH,row*TILE_WIDTH,next_color())

board += translate([BORDER,BORDER,BASE_THICK])(tiles)

# scad_render_to_file(board, "./chess_board.scad")