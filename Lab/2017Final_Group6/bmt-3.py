from __future__ import division, print_function
from visual import *
from math import *
from visual.graph import *
scene.width = 600
scene.height = 400
scene.autoscale = True
scene.range = (2, 2, 1)
xmax = 2
ymax = 2
g = vector(0, -9.8, 0)
wm = ellipsoid(pos = vector(0, 0, 0), axis = vector(1, 0, 0), size = vector(0.3, 0.22, 0.16), color = color.green, opacity = 0.4)
wmmeat = ellipsoid(pos = wm.pos, axis = wm.axis, size = wm.size - 0.02*vector(2, 2, 2), color = color.red, opacity  = 0.3)
bmt = cone(pos = (2, 2, 0), axis = vector(-0.1, 0, 0), radius = 0.06)
ball = sphere(pos = (bmt.pos + bmt.axis), radius = 0.015)
vdist = gdisplay(x=600, y=0, width=700, height=500, xtitle='x', ytitle='y', xmax = xmax, xmin = -xmax, ymax = ymax, ymin = 0)
fdot = gdots(color = color.cyan)
wm.m = 11.4
bmt.m = 0.0055
bmt.p = (30*norm(wm.pos - ball.pos))*bmt.m
#key = scene.kb.getkey()
#print(key)
#bmt.p = vector(-80, 0 ,0)*bmt.m
def inside(ball, wm):
	checkpoint = ball.pos+ball.radius*norm(wm.pos - ball.pos)
	if(mag(checkpoint-wm.c1)+mag(checkpoint - wm.c2) <= 2*wm.a):
		return True
	return False

def dot(a, b):
	return a.x*b.x+a.y*b.y+a.z*b.z

wm.a = wm.size.x * 0.5
wm.b = wm.size.y * 0.5
wm.c = sqrt((wm.a*wm.a) - (wm.b*wm.b))
wm.c1 = wm.pos - wm.c * norm(wm.axis)
wm.c2 = wm.pos + wm.c * norm(wm.axis)
dt = 0.001
vf = 3
alpha = mag(bmt.m * g / (vf*vf))
Fw = 21.5
count = 0
startx = xmax
record = []
maxp = 0
minp = 999999
while(startx >= -xmax):
	starty = ymax
	while(starty >= 0):
		scene.range = (2, 2, 1)
		t = 0
		end = 0
		ball.pos = vector(startx, starty, 0)
		bmt.pos = ball.pos - bmt.axis
		bmt.p = (30*norm(wm.pos - ball.pos))*bmt.m
		if(inside(ball, wm) != True):
			while(ball.pos.y > wm.pos.y - wm.size.y/2 and end == 0):
				rate(10000)
				scene.range = (mag(bmt.pos)+0.25, mag(bmt.pos)+0.25, 1)
				count += 1
				#if(count % 100 == 0):
					#scene.waitfor('click')
				F = vector(0, 0, 0)
				F = alpha * mag2(bmt.p/bmt.m) * (-norm(bmt.p))
				tem = vector(0, 0, 0)
				if(inside(ball, wm)):
					tem = bmt.p
					F += Fw*(-norm(bmt.p))
					print("inside")
				else:
					F += bmt.m * g
					
				bmt.p += F*dt
				t += dt
				if(inside(ball, wm)):
					end = 1
					print("end")
				else:
					bmt.axis = abs(bmt.axis)*norm(bmt.p)
					ball.pos += bmt.p/bmt.m*dt
					bmt.pos = ball.pos - bmt.axis
			if(end == 1):
				record.append([startx, starty, mag(bmt.p)])
				fdot.plot(pos = (startx, starty), color = color.cyan)
				#print(record[len(record)-1])
				if (mag(bmt.p) > maxp):
					maxp = mag(bmt.p)
				if (mag(bmt.p) < minp):
					minp = mag(bmt.p)
		starty = starty - 0.1
	startx = startx - 0.1
scene.range = (2, 2, 1)
scene.center = (0, 0.5, 0)
for i in record:
	sphere(pos = vector(i[0], i[1], 0), radius = 0.1*(i[2] - minp)/(maxp - minp), color = vector(0.5+0.5*(i[2] - minp)/(maxp - minp), 0.5, 0.5), opacity = 0.7)