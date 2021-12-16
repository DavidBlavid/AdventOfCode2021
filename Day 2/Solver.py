xp = yp = ad = ya = 0
for l in open('Day 2/input.txt').readlines():

    if l[0] == 'f':
        xp, ya = xp + int(l[-2]), ya + ad * int(l[-2])

    else:
        d = int(l[-2]) if (l[0] == 'd') else -int(l[-2])
        yp, ad = yp + d, ad + d

print(xp * yp)
print(xp * ya)
