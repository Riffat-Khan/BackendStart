# Write a program to find the binary equivalent of the entered number., i.e. binary
# equivalent of 170 is 10101010

number = input("Enter a valid number:")
rem = int(number)
array = []
while rem > 0:
    digit = rem%2
    array.append(digit)
    rem= rem//2

while len(array) > 0:
    print(array.pop())



