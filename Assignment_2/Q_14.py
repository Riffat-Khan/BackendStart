# Write a function that takes a tuple of 10 number as a parameter and return the minimum of all
# the numbers.

def minTuple(dectuple):
    
    minimumVal = 0
    index = 1
    minimumVal = dectuple[0]
    while index < (len(dectuple)-1):
        if dectuple[index] <= minimumVal: minimumVal = dectuple[index]
        index+=1
    print("Minimum of all the numbers" , minimumVal)

minTuple((55,2,4,1,45,67,0,34,2, 5))