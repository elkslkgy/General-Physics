from __future__ import division, print_function
from visual import *
scene.width = 1000
scene.height = 700
R = 0.08
Q = 50e-9
Nq = 25   
dtheta = 2*pi/Nq
dQ = Q/Nq
k = 9e9
scalefactor = 7e-7
## source charges
ring(pos=vector(0,0,0), radius=R, color=color.red, thickness=0.005)
sources = []
angles=arange(0,2*pi,dtheta)

for theta in angles:
    a = sphere(pos=vector(0, R*cos(theta), R*sin(theta)), radius=0.007, color=color.cyan, q=dQ)
    sources.append(a)

obs = []
for i in range(17):
	field = arrow(pos = vector(-2 * R + 1/4 * R * i, 0, 0))
	obs.append(field)

## outer loop picks observation location
for Ea in obs:
	Enet = vector(0,0,0)
	## inner loop goes through all source charges
	for scharge in sources:
		## add code to calculate contribution of this source charge
		r = Ea.pos - scharge.pos
		Enet += k * dQ/mag2(r) * norm(r)
		## add this to net field at this location
	Ea.axis = Enet * scalefactor

off_axis = []
for i in range(7):
	place = arrow(pos = vector(R/2, 0, -2 * R + 2/3 * R * i), color = color.yellow)
	off_axis.append(place)

## outer loop picks observation location
for Ea in off_axis:
	Enet = vector(0,0,0)
	## inner loop goes through all source charges
	for scharge in sources:
		## add code to calculate contribution of this source charge
		r = Ea.pos - scharge.pos
		Enet += k * dQ/mag2(r) * norm(r)
		## add this to net field at this location
	Ea.axis = Enet * scalefactor

#mouseposition = scene.waitfor('click').pos ## wait for mouse click, save the mouse position
#ball = sphere(pos=mouseposition, radius = 0.01, color = color.red, opacity = 0.4) ## use mouse position when creating electron

ball = sphere(pos = vector(2 * R, 0, 0), radius = 0.01, color = color.red, opacity = 0.4, make_trail = True)
q = -1.6e-19
dt = 1e-11
electron_p = vector(0, 0, 0)
electron_m = 9.1e-31

while true:
	rate(500)
	Enet = vector(0,0,0)
	## inner loop goes through all source charges
	for scharge in sources:
		## add code to calculate contribution of this source charge
		r = ball.pos - scharge.pos
		Enet += k * dQ/mag2(r) * norm(r)
		## add this to net field at this location
	Fq = Enet * q
	electron_p += Fq * dt
	ball.pos += electron_p/electron_m * dt