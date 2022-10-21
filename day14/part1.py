import os
import numpy as np

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput.split("\n")[:-1]
state = myinput[0]
instructions = {}
for i in range(2, len(myinput)):
	key, val = myinput[i].split(" -> ")
	instructions[key] = val

steps = 10
for i in range(steps):
	new_state = state[0]
	for i in range(1, len(state)):
		key = state[i-1:i+1]
		if key in instructions:
			new_state += instructions[key]
		new_state += state[i]
	state = new_state
state = list(state)
unique, counts = np.unique(state, return_counts=True)
print(np.max(counts) - np.min(counts))