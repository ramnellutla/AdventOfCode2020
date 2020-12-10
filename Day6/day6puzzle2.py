from functools import reduce
f = open("input.txt", "r")

lines = f.readlines()
count = 0
seen = []

for line in lines:
    line = line.strip()
    if len(line) == 0:
        answers = reduce((lambda x, y: x & y), seen)
        count += len(answers)
        seen = []
        continue

    ans = set()
    for c in line:
        ans.add(c)
    seen.append(ans)

answers = reduce((lambda x, y: x & y), seen)
count += len(answers)

print("Number of answers: {}".format(count))
