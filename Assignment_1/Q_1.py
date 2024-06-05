# Write a program that asks the user to enter two numbers, obtains them from the user and
# prints their sum, product, difference, quotient and remainder.

Num_1 = input("Enter 1st number:\n")
print("You entered " ,Num_1)

Num_2 = input("Enter 2nd number:\n")
print("You entered" , Num_2)

#SUM
print("The sum:" , Num_1 , "+" , Num_2 , "=" , int(Num_1) + int(Num_2) )

#PRODUCT
print("The product:" , Num_1 , "x" , Num_2 , "=" , int(Num_1) * int(Num_2) )

#DIFFERENCE
print("The difference:" , Num_1 , "-" , Num_2 , "=" , int(Num_1) - int(Num_2) )

#QUOTIENT
print("The quotient:" , Num_1 , "/" , Num_2 , "=" , int(Num_1) / int(Num_2) )

#REMAINDER
print("The remainder:" , Num_1 , "%" , Num_2 , "=" , int(Num_1) % int(Num_2) )
