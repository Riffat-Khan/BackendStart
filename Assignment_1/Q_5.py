# The length & breadth of a rectangle are input through the keyboard. Write a program to
# calculate the area & perimeter of the rectangle.

length = input("What's the length of the rectangle in cm? ")
breadth = input("What's the breadth of the rectangle in cm? ")

area = float(length) * float(breadth)
print("Thus the area is ", area , "cm2")

perimeter = 2 * float(length) + float(breadth)
print("And the perimeter calculated is:" , perimeter, "cm")
