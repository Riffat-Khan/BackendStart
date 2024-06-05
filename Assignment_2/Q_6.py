# Write a function binary2Decimal that take binary number as input and return decimal
# equivalent of the given number.

def binary2Decimal(binaryNum):
    array = []
    for i in str(binaryNum):
        array.append(i)
    
    i =  sum = 0
    revArray = []
    while len(array):
        number = array.pop()
        prod = int(number) * 2**i
        sum+=prod
        i+=1
    print(sum)
    

binary2Decimal(101011)