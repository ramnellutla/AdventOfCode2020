f = open("input.txt", "r")

lines = f.readlines()
fieldNamesFound = {"byr": False, "iyr": False, "eyr": False,
                   "hgt": False, "hcl": False, "ecl": False, "pid": False}
validPassports = 0

for line in lines:
    if len(line.strip()) == 0:  # This is followed by a new passport
        if all(value is True for value in fieldNamesFound.values()):
            print(fieldNamesFound)
            validPassports += 1
        fieldNamesFound = {"byr": False, "iyr": False, "eyr": False,
                           "hgt": False, "hcl": False, "ecl": False, "pid": False}
        continue

    lineFields = line.split(' ')
    for field in lineFields:
        name = field.split(':')[0]
        if name in fieldNamesFound:
            fieldNamesFound[name] = True

if all(value == True for value in fieldNamesFound.values()):
    validPassports += 1

print("Number of valid passports found: {}".format(validPassports))
