import os
import numpy as np
import scipy
from scipy.sparse import lil_matrix

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput.split("\n")[:-1]
for i in range(len(myinput)):
	myinput[i] = [int(x) for x in list(myinput[i])]
myinput = np.array(myinput)
n = myinput.shape[0]
graph = lil_matrix((n**2, n**2))
for i in range(n):
	for j in range(n):
		this_node = np.ravel_multi_index([[i],[j]], (n,n))[0]
		if j < n - 1:
			next_node = np.ravel_multi_index([[i],[j+1]], (n,n))[0]
			graph[this_node,next_node] = myinput[i,j+1]
		if i < n - 1:
			next_node = np.ravel_multi_index([[i+1],[j]], (n,n))[0]
			graph[this_node,next_node] = myinput[i+1,j]
		if j > 0:
			next_node = np.ravel_multi_index([[i],[j-1]], (n,n))[0]
			graph[this_node,next_node] = myinput[i,j-1]
		if i > 0:
			next_node = np.ravel_multi_index([[i-1],[j]], (n,n))[0]
			graph[this_node,next_node] = myinput[i-1,j]
res = scipy.sparse.csgraph.shortest_path(graph, directed=True)
print(res[0,n**2 - 1])
