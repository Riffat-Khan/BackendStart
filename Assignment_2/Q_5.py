# Write your own Range function that take three parameters (start, stop and step) as an input
# and return the list of integer numbers.

def Range(start , stop , step):
    integers = []
    i = start
    while i < stop:
        integers.append(i)
        i+=step
    print(integers)

Range(start=5 , step= 3 , stop= 30)

def RangeArr(start , stop , step):
    integers = [3, 5, 2, 56, 34, 25, 8]
    rangeArray = []
    i = 0
    while i < stop:
        rangeArray.append(integers[i])
        i+=step
    print(rangeArray)

RangeArr(start=2 , step= 2 , stop= 5)