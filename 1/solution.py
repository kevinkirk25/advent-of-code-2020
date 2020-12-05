
def main():
    nums = []
    
    f = open("input.txt", "r")
    
    # grab input
    for line in f:
        nums.append(int(line))

    answer = findNumbers(nums, 3, 2020)
    product = 1
    for num in answer:
        product *= num
    print product


def findNumbers(numberList, numVals, desiredSum):
    #base case:
    if numVals == 1:
        for i in numberList:
            if i == desiredSum:
                return [i]
        return []
    else:
        for i, nextNum in enumerate(numberList):
            nextNum
            answer = findNumbers(numberList[i+1:], numVals - 1, desiredSum - nextNum)
            #if nextNum == 401:
            #    print nextNum
            #    print answer
            #    print numberList
            #    print len(answer) > 0 and sum(answer) + nextNum == desiredSum
            #    break
            if answer is not None and len(answer) > 0 and sum(answer) + nextNum == desiredSum:
                return answer + [nextNum]


            

