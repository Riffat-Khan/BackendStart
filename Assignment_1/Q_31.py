# 31. Write a program that displays the following checkerboard pattern:
# * * * * * * *
# * * * * * * * *
#  * * * * * * * *
# * * * * * * * *
#  * * * * * * * *
# * * * * * * * *
#  * * * * * * * *
# * * * * * * * *
# Your program must use only three output statements, one of each of the following forms:
# print "* "
# print " "

asterisk = 8
row = 4
while row > 0:
    space = 0
    while space < 2:
        print(" "*space , "*" * asterisk)
        space +=1
    row -=1