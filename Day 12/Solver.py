pathDict = {}
counter1 = 0

for ln in open('Day 12/input.txt').readlines():
    entries = ln[:-1].split('-')

    if entries[0] in pathDict:
        pathDict[entries[0]] += [entries[1]]
    else:
        pathDict[entries[0]]  = [entries[1]]
        

    if entries[1] in pathDict:
        pathDict[entries[1]] += [entries[0]]
    else:
        pathDict[entries[1]]  = [entries[0]]



def recSearch1(position, visited):

    if position == 'end':
        print(visited + ['end'])
        return 1

    visitedCurrent = visited.copy()
    visitedCurrent += [position]

    foundPaths = 0

    if position in pathDict:

        paths = pathDict[position].copy()

        for vc in visitedCurrent:  # remove visited small caves

            if vc.islower() and vc in paths:

                paths.remove(vc)

        for p in paths:

            foundPaths += recSearch1(p, visitedCurrent)

        return foundPaths

    else:

        return 0

def recSearch2(position, visited, smallvisit):

    if position == 'end':
        #print(visited + ['end'])
        return 1

    visitedCurrent = visited.copy()
    visitedCurrent += [position]

    foundPaths = 0

    if position in pathDict:

        paths = pathDict[position].copy()

        for vc in visitedCurrent:  # remove visited small caves

            if vc.islower() and vc in paths and smallvisit:
                paths.remove(vc)

            if vc == 'start' and vc in paths:
                paths.remove(vc)

        for p in paths:

            if not smallvisit and p.islower() and p in visitedCurrent:

                foundPaths += recSearch2(p, visitedCurrent, True)

            else:

                foundPaths += recSearch2(p, visitedCurrent, smallvisit)

        return foundPaths

    else:

        return 0

print(pathDict)

print(recSearch2('start', [], True))
print(recSearch2('start', [], False))

print(counter1)
