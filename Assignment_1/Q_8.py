# Write a program that reads in the radius of a circle and prints the circle‟s diameter,
# circumference and area. Use the constant value 3.14159 for pi. Perform each of these
# calculations inside the print statement(s) and use the conversion format specifier %f.

radius = input("Enter the radius of the circle\n")
pi = 3.14159

print("The diameter of the circle is %f" %(float(radius)**2) )
print("The area of the circle is %f" %(pi*float(radius)**2) )
print("The circumference of the circle is %f" %(2*pi*float(radius)) )