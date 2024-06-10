# vii. Given 3 int values, a b c, return their sum. However, if one of the values is the
# same as another of the values, it does not count towards the sum. 
# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0

def lone_sum(int_1 , int_2 , int_3):
    if int_1 != int_2 and int_1 != int_3:
        return (int_1 + int_2 + int_3)
    elif int_1 == int_2 and int_1 != int_3:
        return int_3
    elif int_1 == int_3 and int_1 != int_2:
        return int_2
    elif int_3 == int_2 and int_1 != int_3:
        return int_1
    else:
        return 0
    
print(lone_sum(1, 2, 3) )
print(lone_sum(3, 2, 3) )
print(lone_sum(3, 3, 3) )