# x. Write a the function LongestWord (sen) take the sen parameter being passed and
# return the largest word in the string. If there are two or more words that are the
# same length, return the first word from the string with that length. Ignore
# punctuation and assume sen will not be empty.


# my_str = "Hello!!!, he said ---and went."

def LongestWord (sen):

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    rem_punc = ""
    for char in sen:
        if char not in punctuations:
            rem_punc +=char
    
    print(rem_punc)

    maxLen = 0
    maxString = []
    strList = rem_punc.split()
    for string in strList:
        if len(string) > maxLen:
            maxLen = len(string)
            maxString.append(string)
    print(maxString[-1])         


LongestWord(sen="Hello!!!, he said thattt heeeee ---and went.")
