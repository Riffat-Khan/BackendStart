# Write a program that inputs three different integers from the keyboard (i.e num1, num2,
# num3), then prints the sum, the average, the product, the smallest and the largest of these
# numbers. The screen dialogue should appear as follows:
# Enter three different integers: 13 27 14
# Sum is 54
# Average is 18
# Product is 4914
# Smallest is 13
# Largest is 27

num1 , num2 , num3 = input("Enter three different integers \t").split()
Sum = int(num1) + int(num2) + int(num3)
Average = Sum /3
Product = int(num1) * int(num2) * int(num3)
if(int(num1)> int(num2) and  int(num1) > int(num3)):  
    Largest = int(num1)
elif(int(num2)> int(num1) and  int(num2) > int(num3)):
    Largest = int(num2)
elif(int(num3)> int(num1) and  int(num3) > int(num2)):  
    Largest = int(num3)

if(int(num1) < int(num2) and  int(num1) > int(num3)):  
    Smallest = int(num1)
elif(int(num2) < int(num1) and  int(num2) > int(num3)):
    Smallest = int(num2)
elif(int(num3) < int(num1) and  int(num3) > int(num2)):  
    Smallest = int(num3)

print("Sum is" , Sum)
print("Average is" , Average)
print("Product is" , Product)
print("Smallest is" , Smallest)
print("Largest is" , Largest)