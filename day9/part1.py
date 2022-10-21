import os
import numpy as np

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput.split("\n")[:-1]
for i in range(len(myinput)):
	digits = list(myinput[i])
	for j in range(len(digits)):
		digits[j] = int(digits[j])
	myinput[i] = digits
myinput = np.array(myinput)

risk = 0
lowpoints = []
for i in range(myinput.shape[0]):
	for j in range(myinput.shape[1]):
		val = myinput[i][j]
		ok = True
		if i > 0 and val >= myinput[i-1][j]:
			ok = False
		elif i < myinput.shape[0] - 1 and val >= myinput[i+1][j]:
			ok = False
		elif j > 0 and val >= myinput[i][j-1]:
			ok = False
		elif j < myinput.shape[1] - 1 and val >= myinput[i][j+1]:
			ok = False
		if ok:
			lowpoints.append((i,j))

def bfs(i, j, visited):
	val = myinput[i][j]
	acc = 1

	if (i,j) in visited:
		return 0
	else:
		visited.append((i,j))

	if i > 0 and val < myinput[i-1][j] and myinput[i-1][j] < 9:
		acc += bfs(i - 1, j, visited)
	if i < myinput.shape[0] - 1 and val < myinput[i+1][j] and myinput[i+1][j] < 9:
		acc += bfs(i + 1, j, visited)
	if j > 0 and val < myinput[i][j-1] and myinput[i][j-1] < 9:
		acc += bfs(i, j - 1, visited)
	if j < myinput.shape[1] - 1 and val < myinput[i][j+1] and myinput[i][j+1] < 9:
		acc += bfs(i, j + 1, visited)
	return acc

basinsizes = []
for point in lowpoints:
	i, j = point
	visited = []
	basinsizes.append(bfs(i,j, visited))
basinsizes = sorted(basinsizes, reverse=True)
acc = 1
for i in range(3):
	acc *= basinsizes[i]
print(acc)