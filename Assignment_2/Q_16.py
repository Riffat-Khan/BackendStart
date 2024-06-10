# Implement a program that starts by asking the user to enter a login id (i.e., a string). The
# program then checks whether the id entered by the user is in the list ['Ahmad', 'Zainab',
# 'Hina', 'Ali'] of valid users. Depending on the outcome, an appropriate message should be
# printed. Regardless of the outcome, your function should print “Done” before terminating.
# Here is an example of a successful login:
# >>>
# Login: Ali
# You are in!
# Done.

def authentication(name):
    name = input("Enter your name : ")

    students = ['Ahmad', 'Zainab', 'Hina', 'Ali']
    start = 0
    count = 0
    while start < len(students): 
        if name.lower() == students[start].lower(): count+=1 
        start+=1
    if count>=1 : print("You are in!")
    else: print("You are an imposter!")
    print('Done.')

authentication(name="")