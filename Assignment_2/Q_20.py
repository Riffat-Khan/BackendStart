# Write a program that requests an integer n from the user and append the squares of all
# numbers from 0 up to, but not including, n. At the end print the list.
# >>>
# Enter n: 4
# [0, 1, 4, 9]

def squareALl(number):
    number = input("Enter a number:")
    arraySqr = []
    length = 0
    while length < int(number):
        arraySqr.append(length**2)
        length+=1

    print(arraySqr)

squareALl(number = 0)