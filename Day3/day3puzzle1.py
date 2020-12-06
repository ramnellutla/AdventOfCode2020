f = open("input.txt", "r")
lines = f.readlines()
count = 0
lineNum = -1

for line in lines:
    line = line.strip()
    lineNum += 1
    if lineNum == 0:
        continue

    lineLength = len(line)
    slopeEndIndex = (3*lineNum)+1
    slopeEndValue = slopeEndIndex % lineLength

    actualIndex = lineLength-1 if slopeEndValue == 0 else slopeEndValue - 1

    print(slopeEndIndex, lineLength, actualIndex, line[actualIndex])

    if line[actualIndex] == '#':
        count += 1


print("Total trees: {}".format(count))
