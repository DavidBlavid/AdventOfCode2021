import numpy as np

floor = []
count1 = 0

def lowCheck(x, y):

    coords = False
    currentHeight = floor[y][x]

    if x > 0 and floor[y][x-1] < currentHeight:
        coords = (x-1, y)

    if x < (len(floor[y])-1) and floor[y][x+1] < currentHeight:
        coords = (x+1, y)

    if y > 0 and floor[y-1][x] < currentHeight:
        coords = (x, y-1)

    if y < (len(floor)-1) and floor[y+1][x] < currentHeight:
        coords = (x, y+1)

    return coords

def recBasinCheck(x, y):

    #print('recBasinCheck:', x, y, floor[y][x])

    if floor[y][x] != 9:
        next = lowCheck(x, y)
        #print(next)

        if not next:    # found basin
            #print('found basin!')
            basinMap[y][x] += 1
        else:
            #print('starting recursion')
            recBasinCheck(next[0], next[1])

for ln in open('Day 9/input.txt').readlines():
    floor.append([int(x) for x in ln[:-1]])

floor = np.array(floor)
basinMap = np.zeros_like(floor)

for yp, y in enumerate(floor):
    for xp, x in enumerate(y):
        recBasinCheck(xp, yp)
        if basinMap[yp, xp]:
            print(x, y, basinMap[y][x])
            count1 += (x+1)

print(count1)

bsMapSorted = np.sort(basinMap, axis=None)[::-1]

print((bsMapSorted > 0).sum())

print(bsMapSorted)
print(bsMapSorted[0], bsMapSorted[1], bsMapSorted[2])
print(bsMapSorted[0] * bsMapSorted[1] * bsMapSorted[2])




print('gotem')
