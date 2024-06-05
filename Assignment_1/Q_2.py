# The distance between two cities (in km.) is input through the keyboard. Write a program
# to convert and print this distance in meters, feet, inches and centimeters.

distance = input("The distance between Linked Matrix and my home is:\n")
print("The distance we got is " , distance , "km")

#meters
meter = float(distance) * 1000
print("In meters it will become" , meter)

#inches
inches = float(meter) * 39.4
print("In inches it will become" , inches)

#centimeter
centimeter = float(inches) * 2.5
print("In inches it will become" , centimeter)
