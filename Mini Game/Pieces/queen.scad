// Generated by SolidPython 1.1.1 on 2021-10-30 23:48:01


union() {
	cylinder(d = 24, h = 12);
	translate(v = [0, 0, 12]) {
		cylinder(d1 = 22, d2 = 12, h = 28);
	}
	translate(v = [0, 0, 40]) {
		cylinder(d = 20, h = 3);
	}
	translate(v = [0, 0, 43]) {
		union() {
			cylinder(d1 = 12, d2 = 18, h = 13);
			translate(v = [0, 0, 15]) {
				sphere(d = 6);
			}
		}
	}
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
from solid import *
from solid.utils import *

#total height 6.1cm

base = cylinder(d=24, h=12)
body = cylinder(d1=22, d2=12, h=28)
colar = cylinder(d=20, h=3)
head = cylinder(d1=12, d2=18, h=13)
head += up(15)(sphere(d=6))

queen = base + up(12)(body) + up(40)(colar) + up(43)(head)

scad_render_to_file(queen, "./queen.scad") 
 
************************************************/
