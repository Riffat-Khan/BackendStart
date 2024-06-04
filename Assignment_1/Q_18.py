# A library charges a fine for every book returned late. For first5 days, the fine is 50 paise,
# for 6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book
# after 30days your membership will be cancelled. Write a program to accept the number
# of days the member is late to return the book and display the fine or the appropriate
# message.

duration = input("Enter the number of days you're late from submission:")
fine = 0

if(int(duration) == 0): print("Fine :" , fine )
elif(int(duration) <=5): print("Fine :" , 50 , "paise" )
elif(int(duration) >= 6 and int(duration) <=10): print("Fine :" , 1 , "rupee" )
elif(int(duration) > 10 and int(duration) <=30): print("Fine :" , 5 , "rupees" )
elif(int(duration) > 30): print("Membership cancelled." )
else: print("invalid input!")