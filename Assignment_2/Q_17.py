# Take a name (i.e., a string) as an input from the user and insert it into a list, then pass this list
# to a function swap that exchange the first and last values of list. After swapping print the
# resultant list.

name = "hamza"
theList = ['Ahmad', 'Zainab', 'Hina', 'Ali']
theList.append(name)

def swap(theList):
    temp =""

    temp = theList[0] 
    theList[0]  = theList[(len(theList) -1)]
    theList[(len(theList) -1)] = temp

    print(theList)

swap(theList)



    