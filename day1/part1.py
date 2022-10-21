import numpy as np
import os

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput.split("\n")
prevval = np.inf
n = 0
for line in myinput:
	try:
		val = int(line)
	except:
		continue
	val = int(line)
	if val > prevval:
		n += 1
	prevval = val
print(n)