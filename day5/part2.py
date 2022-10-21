import os
import numpy as np

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput.split("\n")[:-1]
for i in range(len(myinput)):
	myinput[i] = myinput[i].split(" -> ")
	for j in range(len(myinput[i])):
		nums = myinput[i][j].split(",")
		for k in range(len(nums)):
			nums[k] = int(nums[k])
		myinput[i][j] = nums
myinput = np.array(myinput)

mmm = np.max(myinput)
grid = np.zeros((mmm + 1,mmm + 1))
for i in range(len(myinput)):
	line = myinput[i]
	point1 = line[0]
	point2 = line[1]
	delta_x = np.abs(point1[0] - point2[0])
	delta_y = np.abs(point1[1] - point2[1])
	if delta_x == delta_y:
		if point1[0] < point2[0]:
			direction_x = 1
		else:
			direction_x = -1
		if point1[1] < point2[1]:
			direction_y = 1
		else:
			direction_y = -1
		x = point1[0]
		y = point1[1]
		for j in range(delta_x+1):
			grid[x,y] += 1
			x += direction_x
			y += direction_y
	elif point1[0] == point2[0]:
		if point1[1] > point2[1]:
			start = point2[1]
			end = point1[1]
		else:
			start = point1[1]
			end = point2[1]
		for j in np.arange(start, end + 1):
			grid[point1[0], j] += 1
	elif point1[1] == point2[1]:
		if point1[0] > point2[0]:
			start = point2[0]
			end = point1[0]
		else:
			start = point1[0]
			end = point2[0]
		for j in np.arange(start, end + 1):
			grid[j, point1[1]] += 1
indices = np.where(grid > 1)
print(indices[0].shape[0])