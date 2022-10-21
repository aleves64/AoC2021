import numpy as np
import os

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput.split("\n")[:-1]
vals = np.array([int(x) for x in myinput])

i = 3
prevval = np.inf
n = 0
while i < vals.shape[0]:
	if vals[i] > vals[i - 3]:
		n += 1
	i += 1
print(n)