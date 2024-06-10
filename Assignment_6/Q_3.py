# Write a Python program to get the smallest number from a list.

List = [4, 7, 65, 78, 5, 2, 1]
smallest = List[0]
for i in List:
    if i < smallest: smallest = i

print(smallest)
