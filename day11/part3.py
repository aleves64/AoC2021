import os
import numpy as np
import time
from collections import deque

t0 = time.time()

with open("bigboi", "r") as infile:
	myinput = infile.read()
myinput = myinput.split("\n")[:-1]
for i in range(len(myinput)):
	myinput[i] = list(myinput[i])
	for j in range(len(myinput[i])):
		myinput[i][j] = int(myinput[i][j])
myinput = np.array(myinput)

step = 0
max_x = myinput.shape[0]
max_y = myinput.shape[1]
flashes = 0

while not flashes >= max_x * max_y:
	flashes = 0
	myinput += 1
	where = np.where(myinput > 9)
	queue = deque(zip(where[0], where[1]))
	visited = {}
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
			visited[(x,y)] = 1
			myinput[x][y] = 0
			flashes += 1
	step += 1
	print(step)
t1 = time.time()
total = t1 - t0
print(f"Total time elapsed: {total} seconds")