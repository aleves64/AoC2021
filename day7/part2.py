import os
import numpy as np

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput[:-1].split(",")
for i in range(len(myinput)):
	myinput[i] = int(myinput[i])

myinput = np.array(myinput)
n = myinput.shape[0]
p = np.round((np.sum(myinput) + (1/2) * n) / n) - 1
tmp = np.abs(myinput - p)
totalfuel = np.sum((tmp + tmp**2) / 2)
print(totalfuel)