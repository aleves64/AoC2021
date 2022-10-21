import os
import numpy as np

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput[:-1].split(",")
for i in range(len(myinput)):
	myinput[i] = int(myinput[i])

fishdays = np.zeros(9)
for i in range(len(myinput)):
	fishdays[myinput[i]] += 1

days = 256
for i in range(days):
	day0 = fishdays[0]
	for i in range(fishdays.shape[0] - 1):
		fishdays[i] = fishdays[i + 1]
	fishdays[8] = day0
	fishdays[6] += day0
print(np.sum(fishdays))