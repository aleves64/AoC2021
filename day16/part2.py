import os
from math import prod

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
def parse(i):
	version = int(transmission[i:i+3],base=2)
	i += 3
	type_id = int(transmission[i:i+3],base=2)
	i += 3
	if type_id == 4:
		val, i = parse_literal(i)
		return val, i
	else:
		length_type = int(transmission[i],base=2)
		i += 1
		operations = [
			sum,
			prod,
			min,
			max,
			None,
			lambda x : x[0] > x[1],
			lambda x : x[0] < x[1],
			lambda x : x[0] == x[1]
		]
		operation = operations[type_id]
		response_vals = []
		if length_type == 0:
			length = int(transmission[i:i+15], base=2)
			i += 15
			target = i + length
			while i < target:
				val, i = parse(i)
				response_vals.append(val)
		else:
			length = int(transmission[i:i+11], base=2)
			i += 11
			j = 0
			target = length
			while j < target:
				val, i = parse(i)
				response_vals.append(val)
				j += 1
		out_val = operation(response_vals)
		return out_val, i
res = parse(0)
print(res[0])