import os
import numpy as np
import scipy
import time
from scipy.sparse import lil_matrix

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput.split("\n")[:-1]
for i in range(len(myinput)):
	myinput[i] = [int(x) for x in list(myinput[i])]
myinput = np.array(myinput)
n = myinput.shape[0]
newinput = np.zeros((n*5, n*5))
grid = myinput
for i in range(5):
	for j in range(5):
		newinput[i*n:i*n+n,j*n:j*n+n] = grid
		grid = grid % 9 + 1
	grid = (myinput + i) % 9 + 1
n = n*5
graph = lil_matrix((n**2, n**2))
for i in range(n):
	for j in range(n):
		ind = i*n + j
		if j < n - 1:
			graph[ind,i*n + (j+1)] = newinput[i,j+1]
		if i < n - 1:
			graph[ind,(i+1)*n + j] = newinput[i+1,j]
		if j > 0:
			graph[ind,i*n + (j-1)] = newinput[i,j-1]
		if i > 0:
			graph[ind,(i-1)*n + j] = newinput[i-1,j]
t0 = time.time()
res = scipy.sparse.csgraph.shortest_path(graph, directed=True, indices = 0)
print(res[n**2 - 1])
t1 = time.time()
print(t1 - t0)