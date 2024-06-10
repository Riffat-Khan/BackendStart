# iv. Given a string and a non-negative int a, return a larger string that is n copies of
# the original string. 
# string_times(Hi, 2) → HiHi
# string_times(Hi, 3) → HiHiHi
# string_times(Hi, 1) → Hi

def copyStr(string , times):
    print(string*times , end="")

copyStr(string="hi" , times=5)