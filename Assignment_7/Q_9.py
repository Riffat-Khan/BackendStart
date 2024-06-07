# ix. You are provided a string with only digits [0 - 9], your task is to count the
# number of subsequences of string divisible by 6.
# For e.g. The given string is 1234566
# The subsequences divisible by 6 are 12, 24, 36, 6, 6, 66
# Hence the answer should be 6

def subsequencesDiv6(string):
    arr = list(string)
    count = 0

    subsequencesArr = []
    for i in range(len(string) -1):
        for j in range(i+1, len(string)):
            pair = string[i]+string[j]
            subsequencesArr.append(pair)

    unique = []
    for value in range(len(subsequencesArr)-1):
        duplicate = 0
        for nextVal in range(value+1 , len(subsequencesArr)):
            if value == nextVal:
                duplicate +=1
        if duplicate == 0:
            unique.append(subsequencesArr[value])

    for numb in unique:
        if int(numb) % 6 == 0:
            count+=1

    for num in string:
        Number = int(num)
        if Number %6 == 0:
            count +=1

    print(count)


subsequencesDiv6(string="1234566")