import numpy as np
import re

def cmp(a, b): return (a > b) - (a < b) # cmp from python 2

m1, m2 = np.zeros((1000, 1000)), np.zeros((1000, 1000))
    
for line in open('Day 5/input.txt').readlines():
    v = [int(x) for x in re.split(r'\D+', line)[:-1]]

    xs = cmp(v[2], v[0])                # calculate x step
    ys = cmp(v[3], v[1])                # calculate y step
    
    if xs == 0 or ys == 0 or abs(xs) == abs(ys):

        while True:
            if xs == 0 or ys == 0:  m1[v[1]][v[0]] += 1
            m2[v[1]][v[0]] += 1

            if v[0] == v[2] and v[1] == v[3]: break

            v[0] += xs                  # update x pos
            v[1] += ys                  # update y pos

print(len(np.where(m1 > 1)[0]))
print(len(np.where(m2 > 1)[0]))
