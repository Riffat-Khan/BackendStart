# Write a Python program to clone or copy a list.

List = ["Red", "Green", "White", "Black", "Pink" , "Yellow"]
cpyList = []

for i in range(6):
    strVAL = List.pop(0)
    cpyList.append(strVAL)

print(cpyList)
