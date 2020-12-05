def main():
    # parse input
    fileInput = []
    #f = open("smallinput.txt", "r")
    f = open("input.txt", "r")
    for line in f:
        fileInput.append(line[:-1])

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    #slopes = [(3, 1)]

    rowLen = len(fileInput[0])
    product = 1
    for slope in slopes:
        numTrees = 0
        y = 0
        x = 0
        while y < len(fileInput):
            if fileInput[y][x] == '#':
                numTrees += 1
            y += slope[1]
            x += slope[0]
            x = x % rowLen 

        product *= numTrees
    print product
