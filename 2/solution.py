import re

def main():
    # parse input
    f = open("input.txt", "r")
    validCount1 = 0
    validCount2 = 0
    for line in f:
        letter = re.match(r':', line)
        bounds = map(int, re.findall(r'\d+', line))
        splits = line.split()
        letter = splits[1][0]
        pw = splits[2]
        

        ## part 1
        numLetters = 0
        for i in pw:
            if i == letter:
                numLetters += 1

        if numLetters >= bounds[0] and numLetters <= bounds[1]:
            validCount1 += 1

        ## part 2, bounds are now actually indices
        index1 = bounds[0]-1
        index2 = bounds[1]-1
        if pw[index1] == letter and pw[index2] != letter:
            validCount2 += 1
        if pw[index1] != letter and pw[index2] == letter:
            validCount2 += 1

 
    print validCount1
    print validCount2





