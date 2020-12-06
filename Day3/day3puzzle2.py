from functools import reduce

f = open("input.txt", "r")
lines = f.readlines()
count = [0, 0, 0, 0, 0]
lineNum = -1

for line in lines:
    line = line.strip()
    lineNum += 1
    if lineNum == 0:
        continue

    lineLength = len(line)

    slopeIndexes = []
    slopeIndexes.append(lineNum+1)
    slopeIndexes.append((3*lineNum)+1)
    slopeIndexes.append((5*lineNum)+1)
    slopeIndexes.append((7*lineNum)+1)

    if(lineNum % 2 == 0):
        slopeIndexes.append((lineNum/2) + 1)

    slopeCount = 0
    for index in slopeIndexes:
        slopeEndValue = index % lineLength
        actualIndex = int(
            lineLength-1) if slopeEndValue == 0 else int(slopeEndValue - 1)

        if line[actualIndex] == '#':
            count[slopeCount] += 1
        slopeCount += 1


print("Product of trees: {}".format(reduce(lambda x, y: x*y, count)))
