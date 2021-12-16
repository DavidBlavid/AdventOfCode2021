ts = ''
rd, vd = {}, {}

def count_letters():     # print solutions to part 1 and 2

    ld = {}

    for r in rd:
        for l in r:
            if l not in ld: ld[l] = 0
            ld[l] += vd[r] / 2

    ld[ts[0]] += 0.5     # first letter only counted once
    ld[ts[-1]] += 0.5    #  last letter only counted once

    print(max(ld.values()) - min(ld.values()))


for ln in open('Day 14/input.txt').readlines():
    
    if ts == '': ts = ln[:-1]

    if '->' in ln:
        pair, insert = ln[:-1].split(' -> ')
        rd[pair] = (pair[0] + insert, insert + pair[1])
        vd[pair] = 0

for pos, c in enumerate(ts[:-1]):
    vd[c + ts[pos+1]] += 1          # get initial rule count

for i in range(41):
    if i in (10, 40): count_letters()

    next_vd = vd.copy()
                                    # calculate rule count
    for r in rd:                    # ex: CH (3) => CB (2), BH (0)
        next_vd[rd[r][0]] += vd[r]  # CB (2) --(+3)-> CB (5)
        next_vd[rd[r][1]] += vd[r]  # BH (0) --(+3)-> BH (3)
        next_vd[r] -= vd[r]         # CH (3) --(-3)-> CH (0)

    vd = next_vd.copy()