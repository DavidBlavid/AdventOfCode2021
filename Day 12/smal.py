pathDict = {}

for ln in open('Day 12/input.txt').readlines():
    c1, c2 = ln[:-1].split('-')

    if c1 not in pathDict: pathDict[c1] = []
    if c2 not in pathDict: pathDict[c2] = []
    
    pathDict[c1] += [c2] if c2 != 'start' else []
    pathDict[c2] += [c1] if c1 != 'start' else []

def recSearch(vis, small):

    paths = pathDict[vis[-1]].copy()    # paths from current cave
    found = 0                           # paths of current branch

    if vis[-1] == 'end': return 1       # found end? paths +1

    for vc in vis:

        if (vc.islower() and not small) and vc in paths:
            paths.remove(vc)            # remove visited small caves

    for p in paths:                     # go recursively to all paths
        if small and p.islower() and p in vis:
            found += recSearch(vis + [p], False)    # visit small cave 2x

        else:
            found += recSearch(vis + [p], small)

    return found                        # return paths of branch

print(recSearch(['start'], False))      #  no small cave revisit allowed
print(recSearch(['start'], True))       # one small cave revisit allowed