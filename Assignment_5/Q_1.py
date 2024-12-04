# 1. Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them

firstName = input("Enter your first name :")
lastName = input("Enter your last name :")

print(lastName , " " , firstName)

name = firstName + lastName
revName = ""
length = len(name)
for i in range(length):
    i+=1
    print(name[-i] , end =" ")
