#read from input
inp = open("Day 1/input.txt", "r")
ni = inp.readlines()
inp.close()

#convert to int
for p, i in enumerate(ni):
    ni[p] = int(i[:-1])

#solve part 1
def part1(ni):
    
    print(incSum(ni))

#solve part 2
def part2(ni):

    s1 = s2 = s3 = 0
    sa = []

    for p, n in enumerate(ni):
        
        if p%3 == 0:
            sa += [s1]
            s1, s2, s3 = n, s2 + n, s3 + n

        elif p%3 == 1:
            sa += [s2]
            s1, s2, s3 = s1 + n, n, s3 + n

        elif p%3 == 2:
            sa += [s3]
            s1, s2, s3 = s1 + n, s2 + n, n

    print(incSum(sa[3:] + [max(s1, s2, s3)]))

def incSum(la):
    l1 = l2 = lc = 0
    for l in la:
        l2, l1 = l1, l
        lc += (l1 > l2)
    return lc - 1


#execute
part1(ni)
part2(ni)