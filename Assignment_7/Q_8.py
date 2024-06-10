# Given a string you are provided with the possible operations.
# We can group the adjacent substrings, for e.g ABCABCBC can be compressed as 
# 2ABC1BC or 1ABCA2BC
# Among all the possible options, task is to find the resultant string with the
# minimum length.
# In case if there are multiple solutions return the lexicographically smallest string.
# So for the above example the solution would be 2ABC1BC
# Another example would be
# FLFLAFLAFLAF
# Solution: 1FLF3LAF

string = "ABCABCBC"
compressed = []
for char in range( 0 , len(string)-2, 3 ):
    count = 1
    for nextChar in range(char+3 , len(string)-2):

        if string[char] != "'" and string[char] == string[nextChar] and string[char+1] == string[nextChar+1] and  string[char+2] == string[nextChar+2]:
            count +=1
    
    compressed.append(str(count)+string[char]+string[char+1]+string[char+2])
    while(count >1):
        string = string.replace("ABC" , "'''")
        count-=1

print(compressed)
