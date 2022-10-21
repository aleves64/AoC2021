import numpy as np
import os

with open("input", "r") as infile:
	myinput = infile.read()

myinput = myinput.split("\n")[:-1]
myinput = [list(x) for x in myinput]
for i in range(len(myinput)):
	myinput[i] = [int(x) for x in myinput[i]]
myinput = np.array(myinput)

gamma_bits = []
epsilon_bits = []
for i in range(myinput.shape[1]):
	val = np.mean(myinput[:,i])
	bit = 0
	if val > 0.5:
		bit = 1
	gamma_bits.append(bit)
	epsilon_bits.append((bit - 1) * -1)
gamma = int(''.join([str(x) for x in gamma_bits]), base = 2)
epsilon = int(''.join([str(x) for x in epsilon_bits]), base = 2)
print(gamma*epsilon)