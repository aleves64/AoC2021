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

mmm = np.max(myinput + 1)
grid = np.zeros((mmm,mmm))
for i in range(len(myinput)):
	line = myinput[i]
	point1 = line[0]
	point2 = line[1]
	if point1[0] == point2[0]:
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