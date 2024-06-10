# Implement the following integer functions:
# i. A Function Celsius that returns the Celsius equivalent of a Fahrenheit temperature.
# ii. A Function Fahrenheit returns the Fahrenheit equivalent of a Celsius temperature.
# iii. Use these functions to write a program that prints charts showing the Fahrenheit
# equivalents of all Celsius temperatures from 0 to 100 degrees, and the Celsius equivalents
# of all Fahrenheit temperatures from 32 to 212 degrees. Print the outputs in a tabular format
# that minimizes the number of lines of output while remaining readable.

def Celsius(FarenheitTemp):
    CentiTemp = (FarenheitTemp - 32) * (5/9)
    print(FarenheitTemp, "F in Centigrade will be %f " %(CentiTemp), "C")

def Farenheit(CelsiusTemp):
    FarenheitTemp = (CelsiusTemp + 32) * (9/5)
    print(CelsiusTemp, "C in Farenheit will be %f" %(FarenheitTemp), "F")

def TempChart():
    startCelsius = 0
    while(startCelsius <= 100):
        Celsius(FarenheitTemp=startCelsius)
        startCelsius +=1

    startFarenheit = 32
    while(startFarenheit <= 212):
        Farenheit(CelsiusTemp=startFarenheit)
        startFarenheit +=1

TempChart()