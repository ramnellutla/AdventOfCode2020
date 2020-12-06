f = open("input.txt", "r")
lines = f.readlines()
valid = 0

for line in lines:
    split = line.split(':')
    password = split[1].strip()
    policy = split[0]

    policySplit = policy.split(' ')
    threshold = policySplit[0]
    term = policySplit[1]

    thresholdSplit = threshold.split('-')
    position1 = int(thresholdSplit[0])
    position2 = int(thresholdSplit[1])

    print(position1, position2, term, password)

    if (password[position1-1] == term and password[position2-1] != term) or (password[position1-1] != term and password[position2-1] == term):
        valid += 1

print("Number of valid policies: {}".format(valid))
