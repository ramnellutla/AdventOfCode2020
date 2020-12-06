f = open("input.txt", "r")
lines = f.readlines()
valid = 0

for line in lines:
    count = 0
    split = line.split(':')
    password = split[1]
    policy = split[0]

    policySplit = policy.split(' ')
    threshold = policySplit[0]
    term = policySplit[1]

    thresholdSplit = threshold.split('-')
    thresholdMin = int(thresholdSplit[0])
    thresholdMax = int(thresholdSplit[1])

    for c in password:
        if c == term:
            count += 1

    if count >= thresholdMin and count <= thresholdMax:
        valid += 1

print("Number of valid policies: {}".format(valid))
