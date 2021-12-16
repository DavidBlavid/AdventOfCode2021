import numpy as np

config = open('Day 6/input.txt').readline()
print(config)

iterations = 256

population = np.array([config.count(str(x)) for x in range(9)])

matrix = np.zeros((9, 9))
matrix[0, 6] = matrix[0, 8] = 1
for i in range(8):
    matrix[i + 1, i] = 1

print(matrix)
print(population)

print(population@matrix)

for i in range(iterations):

    print(i, np.sum(population))
    population = population@matrix

print(np.sum(population))

