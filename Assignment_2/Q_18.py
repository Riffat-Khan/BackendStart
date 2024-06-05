# Write a for loop that iterates over a list of strings myList and prints the first three characters
# of every word. e.g. If myList is the list ['January', 'February', 'March'] thenthe following
# should be printed:
# Jan
# Feb
# Mar

myList = ['January', 'February', 'March']
start = 0
while start < len(myList):
    string = myList[start]
    strStart = 0
    while strStart < 3:
        print(string[strStart] , end = "")
        strStart+=1
    print("\n")
    start+=1
