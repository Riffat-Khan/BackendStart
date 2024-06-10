# vi. Given 2 arrays of ints, a and b, return True if they have the same first element or
# they have the same last element. Both arrays will be length 1 or more. 
# This_will_give_me_last_index=a.length();
# A[This_will_give_me_last_index];
# common_end([1, 2, 3], [7, 3]) → True
# common_end([1, 2, 3], [7, 3, 2]) → False
# common_end([1, 2, 3], [1, 3]) → True

def common_end (List_1 , List_2):
    if List_1[0] == List_2[0] or List_1[len(List_1)-1] == List_2[len(List_2)-1]:
        return "True"
    else:
        return "False"
    
print(common_end([1, 2, 3], [7, 3]))
print(common_end([1, 2, 3], [7, 3, 2]) )
print(common_end([1, 2, 3], [1, 3]))  
