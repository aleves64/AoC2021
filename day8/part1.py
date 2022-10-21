import os
import numpy as np

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput[:-1].split("\n")
invals = []
outvals = []
for i in range(len(myinput)):
	vals = myinput[i].split("|")
	inval = vals[0].split()
	outval = vals[1].split()
	invals.append(inval)
	outvals.append(outval)

acc = 0
for i in range(len(outvals)):
	for j in range(len(outvals[0])):
		n = len(outvals[i][j])
		if n == 2 or n == 4 or n == 3 or n == 7:
			acc += 1
print(acc)