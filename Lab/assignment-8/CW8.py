from __future__ import division, print_function
from visual import *
from visual.graph import *
scene.width = scene.height = 800

## constants
k = 9e9 # stands for One Over Four Pi Epsilon-Zero
qe = 1.6e-19  
s = 4e-11   
scalefactor = 1.0 # you may need to change this
circle_radius = 3e-10
scale = 12
proton_scalefactor = 5000

p1 = sphere(pos = vector(0, s/2, 0), radius = 1e-11, color = color.red)
q1 = qe
p2 = sphere(pos = vector(0, -s/2, 0), radius = 1e-11, color = color.blue)
q2 = -qe
proton = sphere(pos = vector(-3 * s, 0, 0), radius = 1e-15 * proton_scalefactor, color = color.yellow, make_trail = True)

## for plotting
theta = 0
dtheta = 2 * pi/scale
for i in range(scale):
	pos = vector(circle_radius * cos(theta), circle_radius * sin(theta), 0)
	E_field = k * q1/mag2(pos - p1.pos) * norm(pos - p1.pos) + k * q2/mag2(pos - p2.pos) * norm(pos - p2.pos)
	force = arrow(axis = 2.5e-20 * E_field, pos = pos, color = color.white)
	theta += dtheta

theta = 0

for i in range(scale):
	pos = vector(0, circle_radius * cos(theta), circle_radius * sin(theta))
	E_field = k * q1/mag2(pos - p1.pos) * norm(pos - p1.pos) + k * q2/mag2(pos - p2.pos) * norm(pos - p2.pos)
	force = arrow(axis = 2.5e-20 * E_field, pos = pos, color = color.white)
	theta += dtheta

egraphs = gdisplay(x = 800, width = 600, height = 600)
Ug = gcurve(color=color.yellow)
Kg = gcurve(color=color.cyan)
KUg = gcurve(color=color.magenta)

t, dt = 0, 1e-17
p = vector(0, 0, 0)
proton_mass = 1.6726219e-27
q = qe

while t < 1.385e-13:
    rate(300)
    K = mag2(p)/(2 * proton_mass)
    U = k * q * q1/mag(proton.pos - p1.pos) + k * q * q2/mag(proton.pos - p2.pos)
    Kg.plot(pos=(t,K))
    Ug.plot(pos=(t,U))
    KUg.plot(pos=(t,K+U))

    F = k * q * q1/mag2(proton.pos - p1.pos) * norm(proton.pos - p1.pos) + k * q * q2/mag2(proton.pos - p2.pos) * norm(proton.pos - p2.pos)
    p += F*dt
    proton.pos += p/proton_mass * dt

    t += dt



