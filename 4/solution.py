import re

def main():
    f = open("input.txt", "r")
    inputArray= [line for line in f]

    numValid = 0
    i = 0
    while i < len(inputArray):
        i, isValid = getNextPassport(inputArray, i)
        if isValid:
            numValid += 1

    print numValid 

validityMap = {
    "byr" : lambda val: int(val) >= 1920 and int(val) <= 2002,
    "iyr" : lambda val: int(val) >= 2010 and int(val) <= 2020,
    "eyr" : lambda val: int(val) >= 2020 and int(val) <= 2030,
    "hgt" : lambda val: checkHeight(val),
    "hcl" : lambda val: re.match('#[0-9a-f]{6}$', val),
    "ecl" : lambda val: val in eyecolors,
    "pid" : lambda val: re.match('[0-9]{9}$', val),
    "cid" : lambda val: 1 == 1
}

def isFieldValid(field, value):
    return validityMap[field](value)

def getNextPassport(inputArray, i):
    fieldsSeen = {
        "byr" : False,
        "iyr" : False,
        "eyr" : False,
        "hgt" : False,
        "hcl" : False,
        "ecl" : False,
        "pid" : False,
    }
    while i < len(inputArray) and  inputArray[i] != '\n': 
        nextLine = inputArray[i]
        pairs = nextLine.split()
        for pair in pairs:
             field = pair.split(":")[0]
             value = pair.split(":")[1]
             if field == "pid":
                print field, value, isFieldValid(field, value)
             if field in fieldsSeen:
                 #fieldsSeen[field] = True
                 fieldsSeen[field] = isFieldValid(field, value)
        i += 1 
    for k in fieldsSeen:
        if not fieldsSeen[k]:
            print "False --------------->", k
            return i+1, False
    print "True"
    return i+1, True

eyecolors = {
  "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
}

def checkHeight(val):
    if val[-2:] == 'in':
        return int(val[:-2]) >= 59 and int(val[:-2]) <= 76
    if val[-2:] == 'cm':
        return int(val[:-2]) >= 150 and int(val[:-2]) <= 193
    return False

main()
