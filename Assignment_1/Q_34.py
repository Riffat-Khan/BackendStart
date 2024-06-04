# Write a program that prints the following diamond shape. You may use print statements
# that print either a single asterisk (*) or a single blank. Maximize your use of repetition
# (with nested for statements) and minimize the number of print statements.
# *
# ***
# *****
# *******
# *********
# *******
# *****
# ***
# *


value = 1
while value <10:
    print("*" * value) 
    value += 2

value = 7
while value > 0:
    print("*" * value) 
    value -= 2
