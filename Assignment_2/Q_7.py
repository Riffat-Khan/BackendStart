# Write a function Multiple that considers a pair of integers and determines whether the
# second integer is the multiple of the first or not. The function should take two integers as
# arguments and return True if the second is a multiple of the first, and False otherwise.


def Multiple (integer_1 , integer_2):
    if integer_2%integer_1 == 0: print(integer_2 , "is a multiple of" , integer_1)
    else: print(integer_2 , "is not a multiple of" , integer_1)

Multiple(integer_1=5 , integer_2=15)