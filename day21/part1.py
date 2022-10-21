import os

with open("input", "r") as infile:
   myinput = infile.read()
myinput = [int(x.split(": ")[1]) for x in myinput.split("\n")[:-1]]

dice_vals = range(1,101)
rolls = 0

scores = [0,0]
positions_vals = range(1,11)
positions = [myinput[0],myinput[1]]

while True:
	roll = 3*(dice_vals[rolls % 100] + dice_vals[(rolls + 2) % 100])/2
	positions[0] = ((positions[0] + roll - 1) % 10) + 1
	scores[0] += positions[0]
	rolls += 3

	if scores[0] >= 1000:
		winner = scores[0]
		loser = scores[1]
		break

	roll = 3*(dice_vals[rolls % 100] + dice_vals[(rolls + 2) % 100])/2
	positions[1] = ((positions[1] + roll - 1) % 10) + 1
	scores[1] += positions[1]
	rolls += 3

	if scores[1] >= 1000:
		winner = scores[0]
		loser = scores[1]
		break

print(loser * rolls)