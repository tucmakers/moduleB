from solid import *
from solid.utils import *

#total height 5.6cm
def old():
    base = cylinder(d=22, h=12)
    body = cylinder(d1=20, d2=6, h=30)
    head = rotate([0,120,0])(down(5)(cylinder(d1=6, d2=16, h=5)) + cylinder(d1=16, d2=6, h=16) + up(16)(sphere(d=6)))

    knight = base + up(12)(body) + up(38)(head)
    return knight

base = cylinder(d=22, h=12)
body = polygon([[0,0],[0,34],[18,0]])
body += translate([9,20,0])(circle(d=11))
body += translate([0,20,0])(polygon([[0,0],[0,11],[20,7],[20,0]]))
mane = circle(d=38) - translate([-13,-19,0])((square(39)))
body += translate([13,14,0])(mane)
body = linear_extrude(height=10)(body)
body = rotate([90,0,0])(body)
body = translate([-9,5,0])(body)
knight = base + up(12)(body)

# scad_render_to_file(knight, "./knight.scad")