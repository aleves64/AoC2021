import os
import numpy as np
from itertools import permutations
from itertools import product

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput[:-1].split("\n\n")

scanners = {}
for i in range(len(myinput)):
	myinput[i] = myinput[i].split("\n")[1:]
	for j in range(len(myinput[i])):
		myinput[i][j] = [int(x) for x in myinput[i][j].split(",")]
	myinput[i] = np.array(myinput[i])

n_dimensions = 3
xyz_signs = np.array(list(product([1,-1], [1,-1], [1,-1])))
xyz_perms = np.array(list(permutations(range(n_dimensions))), dtype=np.uint32)

def shared_beacons(sensor0, sensor1):
	for beacon0 in sensor0:
		for beacon1 in sensor1:
			offset = beacon0 - beacon1
			sensor1_offset = sensor1 + offset
			n_shared = 0
			for beacon in sensor1_offset:
				n_shared += np.where((sensor0 == beacon).all(axis = 1))[0].shape[0]
				if n_shared >= 12:
					return True, offset
	return False, None

rotated = np.zeros(len(myinput))
comparisons = {}
offsets = [[0,0,0]]
rotated[0] = 1
while 0 in rotated:
	for i in range(len(myinput)):
		for j in range(i + 1, len(myinput)):
			if ((i,j) in comparisons) or (rotated[i] == 0 and rotated[j] == 0):
				continue
			if rotated[i] == 0 or rotated[j] == 0:
				print(f"Comparing {i} and {j}...")
				comparisons[(i,j)] = 1
				if rotated[j] == 0:
					a = myinput[i]
					b = myinput[j]
				else:
					a = myinput[j]
					b = myinput[i]
				for xyz_perm in xyz_perms:
					for xyz_sign in xyz_signs:
						tmp = b[:,xyz_perm] * xyz_sign
						overlap, offset = shared_beacons(a, tmp)
						if overlap:
							print(f"Offset between {i} and {j}: {offset}")
							offsets.append(offset)
							if rotated[j] == 0:
								myinput[j] = tmp + offset
								rotated[j] = 1
							else:
								myinput[i] = tmp + offset
								rotated[i] = 1
							break
					if overlap:
						break

beacons = []
for i in range(len(myinput)):
	beacons.extend([tuple(x) for x in myinput[i]])
beacons = set(beacons)
print(len(beacons))

maxdist = 0
for i in range(len(offsets)):
	for j in range(len(offsets)):
		if i == j:
			continue
		dist = np.linalg.norm(offsets[i] - offsets[j], ord = 1)
		if dist > maxdist:
			maxdist = dist
print(maxdist)