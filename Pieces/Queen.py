from solid import *
from solid.utils import *

#total height 6.1cm

class Queen:
    def __init__(self, i=0, j=0, color=White):
        base = cylinder(d=24, h=12)
        body = cylinder(d1=22, d2=12, h=28)
        colar = cylinder(d=20, h=3)
        head = cylinder(d1=12, d2=18, h=13)
        head += up(15)(sphere(d=6))
        queen = base + up(12)(body) + up(40)(colar) + up(43)(head)
        
        self.object = queen
        self.coordinates = (i,j)
        self.color = color

# scad_render_to_file(queen, "./queen.scad")