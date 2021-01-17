from __future__ import division, print_function
from visual import *
from math import *
from visual.graph import *
scene.width = 600
scene.height = 400
scene.autoscale = True
scene.range = (2, 2, 1)
g = vector(0, -9.8, 0)
wm = ellipsoid(pos = vector(0, 0, 0), axis = vector(1, 0, 0), size = vector(0.3, 0.22, 0.16), color = color.green, opacity = 0.1, shininess = 1)
wmmeat = ellipsoid(pos = wm.pos, axis = wm.axis, size = wm.size - 0.02*vector(2, 2, 2), color = color.red, opacity  = 0.1)
ev = scene.mouse.getclick()
bmt = cone(pos = ev.pos, axis = vector(-0.09, 0, 0), radius = 0.03)
ball = sphere(pos = (bmt.pos + bmt.axis), radius = 0.0125)
vdist = gdisplay(x=800, y=0, width=500, height=300, xtitle='t', ytitle='V')
f1 = gcurve(color = color.cyan)
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

def dot(a, b):
	return a.x*b.x+a.y*b.y+a.z*b.z

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
count = 0
end = 0
Fg_arrow = arrow(pos = ball.pos, axis = bmt.m*g, color = color.yellow, opacity = 0.5)
Fa_arrow = arrow(pos = ball.pos, axis = alpha*mag2(bmt.p/bmt.m)*(-norm(bmt.p)), color = color.blue, opacity = 0.5)
Fw_arrow = arrow(pos = ball.pos, axis = vector(0, 0 ,0), color = color.red, opacity = 0.1, shaftwidth = 0.01)
print("initial condition:")
print("batmintion is at",bmt.pos,"watermelon is at ",wm.pos)
print("force of air :",alpha,"* v^2")
print("force of watermelon :",Fw)
dv = 1
while(end == 0 and vinit <= 5000):
	ball.pos = ev.pos
	bmt.p = (vinit*norm(wm.pos - ball.pos))*bmt.m
	bmt.axis = abs(bmt.axis)*norm(bmt.p)
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
		rate(1000)
		tem = vector(0, 0, 0)
		if(inside(ball, wm)):
			F += Fw*(-norm(bmt.p))
			Fw_arrow.axis = Fw*(-norm(bmt.p))
			end = 1
			#print("inside")
		else:
			F += bmt.m * g
			
		Fg_arrow.axis = bmt.m * g
		bmt.p += F*dt
		t += dt
		#print("force of air :",mag(Fa_arrow.axis),"force of wm :",mag(Fw_arrow.axis))
		if(inside(ball, wm) and bmt.p.y >= 0):
			#bmt.p = vector(0, 0, 0)
			end = 1
			#print("end")
		else:
			bmt.axis = abs(bmt.axis)*norm(bmt.p)
			ball.pos += bmt.p/bmt.m*dt
			bmt.pos = ball.pos - bmt.axis
	if(end == 1 ):
		if(mag(bmt.pos) < Fw*0.2 and bmt.p.y >= 0):
			end = 0
	vinit += dv