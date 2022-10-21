import os
import numpy as np
from itertools import product

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput.split("\n")[:-1]
instructions = {}
empty_state = {}
count = {}
for c in alphabet:
	count[c] = 0
for pair in product(alphabet, alphabet):
	empty_state[pair] = 0
state = dict(empty_state)
for i in range(1, len(myinput[0])):
	pair = tuple(myinput[0][i - 1:i + 1])
	state[pair] += 1
	count[myinput[0][i]] += 1
count[myinput[0][0]] += 1
for i in range(2, len(myinput)):
	key, val = myinput[i].split(" -> ")
	instructions[tuple(key)] = val

steps = 40
for i in range(steps):
	new_state = dict(empty_state)
	for inst in instructions.keys():
		if inst in state:
			c0 = inst[0]
			c1 = inst[1]
			res = instructions[inst]
			if state[inst] > 0:
				new_state[(c0, res)] += state[inst]
				new_state[(res, c1)] += state[inst]
				count[res] += state[inst]
	state = new_state
counts = np.array(list(count.values()))
counts = counts[counts != 0]
print(np.max(counts) - np.min(counts))