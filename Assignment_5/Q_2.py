# 2. Write a Python program to display the first and last colors from the following list. 
# color_list = [Red, Green, White, Black, Pink , Yellow]

color_list = ["Red", "Green", "White", "Black", "Pink" , "Yellow"]
for i in range(2):
    print(color_list[-i])
    i-=1
