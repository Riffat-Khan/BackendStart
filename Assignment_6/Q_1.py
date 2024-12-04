# Print the following pattern using for loop:
# A) 
# **********
# **********
# **********
# **********

for i in range(4):
    print("*" * 10)




# B)
# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10 12 14 16 18 20
# 3 6 9 12 15 18 21 24 27 30
# 4 8 12 16 20 24 28 32 36 40
# 5 10 15 20 25 30 35 40 45 50

i = 1
for i in range(5):
    i+=1
    for j in range(10):
        j+=1
        print(j*i , end = " ")
        
    print("\n")



# C)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(5):
    i+=1
    for j in range(i):
        j+=1
        print(j , end=" ")
    print("\n")
