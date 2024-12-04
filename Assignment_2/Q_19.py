# Write a twoDlist function that perform 3×3 matrix multiplication. 

list1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
list2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

twoDlist = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3):
    for j in range(3):
        for k in range(3):
            twoDlist[i][j] += list1[i][k] * list2[k][j]

print(twoDlist)