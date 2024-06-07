# 3. Write a program that accepts a comma separated sequence of words as input and prints the
# words in a comma-separated sequence after sorting them alphabetically. Suppose the
# following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

def comma_sepSort(string):
    separate = string.split(",")
    print(separate)

    for char in range(len(separate)-1):
        for nextChar in range(char+1 , len(separate)):
            if separate[char][0] > separate[nextChar][0]:
                separate[char] , separate[nextChar] = separate[nextChar] , separate[char]

    print(separate)        


comma_sepSort("without,hello,bag,world")