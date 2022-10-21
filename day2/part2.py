import os

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput.split("\n")[:-1]
myinput = [x.split(' ') for x in myinput]
x = 0
y = 0
aim = 0
for k in range(len(myinput)):
	delta = int(myinput[k][1])
	if myinput[k][0] == "forward":
		y += aim * delta
		x += delta
	elif myinput[k][0] == "down":
		aim += delta
	elif myinput[k][0] == "up":
		aim -= delta
print(x*y)