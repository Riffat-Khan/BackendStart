# Write a function named isIn that accepts two strings as arguments and returns True if either
# string occurs anywhere in the other as a substring, and False otherwise. Hint: you might
# want to use the built-in str operation in."""  """

def isIn(string_1, string_2):
    valueIn1 = string_1.lower().find(string_2.lower())
    valueIn2 = string_2.lower().find(string_1.lower())
    if valueIn1 != -1 or valueIn2 != -1: print(True)
    else: print(False)

isIn("aqsa" , "QS")

