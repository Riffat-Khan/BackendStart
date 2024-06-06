# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : [Red, Green, White, Black, Pink , Yellow]
# Expected Output : [[Green, White, Black]


List = ["Red", "Green", "White", "Black", "Pink" , "Yellow"]

for i in range(2):
    List.pop()

List.pop(0)
print(List)
