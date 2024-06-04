# (Triangle-Printing Program) Write a program that prints the following patterns
# separately, one below the other. Use for loops to generate the patterns. All asterisks (*)
# should be printed by a single print statement of the form print "*" (this causes the
# asterisks to print side by side). [Hint: The last two patterns require that each line begin
# with an appropriate number of blanks.]



# (A)
# *
# **
# *** 
# **** 
# *****
# ******
# ******* 
# ********
# ********* 
# **********

value = 1
while value <= 10:
    print("*" * value)
    value +=1



# (B)
# **********
# *********
# ********
# *******
# ******
# *****
# ****
# ***
# **
# *

print("\n")
value = 10
while value >= 1:
    print("*" * value)
    value -=1



# (C)
# ********** 
#  ********* 
#   ******** 
#    ******* 
#     ****** 
#      ***** 
#       **** 
#        *** 
#         ** 
#          * 
value = 10
space = 0
while value >= 1 and space<=10:
    print(" " * space,"*" * value)
    value -=1
    space +=1




#(D)
#            *
#            **
#           ***
#           ****
#          *****
#          ******        
#         *******
#         ********
#        *********
value = 0
space = 5
while value <=10:
    count = 0
    while count <2:
      print(" " * space,"*" * value , " " * space)
      value +=1
      count +=1
    space -=1