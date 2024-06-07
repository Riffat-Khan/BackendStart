# ii. Write a function which should add the two vowels in the arrays and generate
# third array


def addVowels(string):
    List = list(string)
    VowelInList = []
    for char in List:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            VowelInList.append(char)
    return VowelInList

def vowelArr(str_1 , str_2):

    combList = addVowels(string=str_1) + addVowels(string=str_2)
    print(combList)

vowelArr(str_1 = "jelliyobean" , str_2= "jelliyobean")

