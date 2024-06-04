# If the three sides of a triangle are entered through the keyboard, write a program to check
# whether the triangle is isosceles, equilateral, scalene or right-angled triangle.

base = input("Enter then base of the triangle:")
hypotenus = input("Enter then hypotenus of the triangle:")
perpendicular = input("Enter then perpendicular of the triangle:")

if(int(base) == int(hypotenus) == int(perpendicular)) : print("Triangle is EQUILATERAL")
elif(int(base)**2 + int(perpendicular)**2 == int(hypotenus)**2) : print("Triangle is RIGHT-ANGLED-TRIANGLE")
elif((int(base) == int(hypotenus)) or (int(hypotenus) == int(perpendicular)) or (int(base) == int(perpendicular))) : print("Triangle is ISOSCELES")
elif(not (int(base) == int(hypotenus) == int(perpendicular))) : print("Triangle is SCALENE")
