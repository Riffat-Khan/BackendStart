# Write a program that takes the marks obtained by a student in five different subjects as
# input through the keyboard, then find out the total marks and percentage marks obtained
# by the student in each subject. Assume that the maximum marks that can be obtained by a
# student in each subject is 100.

print("Kindly enter your marks in\n")
Subj_1 = input("DSA :")
Subj_2 = input("OOP :")
Subj_3 = input("OS :")
Subj_4 = input("CA :")
Subj_5 = input("EC :")

#Total Obtained marks
totalMarks = float(Subj_1) + float(Subj_2) + float(Subj_3) + float(Subj_4) + float(Subj_5)
print("Total marks you got: " , totalMarks)

#Individual subject percentage
print("DSA : " , (float(Subj_1)/100)*100, "%" )
print("OOP : " , (float(Subj_2)/100)*100, "%" )
print("OS : " , (float(Subj_3)/100)*100, "%" )
print("CA : " , (float(Subj_4)/100)*100, "%" )
print("EC : " , (float(Subj_5)/100)*100, "%" )