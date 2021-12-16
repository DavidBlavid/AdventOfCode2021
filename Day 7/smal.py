
fl = open('Day 7/input.txt').readline()
pl = [int(x) for x in fl.strip().split(',')]

minf1, minf2 = [], []

for i in range(min(pl), max(pl) + 1):
    cf1 = cf2 = 0

    for p in [abs(x-i) for x in pl]:
        cf1 += p
        cf2 += p*(p+1)/2    # triangular numbers

    minf1 += [cf1]
    minf2 += [cf2]

print(min(minf1))
print(min(minf2))
