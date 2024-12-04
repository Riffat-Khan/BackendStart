# v. Given an array of ints, return True if .. 1, 2, 3,.. appears in the array
# somewhere. 
# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True


def array123(List):
    match = 0
    for i in range(len(List)-2):
        if List[i] == 1 and List[i+1] == 2 and List[i+2] == 3:
            match+=1
    
    if match >= 1:
        return "True"
    else:
        return "False"
        


print(array123(List=[1, 1, 2, 3, 1]))
print(array123(List=[1, 1, 2, 4, 1]))
print(array123(List=[1, 1, 2, 1, 2, 3]) )