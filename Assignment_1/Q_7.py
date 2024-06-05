# If a five-digit number is input through the keyboard, write a program to calculate the sum
# of its digits. (Hint: Use the modulus operator „%‟ to split the digits).

number = input("Enter a 5 digit number : ")
sum = 0

for i in number:
    sum += int(number)

print("The sum of each digit of " , number , "is :", sum)
  