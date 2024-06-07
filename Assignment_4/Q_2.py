# ii. Given an input n, count the total number of digit 1 appearing in all non-
# negative integers less than or equal to n.

# For example:
# Given n = 13,
# Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

n = input("Enter a number: ")
numArr = []
for i in range(1 ,int(n)+1):
    numArr.append(i)

print(numArr)
digitCount = 0
for value in numArr:
    value = str(value)
    count = 0
    for i in range(len(value)):
        if int(value[i]) == 1: 
            print(value[i])
            count+=1
    if count !=0:
        digitCount+=1

print(digitCount)
