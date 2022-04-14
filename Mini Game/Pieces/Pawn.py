from solid import *
from solid.utils import *

#total height 4cm
class Pawn:
    def __init__(self, i=0, j=0, color=White):
        base = cylinder(d=20, h=10)
        body = cylinder(d1=18, d2=8, h=15)
        collar = cylinder(d=15, h=3)
        head = sphere(r=7)
        pawn = base + up(10)(body) + up(25)(collar) + up(33)(head)
        
        self.object = pawn
        self.coordinates = (i,j)
        self.color = color

# pawn = union()(
#     base,
#     up(10)(body),
#     up(25)(collar),
#     up(33)(head)
#     )

# scad_render_to_file(pawn, "./pawn.scad")