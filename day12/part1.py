import os
import numpy as np
from collections import deque
from copy import deepcopy

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput.split("\n")[:-1]
graph = {}
for i in range(len(myinput)):
	key,val = myinput[i].split("-")
	if not key in graph:
		graph[key] = []
	if not val in graph:
		graph[val] = []
	graph[key].append(val)
	graph[val].append(key)

paths = []
def dfs(node, visited, visited_smalls):
	visited.append(node)
	if node.islower():
		visited_smalls[node] = 1
	if node == "end":
		paths.append(visited)
	else:
		for nextnode in graph[node]:
			if not nextnode in visited_smalls:
				dfs(nextnode, visited[:], deepcopy(visited_smalls))
dfs("start", [], {})

print(len(paths))