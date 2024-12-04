# 2. With a given integer number n provided by the user, write a program to generate a dictionary
# that contains {i: i*i} as its key:value pair such that all the integer numbers between 1
# and n are included). At the end, your program should print the dictionary. Suppose the
# following input is supplied to the program:
# Enter a Number: 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def printDictionary(number):
    number = input("Enter a Number:")
    NumberDict = {}
    number = int(number)
    for num in range(1, number+1):
        NumberDict[num] = num*num
    
    print(NumberDict)

printDictionary(number=0)