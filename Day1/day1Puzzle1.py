f = open("input.txt", "r")
lines = f.readlines()

seen = set()
target = 2020

for line in lines:
    parsedLine = int(line)
    complement = 2020-parsedLine
    if complement in seen:
        print("Numbers: {}, {}; Product: {}".format(
            parsedLine, complement, parsedLine * complement))
        break
    else:
        seen.add(parsedLine)
