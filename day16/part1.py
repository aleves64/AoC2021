import os
import numpy as np

with open("input", "r") as infile:
	myinput = infile.read()
myinput = myinput[:-1]
transmission = ""
for c in myinput:
	transmission += format(int(c,base=16), '04b')

def parse_literal(i):
	packet = int(transmission[i:i+5],base=2)
	i += 5
	val = packet & 0b1111
	while packet & 0b10000:
		packet = int(transmission[i:i+5],base = 2)
		i += 5
		val = (val << 4) | (packet & 0b1111)
	return val, i
def parse(i, version_sum):
	version = int(transmission[i:i+3],base=2)
	version_sum += version
	i += 3
	type_id = int(transmission[i:i+3],base=2)
	i += 3
	if type_id == 4:
		val, i = parse_literal(i)
		return val, i, version_sum
	else:
		length_type = int(transmission[i],base=2)
		i += 1
		if length_type == 0:
			length = int(transmission[i:i+15], base=2)
			i += 15
			target = i + length
			while i < target:
				val, i, version_sub = parse(i,0)
				version_sum += version_sub
		else:
			length = int(transmission[i:i+11], base=2)
			i += 11
			j = 0
			target = length
			while j < target:
				val, i, version_sub = parse(i,0)
				version_sum += version_sub
				j += 1
		return val, i, version_sum
res = parse(0,0)
print(res[2])