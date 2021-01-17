from __future__ import division, print_function
from visual.graph import *
from visual.factorial import *
import math
def combine(a, b):
  if a - b > b:
    big = a - b
    small = b
  else:
    big = b
    small = a - b
  denominator = 1
  nominator = 1
  for i in range(a, big, -1):
    denominator *= i
  for i in range(small, 0, -1):
    nominator *= i
  c = denominator/nominator
  return c
#PROBLEM3_a  
def microstates(q,N):
  c = combine(N + q - 1, q)
  return c
#PROBLEM3_b
def entropy(q,N):
  kB = 1.38e-23
  S = kB*math.log(microstates(q, N))
  return S
  
def temperature(q,N,w):
  hbar = 1.05e-34
  deltaE = hbar * w
  Sq = entropy(q, N)
  Sq_ = entropy(q + 1, N)
  Sqq = entropy(q - 1, N)
  deltaS = (abs(Sq - Sqq) + abs(Sq - Sq_))/2
  T = deltaE/deltaS
  return T
  
#PROBLEM2_a
waygraph = gvbars(delta=0.7, color=color.red) # to make vertical bar graph
Ntotal = 6
N1 = 3
N2 = Ntotal-N1
qtotal = 4
q1 = 0
while q1 <= qtotal:
    q2 = qtotal - q1
    ways1 = combine(N1 + q1 - 1, q1)
    ways2 = combine(N2 + q2 - 1, q2)
    waygraph.plot(pos=(q1, ways1 * ways2))      
    q1 = q1 + 1
#PROBLEM2_b
Problem2_2 = gdisplay(x = 0, y = 200, height = 200, title='Problem2_b')
waygraph = gvbars(delta=0.7, color=color.yellow)
Ntotal = 700
N1 = 400
N2 = Ntotal-N1
qtotal = 100
q1 = 0
big = 0
omega = [0]
while q1 <= qtotal:
    q2 = qtotal - q1
    ways1 = combine(N1 + q1 - 1, q1)
    ways2 = combine(N2 + q2 - 1, q2)
    waygraph.plot(pos=(q1, ways1 * ways2))      ## Plot number of ways to arrange energy in both objects
    omega.append(ways1 * ways2)
    if (ways1 * ways2 > big):
      big = ways1 * ways2
      bigQ = q1
    q1 = q1 + 1
#PROBLEM2_c
half_big = big/2
print("the most probable energy distribution:", big, "\nenergy quanta:", bigQ, "\n")
for i in range(1, qtotal + 1, 1):
  if abs(omega[i] - half_big) < 2e126:
    print("half as the most probable distribution:", omega[i], "\nenergy quanta:", i - 1, "\n")

#PROBLEM3_c
Problem3_3 = gdisplay(x=0, y=0, width=600, height=150, title='ln(omega) vs. t', xtitle='q1', ytitle='ln(omega)')
gc1 = gcurve(color = color.cyan)
gc2 = gcurve(color = color.red)
gc3 = gcurve(color = color.blue)
N1 = 300
N2 = 400
qtotal = 100
q1 = 0
big = 0
while q1 <= qtotal:
    q2 = qtotal - q1
    omega1 = math.log(microstates(q1, N1))
    omega2 = math.log(microstates(q2, N2))
    omega3 = omega1 + omega2
    gc1.plot(pos = (q1, omega1))
    gc2.plot(pos = (q1, omega2))
    gc3.plot(pos = (q1, omega3))      
    q1 = q1 + 1
    if (omega3 > big):
      big = omega3
      bigQ = q1
print("the maximum value of ln():", big, "\nq1:", bigQ, "\n")

#PROBLEM3_f
m = 27e-3/6e23
k = 16
w = math.sqrt(4 * k/m)
q = 150
N = 105
celsius = temperature(q, N, w)
print(celsius, "\n")