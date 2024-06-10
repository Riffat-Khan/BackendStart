# iv. You are given an n x n 2D matrix representing an image.
# Rotate the image by 180 degrees (anti-clockwise) but after sorting the n*n 2D array

array2D = [
    [7, 8, 9],
    [1, 2, 3],
    [4, 5, 6],
]

List = []
for row in range(len(array2D)):
    List+=array2D[row]

for num in range(len(List)-1):
    for nextNum in range(num+1 , len(List)):
        if List[num] > List[nextNum]:
            List[num] , List[nextNum] = List[nextNum] , List[num]

newList = []
for i in range( 0, len(array2D)*len(array2D) , 3):
    newList.append(List[i : i+(len(array2D))])

list180  =[]

for i in range(len(newList)):
    list180.append(newList.pop())

print(list180)
        