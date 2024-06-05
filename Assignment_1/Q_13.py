# Write a program that asks the user to enter two integers, obtains the numbers from the
# user, then prints the larger number followed by the words “is larger.” If the numbers are
# equal, print the message “These numbers are equal.” Use only the single-selection form
# of the if statement you learned in this chapter.

integer_1 , integer_2 = input("Enter two integers:").split()
if int(integer_1) > int(integer_2): print(integer_1 , 'is larger')
elif int(integer_1) < int(integer_2): print(integer_2 , 'is larger')
elif int(integer_1) == int(integer_2): print("These numbers are equal.")
else:print("Invalid")