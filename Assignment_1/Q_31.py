# 31. Write a program that displays the following checkerboard pattern:
# * * * * * * *
# * * * * * * * *
# * * * * * * * *
# * * * * * * * *
# * * * * * * * *
# * * * * * * * *
# * * * * * * * *
# * * * * * * * *
# Your program must use only three output statements, one of each of the following forms:
# print "* "
# print " "


value = 5
space = 0
while value > 1:
    asterisk = 8
    while asterisk >= 7:
        print(" " *space , "*" * asterisk)
        asterisk -=1
        space +=1
    value -=1
    space -=1