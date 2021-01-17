from __future__ import division, print_function
from visual import *
from math import *
from visual.graph import *
scene.width = 1000
scene.height = 600
scene.autoscale = True
g = vector(0, -9.8, 0)
wm = ellipsoid(pos = vector(0, 0, 0), axis = vector(1, 0, 0), size = vector(0.65, 0.5, 0.5), color = color.green, opacity = 0.5)
bmt = cone(pos = vector(3, 1.5,0), axis = vector(-0.1, 0, 0), radius = 0.06)
ball = sphere(pos = (bmt.pos + bmt.axis), radius = 0.015)
bmt.m = 0.0055
bmt.p = 30*norm(wm.pos - ball.pos)*bmt.m

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
t = 0
dt = 0.001
vf = 7
alpha = mag(bmt.m * g / (vf*vf))
Fw = 21.5
while(ball.pos.y > 0):
	#F = alpha * mag2(bmt.p/bmt.m) * (-norm(bmt.p))
	rate(10)
	F = vector(0, 0, 0)
	bmt.p += (F + bmt.m * g) * dt 
	if(inside(ball, wm) and dot(bmt.p, wm.pos - bmt.pos) > 0):
		bmt.p += Fw*(-norm(bmt.p)) * dt
		print("inside")
	
	t += dt
	#bmt, ball = update(bmt, ball, dt) 
	bmt.axis = abs(bmt.axis)*norm(bmt.p)
	ball.pos += bmt.p/bmt.m*dt
	bmt.pos = ball.pos - bmt.axis