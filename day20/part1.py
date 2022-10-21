import os
import numpy as np

with open("input", "r") as infile:
   myinput = infile.read()

myinput = myinput.split("\n")[:-1]
img_filter = np.array(list(myinput[0]))
img_filter = [('0' if x == '.' else '1') for x in img_filter]
myinput = myinput[2:]
n_y = len(myinput)
n_x = len(myinput[0])
arr = np.full((n_y+4,n_x+4), '0')
for i in range(len(myinput)):
    myinput[i] = [('0' if x == '.' else '1') for x in myinput[i]]
arr[2:-2,2:-2] = np.array(myinput)

steps = 2

things = [int(img_filter[0]), int(img_filter[2**9 - 1])]
prev_thing = 0

for step in range(steps):
    n_x = arr.shape[1]
    n_y = arr.shape[0]

    next_arr = np.full((n_y+4,n_x+4), [img_filter[0], img_filter[2**9 - 1]][prev_thing])
    tmp = np.full((n_y, n_x), [img_filter[0], img_filter[2**9 - 1]][prev_thing])
    prev_thing = things[prev_thing]

    for x in range(1,n_x-1):
        for y in range(1,n_y-1):
            window = arr[y-1:y+2,x-1:x+2]
            dec = int(''.join(np.ndarray.flatten(window)), base=2)
            tmp[y,x] = img_filter[dec]
    next_arr[2:-2,2:-2] = tmp
    arr = next_arr

total = 0
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        res = int(arr[i,j])
        total += res
        c = ['.','#'][res]
        print(c,end='')
    print()
print(total)