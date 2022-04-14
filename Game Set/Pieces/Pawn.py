from solid import *
from solid.utils import *

#total height 4cm

base = cylinder(d=20, h=10)
body = cylinder(d1=18, d2=8, h=15)
collar = cylinder(d=15, h=3)
head = sphere(r=7)
pawn = base + up(10)(body) + up(25)(collar) + up(33)(head)

# pawn = union()(
#     base,
#     up(10)(body),
#     up(25)(collar),
#     up(33)(head)
#     )

# scad_render_to_file(pawn, "./pawn.scad")