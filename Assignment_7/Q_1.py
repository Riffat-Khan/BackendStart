# i. Write a program which should count Vowels in the strings and return vowels in reverse order.

string = " jelliyobean"
vowels = []
count = 0
for i in string:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count +=1
        vowels.append(i)
        
for i in range(len(vowels)):
    i+=1
    print(vowels[-i] , end = " ")