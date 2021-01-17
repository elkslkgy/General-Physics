from __future__ import division, print_function
from visual import *
from math import *
from visual.graph import *
scene.width = 600
scene.height = 400
scene.autoscale = True
scene.range = (2, 2, 1)
g = vector(0, -9.8, 0)
wm = ellipsoid(pos = vector(0, 0, 0), axis = vector(1, 0, 0), size = vector(0.3, 0.22, 0.16), color = color.green, opacity = 0.5, shininess = 1)
wmmeat = ellipsoid(pos = wm.pos, axis = wm.axis, size = wm.size - 0.02*vector(2, 2, 2), color = color.red, opacity  = 1)
floor = box(pos = wm.pos - vector(0, wm.size.y/2, 0), size = vector(3, 0.001, 3), color = color.yellow)
ev = scene.mouse.getclick()
bmt = cone(pos = ev.pos, axis = vector(-0.09, 0, 0), radius = 0.03)
ball = sphere(pos = (bmt.pos + bmt.axis), radius = 0.0125)
vdist = gdisplay(x=800, y=0, width=500, height=700, xtitle='ds', ytitle='V', xmin = 0, xmax = 0.02)
f1 = gdots(color = color.cyan)
wm.m = 11.4
bmt.m = 0.0055
vinit = 1
bmt.p = (vinit*norm(wm.pos - ball.pos))*bmt.m
#key = scene.kb.getkey()
#print(key)
#bmt.p = vector(-80, 0 ,0)*bmt.m
def inside(ball, wm):
	checkpoint = ball.pos+ball.radius*norm(wm.pos - ball.pos)
	if(mag(checkpoint-wm.c1)+mag(checkpoint - wm.c2) <= 2*wm.a):
		return True
	return False

wm.a = wm.size.x * 0.5
wm.b = wm.size.y * 0.5
wm.c = sqrt((wm.a*wm.a) - (wm.b*wm.b))
wm.c1 = wm.pos - wm.c * norm(wm.axis)
wm.c2 = wm.pos + wm.c * norm(wm.axis)
t = 0
dt = 0.001
vf = 6.5
alpha = mag(bmt.m * g / (vf*vf))
kniefm = 0.5
dis = 1.05
ds = 0.02
Fw = (dis+ds)*kniefm*mag(g)/ds
end = 0
Fg_arrow = arrow(pos = ball.pos, axis = bmt.m*g, color = color.yellow, opacity = 0.5)
Fa_arrow = arrow(pos = ball.pos, axis = alpha*mag2(bmt.p/bmt.m)*(-norm(bmt.p)), color = color.blue, opacity = 0.5)
Fw_arrow = arrow(pos = ball.pos, axis = vector(0, 0 ,0), color = color.red, opacity = 0.1, shaftwidth = 0.1)
#print("initial condition:")
#print("batmintion is at",bmt.pos,"watermelon is at ",wm.pos)
#print("force of air :",alpha,"* v^2")
#print("force of watermelon :",Fw)
dv = 1
while(end == 0 and vinit <= 5000):
	ball.pos = ev.pos
	bmt.p = (vinit*norm(wm.pos - ball.pos))*bmt.m
	bmt.axis = abs(bmt.axis)*norm(bmt.p)
	bmt.pos = ball.pos - bmt.axis
	print("vinit =",vinit)
	while(ball.pos.y > wm.pos.y - wm.size.y/2 and end == 0):
		print("batmintion is at",bmt.pos,"v = ",mag(bmt.p/bmt.m))
		Fg_arrow.pos = ball.pos
		Fa_arrow.pos = ball.pos
		Fw_arrow.pos = ball.pos
		Fw_arrow.axis = vector(0, 0 ,0)
		f1.plot(pos = (t, mag(bmt.p/bmt.m)))
		#scene.range = (mag(bmt.pos)+0.25, mag(bmt.pos)+0.25, 1)
		F = vector(0, 0, 0)
		F = alpha * mag2(bmt.p/bmt.m) * (-norm(bmt.p))
		Fa_arrow.axis = F
		F += bmt.m * g
		Fg_arrow.axis = bmt.m * g
		bmt.p += F*dt
		bmt.axis = abs(bmt.axis)*norm(bmt.p)
		ball.pos += bmt.p/bmt.m*dt
		bmt.pos = ball.pos - bmt.axis
		t += dt
		rate(500)
		if(inside(ball, wm)):
			ddt = 0.001*dt
			pos = ball.pos
			while(inside(ball, wm)):
				bmt.p -= alpha * mag2(bmt.p/bmt.m) * (-norm(bmt.p)) * ddt
				pos -= bmt.p / bmt.m * ddt
				t -= ddt
			ball.pos = pos
			bmt.pos = ball.pos - bmt.axis
			end = 1
	if(end == 1):
		if(mag2(bmt.p)/2/bmt.m < Fw*0.02):
			f1.plot(pos = ((mag2(bmt.p)/2/bmt.m/Fw), vinit))
			end = 0
	vinit += dv
print("Initial Condition :")
print("start pos :",ev.pos,", dis =",mag(ev.pos),"m")
print("start v :", vinit,"m/s")