import numpy as np
import os

def most_common_bit(myinput, i):
	mean = np.mean(myinput[:,i])
	if mean >= 0.5:
		return 1
	return 0

def prune_vals(myinput, reverse=False):
	remaining = np.copy(myinput)
	for i in range(remaining.shape[1]):
		bit = most_common_bit(remaining, i)
		if reverse:
			bit = (bit - 1) * -1
		keep_these = []
		for j in range(remaining.shape[0]):
			if remaining[j][i] == bit:
				keep_these.append(j)
		remaining = remaining[keep_these]
		if len(remaining) == 1:
			remaining = remaining[0]
			break
	return remaining

with open("input", "r") as infile:
	myinput = infile.read()

myinput = myinput.split("\n")[:-1]
myinput = [list(x) for x in myinput]
for i in range(len(myinput)):
	myinput[i] = [int(x) for x in myinput[i]]
myinput = np.array(myinput)

oxy = prune_vals(myinput)
scrubs = prune_vals(myinput, reverse=True)

oxy = int(''.join([str(x) for x in oxy]), base=2)
scrubs = int(''.join([str(x) for x in scrubs]), base=2)

print(oxy*scrubs)