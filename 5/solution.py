
def main():
    f = open("input.txt", "r")
    ids = [int(findRow(line)*8 + findCol(line)) for line in f]
    ordered= sorted(ids)
    print ordered
    print "max is:", ordered[-1]

    first = ordered[0]
    for i in ordered[1:]:
        if i != first + 1:
            print "my seat is:", i - 1
            break
        first = i

def binarySearch(f, c, line):
    ceil = float(c)
    floor = float(f)
    for i, c in enumerate(line):
        if c == "B" or c == "R":
            floor = round(((ceil - floor)/ 2)) + floor
            if i == len(line) - 1:
                return ceil
        elif c == "F" or c == "L":
            ceil = ceil - round((ceil - floor)  / 2)
            if i == len(line) - 1:
                return floor

def findRow(line):
    return binarySearch(0, 127, line[:7])

def findCol(line):
    return binarySearch(0, 7, line[-4:-1])
