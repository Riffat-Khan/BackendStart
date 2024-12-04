# 1. Implement a function that meets the specification below. Use a try-except block.
# def sumDigits(s):

# """Assumes s is a string
# Returns the sum of the decimal digits in s
# For example, if s is 'a2b3c' it returns 5"""

def sumDigits(s):
    number = "123456789"

    sum =0
    for char in s:
        if char in number:
            sum+=int(char)

    print(sum)

sumDigits(s="a2b3c")