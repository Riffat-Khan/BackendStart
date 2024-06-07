# Develop a program that will determine the gross pay for each of several employees. The
# company pays “straight time” for the first 40 hours worked by each employee and pays
# “time-and-a-half” for all hours worked more than 40 hours. You‟re given a list of the
# employees of the company, the number of hours each employee worked last week and the
# hourly rate of each employee. Your program should input this information for each
# employee and should determine and display the employee's gross pay. Here is a sample
# input/output dialog:
# Enter # of hours worked (-1 to end): 39
# Enter hourly rate of the worker ($00.00): 10.00
# Salary is $390.00
# Enter # of hours worked (-1 to end): 40
# Enter hourly rate of the worker ($00.00): 10.00
# Salary is $400.00
# Enter # of hours worked (-1 to end): 41

# Enter hourly rate of the worker ($00.00): 10.00
# Salary is $415.00
# Enter # of hours worked (-1 to end): -1

workHR = input("Enter # of hours worked (-1 to end):")
rateHR = input("Enter hourly rate of the worker ($00.00):")

if(int(workHR) < 40):
    Salary = int(workHR) * float(rateHR)
    print("Salary is $", float(Salary))
elif int(workHR) > 40:
    extra = int(workHR) - 40
    extraSalary = extra * (float(rateHR)/2)
    Salary = extraSalary + (int(workHR) * float(rateHR))
    print("Salary is $", float(Salary))
else: 
    print("Invalid")
