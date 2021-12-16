from math import prod

data = 'F' + open('Day 16/input.txt').readline()[:-1]

print(data[1:])

res = "{0:08b}".format(int(data, 16))
res = res[4:]

print(res)
print(len(res))

counter1 = 0

def readPacketRec(packet, pos, depth):

    version = int(packet[pos:pos+3], 2)
    type_id = int(packet[pos+3:pos+6], 2)

    global counter1
    counter1 += version

    packetLength = 6

    if type_id == 4:           # contains value

        numberString = ''

        for numberPos in range(pos+6, len(packet), 5):
            numberString += packet[numberPos+1:numberPos+5]

            packetLength += 5
            
            if packet[numberPos] == '0': break
            
        value = int(numberString, 2)

        print(' ' * depth + ' ◎ ' + str(value))

        return value, packetLength

    else:                   # operation

        i = int(packet[pos+6])

        packetLength += 1

        subPacketValues = []

        if i == 0:          # next 15 bits give total length of subpackets

            packetLength += 15
            length = int(packet[pos+7:pos+22], 2)

            subPacketPos = 0

            while subPacketPos < length:

                temp1, temp2 = readPacketRec(packet, pos + packetLength + subPacketPos, depth + 1)
                subPacketValues += [temp1]
                subPacketPos += temp2

            packetLength += length

        else:               # next 11 bits give number of sub packets

            packetLength += 11
            length = int(packet[pos+7:pos+18], 2)

            subPacketPos = 0

            for i in range(length):
                temp1, temp2 = readPacketRec(packet, pos + packetLength + subPacketPos, depth + 1)
                subPacketValues += [temp1]
                subPacketPos += temp2

            packetLength += subPacketPos

        packetValue = 0

        if type_id == 0:

            packetValue = sum(subPacketValues)

            print(' ' * depth + ' +', subPacketValues)

        elif type_id == 1:

            packetValue = prod(subPacketValues)

            print(' ' * depth + ' *', subPacketValues)

        elif type_id == 2:

            packetValue = min(subPacketValues)
            print(' ' * depth + ' min', subPacketValues)

        elif type_id == 3:

            packetValue = max(subPacketValues)
            print(' ' * depth + ' max', subPacketValues)
        elif type_id == 5:

            packetValue = int(subPacketValues[0] > subPacketValues[1])
            print(' ' * depth + ' >', subPacketValues)

        elif type_id == 6:

            packetValue = int(subPacketValues[0] < subPacketValues[1])
            print(' ' * depth + ' <', subPacketValues)

        elif type_id == 7:

            packetValue = int(subPacketValues[0] == subPacketValues[1])
            print(' ' * depth + ' =', subPacketValues)

        if subPacketValues == 64925962533:
            print('found ya!')

        print(' ' * (depth-1) + ' ▣ ' , packetValue)

        return packetValue, packetLength

print(readPacketRec(res, 0, 0))
print(counter1)