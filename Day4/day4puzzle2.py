import re
f = open("input.txt", "r")

lines = f.readlines()
fieldNamesFound = {"byr": False, "iyr": False, "eyr": False,
                   "hgt": False, "hcl": False, "ecl": False, "pid": False}

validEcls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def byr(byr):
    byrNum = int(byr)
    return len(byr) == 4 and byrNum >= 1920 and byrNum <= 2002


def iyr(iyr):
    iyrNum = int(iyr)
    return len(iyr) == 4 and iyrNum >= 2010 and iyrNum <= 2020


def eyr(eyr):
    eyrNum = int(eyr)
    return len(eyr) == 4 and eyrNum >= 2020 and eyrNum <= 2030


def hgt(hgt):
    if hgt.endswith('cm'):
        splitHgt = hgt.split('cm')
        print(splitHgt, len(splitHgt[1]))
        hgtNum = int(splitHgt[0])
        return len(splitHgt[1]) == 0 and hgtNum >= 150 and hgtNum <= 193
    elif hgt.endswith('in'):
        splitHgt = hgt.split('in')
        hgtNum = int(splitHgt[0])
        return len(splitHgt[1]) == 0 and hgtNum >= 59 and hgtNum <= 76
    return False


def hcl(hcl):
    return len(hcl) == 7 and hcl.startswith('#') and bool(re.match('[a-f0-9]+$', hcl[1:]))


def ecl(ecl):
    return ecl in validEcls


def pid(pid):
    return len(pid) == 9 and bool(re.match('[0-9]+$', pid))


fieldValidations = {"byr": byr, "iyr": iyr, "eyr": eyr,
                    "hgt": hgt, "hcl": hcl, "ecl": ecl, "pid": pid}

validPassports = 0

for line in lines:
    if len(line.strip()) == 0:  # This is followed by a new passport
        if all(value is True for value in fieldNamesFound.values()):
            validPassports += 1
        fieldNamesFound = {"byr": False, "iyr": False, "eyr": False,
                           "hgt": False, "hcl": False, "ecl": False, "pid": False}
        continue

    lineFields = line.split(' ')
    for field in lineFields:
        fieldSplit = field.split(':')
        name = fieldSplit[0].strip()
        value = fieldSplit[1].strip()
        if name in fieldNamesFound:
            fieldNamesFound[name] = fieldValidations[name](value)

if all(value == True for value in fieldNamesFound.values()):
    validPassports += 1

print("Number of valid passports found: {}".format(validPassports))
