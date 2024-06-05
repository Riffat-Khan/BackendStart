# Write a function that displays a solid square of a character whose side and the character to be
# printed are specified in integer and character as the function parameters. For example, if side
# is 5 and character is ‘#’, the function should display:
# #####
# #####
# #####
# #####
# #####

def solidSquare(length , char):
    i = 0
    while i< length:
        print(char*length)
        i+=1

solidSquare(length=5 , char="@")