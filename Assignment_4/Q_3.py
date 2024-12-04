# Given an array, Rotate (shift left) an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated
# to [5,6,7,1,2,3,4].
# After rotating the array add in into another array and display array index with
# minumum value.


n = input("Enter the length of thr array:")
k = input("Enter the shift value:")

n = int(n)
k = int(k)

List = []
for i in range(1,n+1):
    List.append(i)

rotatedList = []

for j in range(1, k+1):
    if len(List) == 0:
        for i in range(1,n+1):
            List.append(i)
    
    rotatedList.append(List.pop())


rotatedList+=List

smallestValIndex = 0
smallVal = rotatedList[smallestValIndex]

for num in range(len(rotatedList)):
    if smallVal > rotatedList[num]:
        smallVal = rotatedList[num]
        smallestValIndex = num


print("array index with minimum value" , smallestValIndex )
