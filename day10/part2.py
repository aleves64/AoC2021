import os
import numpy as np

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput.split("\n")[:-1]

starts = ['(', '[', '{', '<']
ends = [')', ']', '}', '>']

acc = 0
incompletes = []
incomplete_stacks = []
for line in myinput:
	lastopen = 0
	stack = []
	for i in range(len(line)):
		if line[i] in starts:
			lastopen = starts.index(line[i])
			stack.append(lastopen)
		elif line[i] in ends:
			lastclose = ends.index(line[i])
			if lastopen != lastclose:
				break
			else:
				stack.pop()
				if len(stack) != 0:
					lastopen = stack[-1]
	if i == len(line) - 1 and len(stack) != 0:
		incompletes.append(line)
		incomplete_stacks.append(stack)

scores = []
for i in range(len(incompletes)):
	score = 0
	while len(incomplete_stacks[i]) != 0:
		val = (incomplete_stacks[i].pop() + 1)
		score *= 5
		score += val
	scores.append(score)
sorted_scores = sorted(scores)
middle_score = sorted_scores[int(len(sorted_scores) / 2)]
print(middle_score)