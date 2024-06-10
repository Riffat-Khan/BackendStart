# Write a function primeFactor that takes one parameter as its argument and obtain the prime
# factors of the number. Hint: Find all the prime number that multiply together to make the
# original number. e.g. prime factors of 15 are 5 and 3.

def primeFactor(number):
    primeFactors = []
    i = 2
    while(i < number//2):
        if(number%i == 0):
            if(i==2 or i==3 or (i%2!= 0  and i%3 != 0)): primeFactors.append(i)
        i+=1

    primeFacArray = []
    i = 1
    while i <= len(primeFactors):
        j = i+1
        while j < len(primeFactors):
            if i*j == number:
                primeFacArray.append(i , j)
            j+=1
        i+=1
    print(primeFacArray)

primeFactor(15)
