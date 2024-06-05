# Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a
# program to convert this temperature into Centigrade degrees.

FarenheitTemp = input("What's the Temperature in your city right now? ")

#(°F − 32) × 5/9 
CentiTemp = (float(FarenheitTemp) - 32) * (5/9)
print(FarenheitTemp, "Farenheit in Centigrade will be;s" , CentiTemp, "C")
