g = 9.8
def collision (watermelon, ball, v):
	return()
a = length * 0.5
b = height * 0.5
c = sqrt((a*a) - (b*b))
c1 = watermelon.pos - c * norm(watermelon.axis)
c2 = watermelon.pos + c * norm(watermelon.axis)
t = 0
dt = 0.01
v = vector()
p = m * v
while(v > 0):
	F = 0.5 * 1.293 * ? * mag2(v) * (-norm(v))
	p += (F + m * g) * dt 
	v = p/m
	t += dt
	if(mag(ball.pos + 0.03 * norm(v) - c1) + mag(ball.pos + 0.03 * norm(v) - c2) == 2 * a)