#Two numbers (base and exponent) are entered through the keyboard. Write a program to
#find the value of base raised to the power of exponent.

base = input("Enter the value for the base : ")
exponent = input("Enter the value for the exponent : ")

print( base, "^", exponent , "=" , pow(int(base),int(exponent)))
