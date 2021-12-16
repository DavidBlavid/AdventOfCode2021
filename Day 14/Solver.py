import string
import math

template = ''
rules = {}
values = {}

for ln in open('Day 14/dummy.txt').readlines():
    
    if template == '': template = ln[:-1]

    if '->' in ln:
        pair, insert = ln[:-1].split(' -> ')
        rules[pair] = (pair[0] + insert, insert + pair[1])
        values[pair] = 0

print(template, rules)

for pos, c in enumerate(template[:-1]):
    values[c + template[pos+1]] += 1

print(template)
print(rules)
print(values)

for i in range(40):

    nextValues = values.copy()

    for r in rules:
        next1, next2 = rules[r]
        #print(str(r) + ' -' + str(values[r]) + '->', next1, next2)
        nextValues[next1] += values[r]
        nextValues[next2] += values[r]
        nextValues[r] -= values[r]

    #print(nextValues)

    values = nextValues.copy()

print(sum(values.values()) + 1)

letterCount = {}

# count num of letters
for r in rules:
    l1 = r[0]
    l2 = r[1]

    if l1 not in letterCount: letterCount[l1] = 0
    if l2 not in letterCount: letterCount[l2] = 0

    letterCount[l1] += values[r] / 2
    letterCount[l2] += values[r] / 2

letterCount[template[0]] += 0.5
letterCount[template[-1]] += 0.5

print(letterCount)

print(min(letterCount.values()), max(letterCount.values()))
print(max(letterCount.values()) - min(letterCount.values()))