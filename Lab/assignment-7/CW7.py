from visual import *
from random import random
from visual.graph import *
import numpy as np

N = 50                              # number of the He atoms
L = ((24.4e-3/(6e23))*N)**(1/3.0)/2 # side length of the cubic container box

m, size = 4e-3/6e23, 310e-12        # He atoms mass, radius are made 10 times bigger for easiear collision
# size is the atom's size.
L_size = L - size                   # L - size, used many times in the program
# i also don't know what does "L_size" mean. 
k, T = 1.38e-23, 298.0              # k = Boltzmann constant, and T = temperature in unit K

t, dt = 0, 0.5e-13                  # dt = 0.5E-13 second
vrms = (3 * k * T/m)**0.5               # root mean square velocity at T
print(vrms)
atoms = []                          # list to contain the 50 atoms
delta_p = 0
dt_times = 0
before = []
for i in range(N):
	before.append((0, 0, 0))

before_pos = np.zeros((N))
hit_times = np.zeros((N))

IDEAL = 8 * L**3/(4 * pi * size**2 * N)

# histogram initialization, more on this see http://vpython.org/contents/docs/graph.html
deltav = 100. #what the fuck it is
vdist = gdisplay(x = 800, y = 0, ymax = N * deltav/1000., width = 500, height = 300, xtitle = 'v', ytitle = 'dN')
theory = gcurve(color = color.cyan) # plot the theoretical speed distribution
dv = 10. #what the fuck it is again

for v in arange(0., 3001. + dv, dv): #the first is the start, the second is the end, the third is the increase or decrease rate
    theory.plot(pos = (v, (deltav/dv) * N * 4. * pi * (( m/(2. * pi * k * T) )**1.5) * exp( (-0.5 * m * v**2)/(k * T) ) * v**2 * dv)) #what the fuck it is again and again.
observation = ghistogram(bins = arange(0., 3000., deltav), accumulate = 1, average = 1, color = color.red)
# what do "accumulate" and "average" mean?

# initialization of display, setting up for the random position distribution and random velocity direction of atoms
scene = display(width = 800, height = 800, background = (0.2, 0.2, 0))
#what does the "background" mean?
container = box(length = 2 * L, height = 2 * L, width = 2 * L, opacity = 0.2, color = color.yellow)


# Initialize atom position and velocity
for i in range(N):
    position = vector(-L_size + 2 * L_size * random(), -L_size + 2 * L_size * random(), -L_size + 2 * L_size * random())
    #why it should be minus first and then plus twice
    if i == N - 1:
        atom = sphere(pos = position, radius = size, color = color.yellow, make_trail = True, retain = 600)
        # what does "retain" mean?
    else:
        atom = sphere(pos = position, radius = size, color = (random(), random(), random()))
        theta, phi = pi * random(), 2 * pi * random()
        #what does "phi" mean?
    atom.m, atom.v = m, vector(vrms * sin(theta) * cos(phi), vrms * sin(theta) * sin(phi), vrms * cos(theta))
    
    atoms.append(atom)

def vcollision(a1,a2):
    '''
    Function to find the velocities of atoms after each collision
    '''
    v1prime = a1.v - 2 * a2.m/(a1.m + a2.m) * (a1.pos - a2.pos) * dot(a1.v - a2.v, a1.pos - a2.pos)/abs(a1.pos - a2.pos)**2
    v2prime = a2.v - 2 * a1.m/(a1.m + a2.m) * (a2.pos - a1.pos) * dot(a2.v - a1.v, a2.pos - a1.pos)/abs(a2.pos - a1.pos)**2
    return v1prime, v2prime

