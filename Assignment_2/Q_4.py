# Write a function to find the octal equivalent of the given number. For example: the octal
# equivalent of 50 is 62.

def octalValue(number):
    rem = int(number)
    array = []
    while rem > 0:
        digit = rem%8
        array.append(digit)
        rem= rem//8
    
    print(" The octal equivalent of " , number , " is " , end = "")
    while len(array) > 0:
        print(array.pop() , end = "")

    print("\n")
octalValue(50)
