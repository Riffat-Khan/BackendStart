# Given the length and breadth of a rectangle, write a program to find whether the area of
# the rectangle is greater than its perimeter. For example, the area of the rectangle with
# length = 5 and breadth = 4 is greater than its perimeter.

length = 5
breadth = 4

area = length * breadth
perimeter = (length + breadth) / 2

if(area > perimeter): print(True)
elif(area <= perimeter): print(False)
else:print("Invalid")