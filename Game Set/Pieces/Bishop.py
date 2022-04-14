from solid import *
from solid.utils import *

#total height 5.6cm

base = cylinder(d=22, h=12)
body = cylinder(d1=20, d2=10, h=24)
colar = cylinder(d=20, h=3)
head = sphere(d=18) + up(10)(sphere(d=4))
head -= translate([2,0,4])(rotate([0,20,0])(cube([2, 20, 12], center=True)))
bishop = base + up(12)(body) + up(34)(colar) + up(44)(head)

# scad_render_to_file(bishop, "./bishop.scad")