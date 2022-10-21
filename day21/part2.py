import os
from collections import deque

with open("input", "r") as infile:
   myinput = infile.read()
myinput = [int(x.split(": ")[1]) for x in myinput.split("\n")[:-1]]

position0 = myinput[0]
position1 = myinput[1]

wins = [0,0]

stack = deque()
stack.append((0, 0, position0, position1, 3, 1, 1))
stack.append((0, 0, position0, position1, 4, 3, 1))
stack.append((0, 0, position0, position1, 5, 6, 1))
stack.append((0, 0, position0, position1, 6, 7, 1))
stack.append((0, 0, position0, position1, 7, 6, 1))
stack.append((0, 0, position0, position1, 8, 3, 1))
stack.append((0, 0, position0, position1, 9, 1, 1))
while stack:
	score0, score1, position0, position1, roll, multiplier, player1_turn = stack.pop()
	if player1_turn:
		position0 += roll
		if position0 > 10:
			position0 -= 10
		score0 += position0
		if score0 >= 21:
			wins[0] += multiplier
			continue
	else:
		position1 += roll
		if position1 > 10:
			position1 -= 10
		score1 += position1
		if score1 >= 21:
			wins[1] += multiplier
			continue
	player1_turn = player1_turn^1
	stack.append((score0, score1, position0, position1, 3, multiplier*1, player1_turn))
	stack.append((score0, score1, position0, position1, 4, multiplier*3, player1_turn))
	stack.append((score0, score1, position0, position1, 5, multiplier*6, player1_turn))
	stack.append((score0, score1, position0, position1, 6, multiplier*7, player1_turn))
	stack.append((score0, score1, position0, position1, 7, multiplier*6, player1_turn))
	stack.append((score0, score1, position0, position1, 8, multiplier*3, player1_turn))
	stack.append((score0, score1, position0, position1, 9, multiplier*1, player1_turn))

if (wins[0] > wins[1]):
	print(wins[0])
else:
	print(wins[1])
