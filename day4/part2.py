import os
import numpy as np

with open("input", "r") as infile:
	myinput = infile.read()

winning_nums = [23,91,18,32,73,14,20,4,10,55,40,29,13,25,48,65,2,80,22,16,93,85,66,21,9,36,47,72,88,58,5,42,53,69,52,8,54,63,76,12,6,99,35,95,82,49,41,17,62,34,51,77,94,7,28,71,92,74,46,79,26,19,97,86,87,37,57,64,1,30,11,96,70,44,83,0,56,90,59,78,61,98,89,43,3,84,67,38,68,27,81,39,15,50,60,24,45,75,33,31]
myinput = myinput.split("\n")[:-1]

myinput = [x.split() for x in myinput]
myinput = list(filter(lambda x: len(x) != 0, myinput))
for i in range(len(myinput)):
	myinput[i] = [int(x) for x in myinput[i]]

myinput = np.array(myinput).reshape((100, 5, 5))

winner = False
winners = np.zeros(myinput.shape[0])
lastwin = False
for num in winning_nums:
	for i in range(myinput.shape[0]):
		x, y = np.where(myinput[i] == num)
		for j in range(len(x)):
			myinput[i][x[j],y[j]] = 0
		rowsums = np.sum(myinput[i], axis = 1)
		columnsums = np.sum(myinput[i], axis = 0)
		if 0 in rowsums or 0 in columnsums:
			winners[i] = 1
		if np.sum(winners) == myinput.shape[0]:
			lastwinner = i
			lastwin = True
			lastnum = num
			break
	if lastwin:
		break
print(np.sum(myinput[lastwinner]) * lastnum)