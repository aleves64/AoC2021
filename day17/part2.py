import os
from itertools import product

with open("input", "r") as infile:
	myinput = infile.read()
myinput =  [y[1].split('..') for y in [x.split('=') for x in myinput[:-1].split(':')[1].split(',')]]
myinput[0] = [int(x) for x in myinput[0]]
myinput[1] = [int(x) for x in myinput[1]]
min_x = myinput[0][0]
max_x = myinput[0][1]
min_y = myinput[1][0]
max_y = myinput[1][1]

def check_hit(x_vel, y_vel):
	x = 0
	y = 0
	apex = 0
	steps = 0
	while x < max_x and y > min_y:
		steps += 1
		x += x_vel
		y += y_vel
		if y > apex:
			apex = y
		if x_vel < 0:
			x_vel += 1
		elif x_vel > 0:
			x_vel -= 1
		y_vel -= 1
	
		if x >= min_x and x <= max_x and y >= min_y and y <= max_y:
			return True, apex
	return False, apex

hits = 0
for x_vel, y_vel in product(range(999),range(500,-500,-1)):
	hit, apex = check_hit(x_vel, y_vel)
	if hit:
		hits += 1
print(hits)