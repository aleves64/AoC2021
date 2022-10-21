import os
import numpy as np

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput.split("\n")
grid = []
for i in range(len(myinput)):
	if myinput[i] == "":
		break
	myinput[i] = myinput[i].split(",")
	for j in range(len(myinput[i])):
		myinput[i][j] = int(myinput[i][j])
gridspots = myinput[:i]
folds = []
skip = len("fold along ")
for j in range(i+1, len(myinput)):
	if myinput[j] == "":
		break
	tmp = myinput[j][11:]
	tmp = tmp.split("=")
	tmp[1] = int(tmp[1])
	folds.append(tmp)

nx, ny = np.max(gridspots,axis=0) + 1
grid = np.zeros((nx,ny))
for x, y in gridspots:
	grid[x][y] = 1

latestx = nx
latesty = ny
for axis, coord in folds:
	i = 1
	if axis == "x":
		grid[coord] = -1
		while coord + i < latestx and coord - i >= 0:
			grid[coord - i] += grid[coord + i]
			i += 1
		latestx = coord
	else:
		grid[:,coord] = -1
		while coord + i < latesty and coord - i >= 0:
			grid[:,coord - i] += grid[:,coord + i]
			i += 1
		latesty = coord
display = grid[:latestx,:latesty].T
for x in range(display.shape[0]):
	for y in range(display.shape[1]):
		if display[x][y] > 0:
			print("#", end = '')
		else:
			print(".", end = '')
	print()