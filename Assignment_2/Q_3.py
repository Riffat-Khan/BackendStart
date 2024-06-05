# Take an integer number as an input from user, write a function that checks weather a given
# number is Armstrong or not. Hint: If sum of the cubes of each digit of the number is equal to
# the number itself, then the number is called an Armstrong number. For example, 153 = (1 * 1
# * 1) + (5 * 5 * 5) + (3 * 3 * 3)

def isArmstrong():
    number = input("Enter a integer:")

    value = 0
    for i in number:
        cube = (int(i)**3)
        value += cube
    if value == int(number): print(number + " is an Armstrong number")
    else: print(number + " is not an Armstrong number")

isArmstrong()