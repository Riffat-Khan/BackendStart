# A university has the following rules for a student to qualify for a degree with A as the
# main subject and B as the subsidiary subject:
# (a) He should get 55 percent or more in A and 45 percent or more in B.
# (b) If he gets than 55 percent in A he should get 55 percent or more in B. However, he
# should get at least 45 percent in A.
# (c) If he gets less than 45 percent in B and 65 percent or more in A he can reappear in an
# examination in B to qualify.
# (d) In all other cases he is declared to have failed.
# Write a program to receive marks in A and B and Output whether the student has passed, failed
# or can reappear in B.

mainSubj = input("Enter % marks in A [main SUBJECT]:")
subsidiarySubj = input("Enter % marks in B [subsidiary SUBJECT]:")

if(float(mainSubj) >= 55 or float(subsidiarySubj) >= 45) : Status = "passed"
elif((float(mainSubj) < 55 and (float(mainSubj)>45)) and float(subsidiarySubj) >= 55): Status = "passed"
elif(float(mainSubj) >= 65 and float(subsidiarySubj) < 45) : Status = "reappear"
else: Status = "failed"

print("The student has : " , Status)

