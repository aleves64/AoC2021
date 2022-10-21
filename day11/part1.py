import os
import numpy as np
from collections import deque

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput.split("\n")[:-1]
for i in range(len(myinput)):
	myinput[i] = list(myinput[i])
	for j in range(len(myinput[i])):
		myinput[i][j] = int(myinput[i][j])
myinput = np.array(myinput)

steps = 100
flashes = 0
max_x = myinput.shape[0]
max_y = myinput.shape[1]

for i in range(steps):
	myinput += 1
	where = np.where(myinput > 9)
	myinput[where] -= 1
	queue = deque(zip(where[0], where[1]))
	visited = []
	while len(queue) != 0:
		x, y = queue.popleft()
		if (x,y) in visited or x < 0 or x >= max_x or y < 0 or y >= max_y:
			continue
		myinput[x][y] += 1
		if myinput[x][y] > 9:
			queue.append((x-1, y+1))
			queue.append((x, y+1))
			queue.append((x+1, y+1))
			queue.append((x+1, y))
			queue.append((x+1, y-1))
			queue.append((x, y-1))
			queue.append((x-1, y-1))
			queue.append((x-1, y))
			visited.append((x,y))
			myinput[x][y] = 0
			flashes += 1
print(flashes)