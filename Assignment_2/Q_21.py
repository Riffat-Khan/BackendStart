# Implement a function ion2e() that takes a string as input and returns a copy of the string with
# the following change: if the entered word (input string) ends in 'ion', then 'ion' is replaced
# with 'e', otherwise it returns the same word.
# >>> ion2e(“congratulation”)
# “congratulate”
# >>> ion2e(“marathon”)
# “marathon”

def ion2e(string):
    newStr = string
    if string.find("ion") != -1:
        newStr = string.replace("ion" , "e")

    print(newStr)

ion2e("wahion")