while True:
    t += dt
    #dt = 0.5e-13 
    rate(1000)
    
    #calculate new positions for all atoms and plot histogram
    v = []
    pos = []
    radius = []
    p = []
    for i in range(N):

        #### calculate new positions for atoms
        atoms[i].pos += atoms[i].v * dt
        before_pos[i] += mag(atoms[i].v * dt)

        pos.append(atoms[i].pos)
        radius.append(size)
        p.append(m * atoms[i].v)
        v.append(mag(atoms[i].v))

    observation.plot(data = v)

    pos = array(pos)
    radius = array(radius)
    p = array(p)

    #outside = less_equal(pos, -L + size) # walls closest to origin
    #p_before = p
    #p1 = p * outside
    #p = p - p1 + abs(p1) # force p component inward
    #delta_p += sum(abs(p - p_before))
    #pos += 2*outside*(-L_size - pos)
    #outside = greater_equal(pos, L - size) # walls farther from origin
    #p_before = p
    #p1 = p * outside
    #p = p - p1 - abs(p1) # force p component inward
    #delta_p += sum(abs(p - p_before))
    #pos += 2*outside*(L_size - pos)

    for i in range(N):
        atoms[i].v = p[i]/m
        v.append(mag(atoms[i].v))

    #### find collisions between atoms, and then handle their collisions
    r = pos - pos[:,newaxis] # all pairs of atom-to-atom vectors
    rmag = sqrt(sum(square(r), -1)) # atom-to-atom scalar distances
    hit = less_equal(rmag, radius + radius[:,newaxis]) - identity(N)
    hitlist = sort(nonzero(hit.flat)[0]).tolist() # i,j encoded as i*N+j
    
    for i in range(len(hitlist)):
    	atom1 = hitlist[i]/N
    	atom2 = hitlist[i] % N
    	if (atom1 > atom2):

    		while (mag(atoms[atom1].pos - atoms[atom2].pos) < 2 * size):
    			#deltatt = dt/1000
    			atoms[atom1].pos -= atoms[atom1].v * dt
    			atoms[atom2].pos -= atoms[atom2].v * dt


    			deltatt = (mag(atoms[atom1].pos - atoms[atom2].pos) - 2 * size)/abs(dot(atoms[atom1].v - atoms[atom2].v, norm(atoms[atom1].pos - atoms[atom2].pos)))
    			
    			atoms[atom1].pos += atoms[atom1].v * deltatt
    			atoms[atom2].pos += atoms[atom2].v * deltatt

    			for i in range(N):
        			atoms[i].v = p[i]/m
        			v.append(mag(atoms[i].v))

    		atoms[atom1].v, atoms[atom2].v = vcollision(atoms[atom1], atoms[atom2])
    		v[atom1], v[atom2] = atoms[atom1].v, atoms[atom2].v 
    		p[atom1], p[atom2] = m * v[atom1], m * v[atom2]
    		pos[atom1], pos[atom2] = atoms[atom1].pos, atoms[atom2].pos
    		hit_times[atom1] += 1
    		hit_times[atom2] += 1

    		#outside = less_equal(pos, -L + size) # walls closest to origin
    		#p_before = p
    		#p1 = p * outside
    		#p = p - p1 + abs(p1) # force p component inward
    		#delta_p += sum(abs(p - p_before))
    		#pos += 2*outside*(-L_size - pos)
    		#outside = greater_equal(pos, L - size) # walls farther from origin
    		#p_before = p
    		#p1 = p * outside
    		#p = p - p1 - abs(p1) # force p component inward
    		#delta_p += sum(abs(p - p_before))
    		#pos += 2*outside*(L_size - pos)

    #### find collisions between atoms and walls, and then handle their collision
    outside = less_equal(pos, -L + size) # walls closest to origin
    p_before = p
    p1 = p * outside
    p = p - p1 + abs(p1) # force p component inward
    delta_p += sum(abs(p - p_before))
    pos += 2*outside*(-L_size - pos)
    outside = greater_equal(pos, L - size) # walls farther from origin
    p_before = p
    p1 = p * outside
    p = p - p1 - abs(p1) # force p component inward
    delta_p += sum(abs(p - p_before))
    pos += 2*outside*(L_size - pos)

    for i in range(N):
    	atoms[i].pos = pos[i]
        atoms[i].v = p[i]/m
        v.append(mag(atoms[i].v))

    #### calculate the momentum transferred to the walls and obtain the pressure
    #### print the averaged pressure on the walls every 1000*dt
    dt_times += 1
    if (dt_times == 1000):
    	print("pressure:", delta_p/(dt * 1000)/(2 * L * 2 * L * 6))

    	for i in range(N):
    		if (hit_times[i] == 0):
    			hit_times[i] = 1
    	divide = before_pos/hit_times
    	mean_free_path = sum(divide)/N
    	print("mean_free_path:", mean_free_path)
    	print('\n')
    	
    	before_pos = np.zeros((N))
    	hit_times = np.zeros((N))

    	dt_times = 0
    	delta_p = 0