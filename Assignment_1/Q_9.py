# A company insures its drivers in the following cases:
# − If the driver is married.
# − If the driver is unmarried, male & above 30 years of age.
# − If the driver is unmarried, female & above 25 years of age.
# In all other cases, the driver is not insured. If the marital status, sex and age of the driver
# are the inputs, write a program to determine whether the driver is to be insured or not.

MaritalStatus = input("What's the marital status of the driver? married/unmarried:")
Gender = input("What's the gender of the driver? male/female :")
Age = input("What's the age of the driver:")

if MaritalStatus.lower() == "married": print("Eligible")
elif MaritalStatus.lower() == "unmarried" and Gender.lower() == "male" and int(Age) > 30 : print("Eligible")
elif MaritalStatus.lower() == "unmarried" and Gender.lower() == "female" and int(Age) > 25 : print("Eligible")
else:print("The driver is not insured")