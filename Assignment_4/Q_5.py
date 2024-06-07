# v. Given a string containing just the characters '(' and ')', find the length of the longest
# and shortest valid (well-formed) parentheses substring.
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
# Another example is ")()())", where the longest valid parentheses substring is "()()",
# which has length = 4.


string = ")()()(((()))))"
length = 0
for i in range(len(string)):
    if string[i] == "(" and string[i+1] == ")":
        length+=1
        i+=2

print(length)