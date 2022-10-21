import os
import numpy as np

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput.split("\n")[:-1]

starts = ['(', '[', '{', '<']
ends = [')', ']', '}', '>']
scores = [3, 57, 1197, 25137]

acc = 0
for line in myinput:
	lastopen = 0
	stack = []
	for i in range(len(line)):
		print(stack)
		if line[i] in starts:
			lastopen = starts.index(line[i])
			stack.append(lastopen)
		elif line[i] in ends:
			lastclose = ends.index(line[i])
			if lastopen != lastclose:
				acc += scores[lastclose]
				print(f"expected {ends[lastopen]} but got {ends[lastclose]} at {i}")
				break
			else:
				stack.pop()
				if len(stack) == 0:
					break
				else:
					lastopen = stack[-1]