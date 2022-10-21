import os
import numpy as np

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput[:-1].split("\n")
invals = []
outvals = []
for i in range(len(myinput)):
	vals = myinput[i].split("|")
	inval = vals[0].split()
	outval = vals[1].split()
	invals.append(inval)
	outvals.append(outval)


################## GET ALL THE PERMUTATIONS #########################
perms = []
nums = np.arange(7)
hit_end = False
while not hit_end:
	perms.append(np.copy(nums))
	decrease = nums.shape[0] - 2
	while nums[decrease] > nums[decrease + 1] and decrease >= 0:
		if (decrease == 0):
			hit_end = True
		decrease -= 1
	if not hit_end:
		larger = nums.shape[0] - 1
		while nums[larger] < nums[decrease]:
			larger -= 1
		tmp = nums[larger]
		nums[larger] = nums[decrease]
		nums[decrease] = tmp
		decrease += 1
		nums[decrease:] = np.flip(nums[decrease:])
############## Array with valid digts ###################
digits = np.array(
	[[1,1,1,0,1,1,1],
	 [0,0,1,0,0,1,0],
	 [1,0,1,1,1,0,1],
	 [1,0,1,1,0,1,1],
	 [0,1,1,1,0,1,0],
	 [1,1,0,1,0,1,1],
	 [1,1,0,1,1,1,1],
	 [1,0,1,0,0,1,0],
	 [1,1,1,1,1,1,1],
	 [1,1,1,1,0,1,1]]
)
############ Get the keys ########################
keys = np.zeros((len(invals), 7), dtype=np.uint8)
for i in range(len(invals)):
	print(f"{i+1} of 200")
	for perm in perms:
		all_valid = True
		for j in range(len(invals[i])):
			pattern = np.zeros(7, dtype=np.uint8)
			for k in range(len(invals[i][j])):
				c = ord(invals[i][j][k]) - ord('a')
				transformed_c = perm[c]
				pattern[transformed_c] = 1
			if not any((digits[:] == pattern).all(1)):
				all_valid = False
				break
		if all_valid == True:
			keys[i] = perm
############# Get the output vals ####################
real_outvals = []
for i in range(len(outvals)):
	outval = []
	for j in range(len(outvals[i])):
		pattern = np.zeros(7, dtype=np.uint8)
		for k in range(len(outvals[i][j])):
			c = ord(outvals[i][j][k]) - ord('a')
			transformed_c = keys[i][c]
			pattern[transformed_c] = 1
		digit = np.where((digits == pattern).all(axis=1))[0][0]
		outval.append(str(digit))
	outval = int(''.join(outval))
	real_outvals.append(outval)
##################### sum them all #####################
print(np.sum(real_outvals))