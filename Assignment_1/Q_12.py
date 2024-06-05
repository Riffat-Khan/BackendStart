# Write a program that reads in two integers and determines and prints whether the first is a
# multiple of the second. [Hint: Use the remainder operator.

integer_1 , integer_2 = input("Enter two integers:").split()
if int(integer_1)%int(integer_2) == 0: print(True)
else:print(False)
