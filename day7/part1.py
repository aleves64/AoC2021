import os
import numpy as np

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput[:-1].split(",")
for i in range(len(myinput)):
	myinput[i] = int(myinput[i])

myinput = np.array(myinput)
minfuel = np.inf
for i in range(np.max(myinput)):
	totalfuel = np.sum(np.abs(myinput - i))
	if totalfuel < minfuel:
		minfuel = totalfuel
print(minfuel)