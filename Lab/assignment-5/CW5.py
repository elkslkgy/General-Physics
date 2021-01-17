from __future__ import division, print_function
from visual import *
from visual.graph import *
scene.width = 800

##Constants
massAu = (79 + 118) * 1.7e-27
massAlpha = (2 + 2) * 1.7e-27
qAu = 2 * 1.6e-19
qAlpha = 79 * 1.6e-19
k = 9e9     ## one-over-four-pi-epsilon-zero
deltat = 1e-23
b1 = 5e-15
b2 = 1e-14
b3 = 1e-13
b_degree45 = 3.99789821818e-14
b_degree90 = 1.757651506825e-14
b_degree135 = 7.3758561121e-15

##Objects
Au = sphere(pos = vector(0, 0, 0), radius = 8e-15, color = color.yellow, make_trail = True)
Alpha = sphere(pos = vector(-1e-13, b1, 0), radius = 2e-15, color = color.red, make_trail = True)

#Initial Values
pAu = massAu * vector(0, 0, 0)           
pAlpha = vector(1.043e-19, 0, 0)
pTotal = pAu + pAlpha
F = (k * qAu * qAlpha/mag2(Au.pos - Alpha.pos)) * norm(Alpha.pos - Au.pos)
t = 0

##Calculation Loop
X_momentum = gdisplay(x = 0, y = 400, height = 200)
px_Alpha = gcurve(color = color.red)
px_Au = gcurve(color = color.blue)
px_total = gcurve(color = color.cyan)
Y_momentum = gdisplay(x = 0, y = 600, height = 200)
py_Alpha = gcurve(color = color.red)
py_Au = gcurve(color = color.blue)
py_total = gcurve(color = color.cyan)
while t < 1e-20:
    rate(1000)
    pAlpha += F * deltat
    pAu -= F * deltat
    Alpha.pos += (pAlpha/massAlpha) * deltat
    Au.pos += (pAu/massAu) * deltat
    F = k * qAu * qAlpha/mag2(Au.pos - Alpha.pos) * norm(Alpha.pos - Au.pos)
    pTotal = pAlpha + pAu

    px_Alpha.plot(pos = (t, pAlpha.x))
    px_Au.plot(pos = (t, pAu.x))
    px_total.plot(pos = (t, pTotal.x))
    py_Alpha.plot(pos = (t, pAlpha.y))
    py_Au.plot(pos = (t, pAu.y))
    py_total.plot(pos = (t, pTotal.y))
    
    t = t + deltat
final_direction = norm(pAlpha/massAlpha)
theta = acos(final_direction.x)/pi * 180
print("theta = ", theta)

b1_theta = 148.676319269
b2_theta = 121.24995315
b3_theta = 14.4091116847
print("b1_theta = ", b1_theta)
print("b2_theta = ", b2_theta)
print("b3_theta = ", b3_theta)
print("degree45_b = ", b_degree45)
print("degree90_b = ", b_degree90)
print("degree135_b = ", b_degree135)