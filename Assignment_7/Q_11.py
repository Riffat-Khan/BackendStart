# xi. Write a function AlphabetSoup(str) take the str string parameter being passed
# and return the string with the letters in alphabetical order (ie. hello becomes
# ehllo). Assume numbers and punctuation symbols will not be included in the
# string.

def AlphabetSoup(string):
    for i in range(len(string)-1):
        j = i+1
        for j in range(len(string)):
            if string[i] < string[j]:
                temp = string[i] 
                temp_2 = string[j]

                string[i] = temp_2
                string[j] = temp
                i+=1
    print(string)

AlphabetSoup(string="hello")


