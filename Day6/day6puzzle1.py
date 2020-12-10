f = open("input.txt", "r")

lines = f.readlines()
count = 0
seen = [0] * 26

for line in lines:
    line = line.strip()
    if len(line) == 0:
        answers = seen.count(1)
        count += answers
        seen = [0] * 26
        continue

    for c in line:
        seen[ord(c)-97] = 1


count += seen.count(1)

print("Number of answers: {}".format(count))
