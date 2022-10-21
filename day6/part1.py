import os
import numpy as np

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput[:-1].split(",")
for i in range(len(myinput)):
	myinput[i] = int(myinput[i])

fish = myinput
days = 80
for i in range(days):
	fishes = len(fish)
	for j in range(fishes):
		if fish[j] == 0:
			fish[j] = 6
			fish.append(8)
		else:
			fish[j] -= 1
print(len(fish))