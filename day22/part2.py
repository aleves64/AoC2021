import os

with open("input", "r") as infile:
   myinput = infile.read()
myinput = myinput.split("\n")[:-1]

commands = []
for command in myinput:
    action = 1 if command[:2] == "on" else 0
    command = command.split("=")
    x = [int(x) for x in command[1][:-2].split("..")]
    y = [int(x) for x in command[2][:-2].split("..")]
    z = [int(x) for x in command[3].split("..")]
    commands.append((action, x, y, z))

regions = []
for command in commands:
    action, x, y, z = command

    if action == 1:
        tmp_regions = []
        for region in regions:
            factor, a, b, c = region
            if (x[1] >= a[0]) and (x[0] <= a[1]) and (y[1] >= b[0]) and (y[0] <= b[1]) and (z[1] >= c[0]) and (z[0] <= c[1]):
                tmp_regions.append((-1*factor, [max(a[0],x[0]), min(a[1],x[1])],[max(b[0],y[0]), min(b[1],y[1])],[max(c[0],z[0]), min(c[1],z[1])]))
        regions.append((1, x,y,z))
        regions.extend(tmp_regions)
    else:
        tmp_regions = []
        for region in regions:
            factor, a, b, c = region
            if (x[1] >= a[0]) and (x[0] <= a[1]) and (y[1] >= b[0]) and (y[0] <= b[1]) and (z[1] >= c[0]) and (z[0] <= c[1]):
                tmp_regions.append((-1*factor, [max(a[0],x[0]), min(a[1],x[1])],[max(b[0],y[0]), min(b[1],y[1])],[max(c[0],z[0]), min(c[1],z[1])]))
        regions.extend(tmp_regions)

volume = 0
for region in regions:
    factor, x, y, z = region
    volume += factor * ((x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1))
print(volume)