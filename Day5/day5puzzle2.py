f = open("input.txt", "r")

lines = f.readlines()
seatIdsFound = []
mySeatid = []


def getPosition(min, max, lower, upper, seats):
    for seat in seats:
        if seat == lower:
            max = min + int((max-min)/2)
        elif seat == upper:
            min = min + int((max-min+1)/2)
    return min if seats.endswith(lower) else max


for line in lines:
    line = line.strip()
    rows = line[0:7]
    columns = line[7:]

    rowNum = getPosition(0, 127, 'F', 'B', rows)
    colNum = getPosition(0, 7, 'L', 'R', columns)
    seatIdsFound.append((rowNum * 8) + colNum)

sortedSeatIds = sorted(seatIdsFound)
next = sortedSeatIds[0]

for seatId in sortedSeatIds:
    if next != seatId:
        break
    next += 1

print("My seat id: {}".format(next))
