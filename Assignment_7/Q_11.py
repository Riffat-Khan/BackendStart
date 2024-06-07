# xi. Write a function AlphabetSoup(str) take the str string parameter being passed
# and return the string with the letters in alphabetical order (ie. hello becomes
# ehllo). Assume numbers and punctuation symbols will not be included in the
# string.

def AlphabetSoup(string):
    array = list(string)
    for i in range(len(array)-1):
        for j in range(i+1 , len(string)):
            if array[i] > array[j]:
                array[i] , array[j] = array[j] , array[i]

    sortedString = "".join(array)
    print(sortedString)

AlphabetSoup(string="hello")
