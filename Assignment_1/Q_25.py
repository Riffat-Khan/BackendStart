# Write a program to find the range of a set of numbers. Range is the difference between
# the smallest and biggest number in the list. You are not allowed to use built-in range()
# function.

# using sort()
list = [4, 7, 2, 4, 97, 19, 34, 1]
list.sort()
range = list[len(list) - 1] - list[0]
print(range)


# without using built-in func
smallest = largest = list[0]

for integer in list:
    if integer >= largest: largest = integer
    elif integer <= smallest: smallest = integer

range = largest - smallest
print(range)