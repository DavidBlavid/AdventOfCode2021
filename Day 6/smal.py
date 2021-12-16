import numpy as np

fl = open('Day 6/input.txt').readline()
p = np.array([fl.count(str(x)) for x in range(9)])

m = np.zeros((9, 9))
m[0, 6] = m[0, 8] = 1
for i in range(8): m[i + 1, i] = 1

for i in range(257): 
    if i in (80, 256): print(sum(p))
    p @= m
