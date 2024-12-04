# iii. Write a program to return the third and last largest number in the array.

List = [4, 34, 7, 56, 8, 4, 66 ,98, 3, 66]

unique = []
count = 0
for i in range(len(List)):
    for j in range(i+1 , len(List)):
        if List[j] != List[i]:
            count +=1
    if count >=1:
        unique.append(List[i])

print(unique)

unique.sort()

print("Last Largest : " , unique[-1])
print("Third last Largest : " , unique[-3])
