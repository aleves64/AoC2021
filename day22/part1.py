import os
from itertools import product

with open("input", "r") as infile:
   myinput = infile.read()
myinput = myinput.split("\n")[:-1]

min_coord = -50
max_coord = 50

commands = []
grid = {}
for command in myinput:
	action = 1 if command[:2] == "on" else 0
	command = command.split("=")
	x_range = [int(x) for x in command[1][:-2].split("..")]
	y_range = [int(x) for x in command[2][:-2].split("..")]
	z_range = [int(x) for x in command[3].split("..")]

	if (x_range[0] < min_coord or x_range[1] < min_coord 
		or y_range[0] < min_coord or y_range[1] < min_coord 
		or z_range[0] < min_coord or z_range[1] < min_coord 
		or x_range[0] > max_coord or x_range[1] > max_coord 
		or y_range[0] > max_coord or y_range[1] > max_coord 
		or z_range[0] > max_coord or z_range[1] > max_coord ):
		continue

	x_range[0] = max(min_coord, min(max_coord, x_range[0]))
	y_range[0] = max(min_coord, min(max_coord, y_range[0]))
	z_range[0] = max(min_coord, min(max_coord, z_range[0]))
	x_range[1] = max(min_coord, min(max_coord, x_range[1]))
	y_range[1] = max(min_coord, min(max_coord, y_range[1]))
	z_range[1] = max(min_coord, min(max_coord, z_range[1]))
	if action:
		for coord in product(range(x_range[0], x_range[1]+1), range(y_range[0], y_range[1]+1), range(z_range[0], z_range[1]+1)):
			grid[coord] = 1
	else:
		for coord in product(range(x_range[0], x_range[1]+1), range(y_range[0], y_range[1]+1), range(z_range[0], z_range[1]+1)):
			grid[coord] = 0

print(sum(grid.values())