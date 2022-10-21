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
		if not node in visited_smalls:
			visited_smalls[node] = 1
		else:
			visited_smalls[node] += 1
	if node == "end":
		paths.append(visited)
	else:
		for nextnode in graph[node]:
			if not nextnode in visited_smalls or visited_smalls[nextnode] < 2:
				dfs(nextnode, visited[:], deepcopy(visited_smalls))

middle_nodes = []
for key in graph.keys():
	if key != "start" and key != "end":
		middle_nodes.append(key)
for i in range(len(middle_nodes)):
	dic = {}
	dic["start"] = 2
	for key in middle_nodes:
		dic[key] = 1
	dic[middle_nodes[i]] = 0
	dfs("start", [], dic)

print(len(set(tuple(x) for x in paths)))