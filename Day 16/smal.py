from math import prod

data = 'F' + open('Day 16/input.txt').readline()[:-1]
data = "{0:08b}".format(int(data, 16))[4:]
c1 = 0

def readPacket(p):      # takes binary string with
                        # current packet at front
    version = int(p[:3], 2)
    id = int(p[3:6], 2)

    pl = 6              # length of current Packet

    global c1
    c1 += version       # count version numbers

    if id == 4:         # read literal value
        bv = ''         # build binary string of value

        for pos in range(6, len(p), 5):
            bv += p[pos+1:pos+5]
            pl += 5
            
            if p[pos] == '0': break

        return int(bv, 2), pl

    else:               # operation

        spv = []
        spp = 0

        pl += 12 if int(p[6]) else 16

        if int(p[6]):   # sub packets
            for i in range(int(p[7:18], 2)):
                t1, t2 = readPacket(p[pl + spp:])
                spv += [t1]
                spp += t2

        else:           # sub packet length
            while spp < int(p[7:22], 2):
                t1, t2 = readPacket(p[pl + spp:])
                spv += [t1]
                spp += t2

        if   id == 0: pv = sum(spv)
        elif id == 1: pv = prod(spv)
        elif id == 2: pv = min(spv)
        elif id == 3: pv = max(spv)
        elif id == 5: pv = int(spv[0] > spv[1])
        elif id == 6: pv = int(spv[0] < spv[1])
        elif id == 7: pv = int(spv[0] == spv[1])

        return pv, pl + spp

print(readPacket(data)[0])    # part 2      <- reverse order!
print(c1)                     # part 1