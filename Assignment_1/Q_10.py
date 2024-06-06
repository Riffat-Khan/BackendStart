# Write a program that take year as an input from user. Determine whether year is leap year
# or not.

year = input("Enter a year you want to check:")

if(int(year)%4 == 0): 
    print("Is a leap year")
elif(int(year)%100 == 0) and (int(year)%400 == 0): 
    print("Is a leap year")
else : 
    print("It's not a leap year")