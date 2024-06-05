# Declare a list of 10 random  integers and then find mean, median and mode of integers.

import random

# integerArray = [45,4, 8, 2, 90, 34, 3, 24, 66, 7]
# index = 0
# while index <10:
#     integerArray.append(random.randint(0,10))

def mean(integerArray):
    start = sum = 0
    while start < len(integerArray):
        sum+=integerArray[start]
        start+=1
    
    meanVal = sum/10
    print("mean" , meanVal)


def median(integerArray):
    medianVal = 0
    integerArray.sort()
    if len(integerArray)%2 != 0 :
        middleIndex =  len(integerArray//2)+1
        medianVal = integerArray[middleIndex]
    else: 
        middleIndex1 = len(integerArray)//2
        middleIndex2 = (len(integerArray)//2) -1
        medianVal = (integerArray[middleIndex1] + integerArray[middleIndex2])/2
    print("median" , medianVal)

def mode(integerArray):
    index = 0 
    maxCount = 0
    modeVal = 0
    while index < (len(integerArray) -1):
        next = index +1
        matchCount = 0
        while next < len(integerArray):
            if integerArray[index] == integerArray[next]: 
                matchCount+=1
            next+=1
        if matchCount > maxCount: 
            maxCount = maxCount
            modeVal = integerArray[index]
        index+=1

    print("mode" , modeVal)
    

mean(integerArray = [45,4, 8, 2, 90, 34, 3, 2, 66, 7])
median(integerArray = [45,4, 8, 2, 90, 34, 3, 2, 66, 7])
mode(integerArray = [45,4, 8, 2, 90, 34, 3, 2, 66, 7])
