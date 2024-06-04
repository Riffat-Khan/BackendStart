# Write a program to check whether a triangle is valid or not, when the three angles of the
# triangle are entered through the keyboard. A triangle is valid if the sum of all the three
# angles is equal to 180 degrees.

Angle_1 = input("Enter the 1st angle in degrees:")
Angle_2 = input("Enter the 2nd angle in degrees:")
Angle_3 = input("Enter the 3rd angle in degrees:")

AnglesSum = int(Angle_1) + int(Angle_3) + int(Angle_3)
if(AnglesSum == 180): print("Triangle is valid")
else: print("Triangle is not valid")