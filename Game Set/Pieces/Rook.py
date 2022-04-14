from solid import *
from solid.utils import *

#total height 5cm

def alternative():
    head = difference() (
        cylinder(d=18, h=13),
        up(8)(cylinder(d=14, h=6))
    )
    # alternative way to create upper part of rook with lists
    crown = union() (
        *(up(11)(rotate([0,0,a])(cube([4,19,6], center=True))) for a in [0, 60, 120])
    )
    head -= crown
    r = union() (base,
        up(12)(body),
        up(34)(colar),
        up(37)(head)
    )

    return r

base = cylinder(d=22, h=12)
body = cylinder(d1=20, d2=10, h=24)
collar = cylinder(d=20, h=3)
head = cylinder(d=18, h=13)
head -= up(8)(cylinder(d=14, h=6))

for a in [0, 60, 120]:
    head -= up(11)(rotate([0,0,a])(cube([4,19,6], center=True)))

rook = base + up(12)(body) + up(34)(collar) + up(37)(head)
        
# scad_render_to_file(rook, "./rook.scad")