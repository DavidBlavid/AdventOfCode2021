import numpy as np

coords = []
folds = []

for ln in open('Day 13/input.txt').readlines():

    if ',' in ln:
        x, y = ln[:-1].split(',')
        coords.append((int(x), int(y)))

    if '=' in ln:
        fold, pos = ln[:-1].split('=')
        folds.append((fold[-1], int(pos)))

maxVals = np.max(coords, 0)
paper = np.zeros((maxVals[1] + 1, maxVals[0] + 1))

for c in coords:
    paper[c[1], c[0]] = 1

for i, f in enumerate(folds):

    foldAxis = f[0]
    foldLine = f[1]

    if foldAxis == 'x': # fold along x

        for yp, y in enumerate(paper):
            for xp, x in enumerate(y):

                if xp > foldLine and x:   # point gets folded
                    foldDistance = xp - foldLine
                    paper[yp, foldLine - foldDistance] = paper[yp, xp]

        paper = paper[:,:foldLine]


    else:               # fold along y

        for yp, y in enumerate(paper):
            for xp, x in enumerate(y):

                if yp > foldLine and x:   # point gets folded
                    foldDistance = yp - foldLine
                    paper[foldLine - foldDistance, xp] = paper[yp, xp]

        paper = paper[:foldLine, :]

    if i == 0:
        print(np.count_nonzero(paper > 0), '\n-----')

for y in range(len(paper)):
    for x in range(len(paper[0])):
        printChar = '##' if paper[y, x] else '  '
        print(printChar, sep = '', end = '')
    print()
