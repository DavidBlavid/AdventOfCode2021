import numpy as np

co, fo = [], []

for ln in open('Day 13/input.txt').readlines():
    if ',' in ln:
        x, y = ln[:-1].split(',')       # get coordinates
        co.append((int(x), int(y)))     

    if '=' in ln:
        fold, pos = ln[:-1].split('=')  # get folds
        fo.append((fold[-1] == 'y', int(pos)))

paper = np.zeros((np.max(co, 0)[1] + 1, np.max(co, 0)[0] + 1))
for c in co: paper[c[1], c[0]] = 1      # initialize paper

for i, f in enumerate(fo):              # go through all folds

    for yp, y in enumerate(paper):      
        for xp, x in enumerate(y):

            if f[0]:                    # fold along y
                if yp > f[1] and x:
                    paper[f[1] - (yp - f[1]), xp] = 1

            else:                       # fold along x
                if xp > f[1] and x:
                    paper[yp, f[1] - (xp - f[1])] = 1

    if f[0]: paper = paper[:f[1], :]    # remove folded halve (y)
    else:    paper = paper[:, :f[1]]    # remove folded halve (x)

    if i == 0: print(np.sum(paper > 0)) # print part 1

for y in range(len(paper)):
    for x in range(len(paper[y])):      # print part 2
        print('##' if paper[y, x] else '  ', end = '')
    print()
