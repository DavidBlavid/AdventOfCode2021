import numpy as np

f, c1= [], 0

def lowP(x, y):                       # find adjacent low points
    co, ch = False, f[y][x]

    if x > 0 and f[y][x-1] < ch:             co = (x-1, y)
    if x < (len(f[y])-1) and f[y][x+1] < ch: co = (x+1, y)
    if y > 0 and f[y-1][x] < ch:             co = (x, y-1)
    if y < (len(f)-1) and f[y+1][x] < ch:    co = (x, y+1)

    return co                         # return False or coords

def recB(x, y):                       # recursively find basins
    if f[y][x] != 9:
        co = lowP(x, y)

        if co: recB(co[0], co[1])
        else:  bsm[y][x] += 1

for ln in open('Day 9/input.txt').readlines():
    f.append([int(x) for x in ln[:-1]])

bsm = np.zeros_like(f)                # basin size map

for yp, y in enumerate(f):
    for xp, x in enumerate(y):
        recB(xp, yp)
        c1 += (x+1) * (bsm[yp, xp] > 0)

print(c1)
print(np.prod(np.sort(bsm, axis=None)[-1:-4:-1]))