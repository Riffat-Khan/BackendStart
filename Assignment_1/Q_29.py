# 29. Write a program to produce the following output using loop:

#       1
#     2   3
#   4   5   6
# 7   8   9   10

number = 1
count = 1
while count <=4:
    print(" "*(4-count) , end="") 
    contain = 1
    while contain <=count:
        print(number , end=" ")
        number+=1
        contain +=1
    count +=1
    print("\n")

        
        