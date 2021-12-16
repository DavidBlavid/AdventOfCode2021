
minFuel1 = minFuel2 = 999999999999

positions = [int(x) for x in open('Day 7/input.txt').readline().strip().split(',')]

maxP = max(positions)
minP = min(positions)

def recSum(n): return n*(n+1)/2

for i in range(minP, maxP + 1):
    currentFuel1 = 0
    currentFuel2 = 0

    for p in positions:
        currentFuel1 += abs(p - i)
        currentFuel2 += recSum(abs(p - i))

    # print(i, currentFuel)

    minFuel1 = min(currentFuel1, minFuel1)
    minFuel2 = min(currentFuel2, minFuel2)

print(minFuel1)
print(minFuel2)
