# i. Convert a non-negative integer to its English words representation and print in
# reverse if total characters in English words are more than total words in a
# sentence.


n = 72
engRep = chr(n)

sentence = " what are you doing"
words = sentence.split()
reverse = []
if len(engRep) > len(words):
    for i in range(len(chr)):
        reverse.append(engRep.pop())

print(engRep)
