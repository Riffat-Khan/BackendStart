# An integer number is said to be a perfect number if its factors, including 1 (but not the
# number itself), sums up to the number. For example, 6 is a perfect number because 6 = 1 + 2
# + 3. Write a function perfect that determines whether parameter number is a perfect number.
# Use this function in a program that determines and prints all the perfect numbers between 1
# and 1000.

def perfectNum(number):
    i=2
    factors = [1]
    while i <= number//2:
        if( i == 1 or number%i == 0 ): factors.append(i)
    
    i = sum = 0
    while i<len(factors):
        sum+=factors[i]
        i+=1
    
    if sum == number: print(number)


def allPerfectNum():
    print("Following are the perfect numbers between 0 - 1000")
    start = 2
    while(start < 1000):
        perfectNum(number=start)
        start+=1


allPerfectNum()