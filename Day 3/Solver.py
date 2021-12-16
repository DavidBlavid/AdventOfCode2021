fl = open('Day 3/input.txt').readlines()
lg, ls = fl.copy(), fl.copy()
gr = 0

for i in range(12):

        gr += pow(2, 11-i) * (sum([int(x[i]) for x in fl]) > (len(fl) / 2))

        fg = str(int(sum([int(x[i]) for x in lg]) >= (len(lg) / 2.)))
        fs = str(int(sum([int(x[i]) for x in ls]) <  (len(ls) / 2.)))

        lg = list(filter(lambda x: x[i] == fg, lg)) if len(lg) > 1 else lg
        ls = list(filter(lambda x: x[i] == fs, ls)) if len(ls) > 1 else ls

print(gr * (pow(2, 12) - gr - 1))
print(int(lg[0], 2) * int(ls[0], 2))