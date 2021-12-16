import numpy as np
import re

map = np.zeros((1000, 1000))
    
for line in open('Day 5/input.txt').readlines():

    print('---')
    vals = [int(x) for x in re.split(r'\D+', line)[:-1]]

    print(vals)

    if vals[0] == vals[2] or vals[1] == vals[3]:

        #print('checking')

        xmin = min(vals[0], vals[2])
        xmax = max(vals[0], vals[2])

        ymin = min(vals[1], vals[3])
        ymax = max(vals[1], vals[3])

        #print(xmin, xmax, ymin, ymax)

        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):

                #print(x, y)
                map[y][x] = map[y][x] + 1

    # diagonal walking
    if abs(vals[0] - vals[2]) == abs(vals[1] - vals[3]):

        xstep = 1 if vals[0] < vals[2] else -1
        ystep = 1 if vals[1] < vals[3] else -1

        x = vals[0]
        y = vals[1]

        while x != vals[2]:

            map[y][x] = map[y][x] + 1
            x += xstep
            y += ystep

        map[y][x] = map[y][x] + 1

    
print(map)

print(len(np.where(map > 1)[0]))
