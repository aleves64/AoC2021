import numpy as np
import os

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput.split("\n")[:-1]
myinput = [x.split(' ') for x in myinput]
x_moves = np.zeros(len(myinput))
y_moves = np.zeros(len(myinput))
x_i = 0
y_i = 0
for k in range(len(myinput)):
	if myinput[k][0] == "forward":
		x_moves[x_i] = int(myinput[k][1])
		x_i += 1
	elif myinput[k][0] == "down":
		y_moves[y_i] = int(myinput[k][1])
		y_i += 1
	elif myinput[k][0] == "up":
		y_moves[y_i] = -int(myinput[k][1])
		y_i += 1
x = np.sum(x_moves)
y = np.sum(y_moves)
print(x*y)