# Write a program to enter the numbers till the user wants and at the end it should display
# the count of positive, negative and zeros entered."""  """

want = "y"
positive = negative = zeros = 0

while want.lower() != "n":
    want = input("Want to enter number YES : y / NO : n ? ")
    if( want == "y"):
        number = input("Enter a number :")
        if(float(number) == 0): zeros+=1
        elif(float(number) > 0) : positive+=1
        elif(float(number) < 0) : negative+=1
        else: print("Must be a number")
    else: want = "n"

print("The number entered are : \n positive:" , positive , "\n negative:" , negative , "\n zeros:" , zeros)