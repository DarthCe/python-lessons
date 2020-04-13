#Temperature Conversion Tool
import time

unit_range = ["C","F","K"]

print("Welcome to the Temperature Conversion Tool!")
time.sleep(2)

# Loop forever
while True:

    # Get the starting unit
    convert_from = input("\nWhat do you want to convert from? Type C for Celsius, F for Fahrenheit, or K for Kelvin: ").strip().upper()
    while convert_from not in unit_range:
        convert_from = input("Please only type C for Celsius, F for Fahrenheit, or K for Kelvin: ").strip().upper()


    # Get the unit to convert to
    time.sleep(1)
    convert_to = input("\nWhat do you want to convert to? Type C for Celsius, F for Fahrenheit, or K for Kelvin: ").strip().upper()
    while convert_to not in unit_range:
        convert_to = input("Please only type C for Celsius, F for Fahrenheit, or K for Kelvin: ").strip().upper()


    # Create a string with the full name of their convert to and from
    if convert_from == "C":
        convert_from = "Celsius"
    elif convert_from == "F":
        convert_from = "Fahrenheit"
    elif convert_from == "K":
        convert_from = "Kelvin"
    if convert_to == "C":
        convert_to = "Celsius"
    elif convert_to == "F":
        convert_to = "Fahrenheit"
    elif convert_to == "K":
        convert_to = "Kelvin"


    # Get the temp they're trying to convert
    time.sleep(1)
    temp = float(input("\nWhat's the temperature (in " + convert_from + ") that you want to convert? "))
    time.sleep(1)


    # Defining conversion functions
    def celsiusToFahrenheit ():
        converted_temp = float(((temp/5)*9)+32)
        print("\n" + str(temp) + " in Celsius is " + str(converted_temp) + " in Fahrenheit!")
        
    def fahrenheitToCelsius ():
        converted_temp = float(((temp-32)*5)/9)
        print("\n" + str(temp) + " in Fahrenheit is " + str(converted_temp) + " in Celsius!")
        
    def celsiusToKelvin ():
        converted_temp = float(temp+273.15)
        print("\n" + str(temp) + " in Celsius is " + str(converted_temp) + " in Kelvin!")
        
    def kelvinToCelsius ():
        converted_temp = float(temp-273.15)
        print("\n" + str(temp) + " in Kelvin is " + str(converted_temp) + " in Celsius!")
        
    def fahrenheitToKelvin ():
        converted_temp = float((((temp-32)*5)/9)+273.15)
        print("\n" + str(temp) + " in Fahrenheit is " + str(converted_temp) + " in Kelvin!")
        
    def kelvinToFahrenheit ():
        converted_temp = float((((temp-273.15)/5)*9)+32)
        print("\n" + str(temp) + " in Kelvin is " + str(converted_temp) + " in Fahrenheit!")


    # Do the conversions
    if convert_from == "Celsius" and convert_to == "Fahrenheit":
        celsiusToFahrenheit()

    elif convert_from == "Fahrenheit" and convert_to == "Celsius":
        fahrenheitToCelsius()
        
    elif convert_from == "Celsius" and convert_to == "Kelvin":
        celsiusToKelvin()
        
    elif convert_from == "Kelvin" and convert_to == "Celsius":
        kelvinToCelsius()
        
    elif convert_from == "Fahrenheit" and convert_to == "Kelvin":
        fahrenheitToKelvin()
        
    elif convert_from == "Kelvin" and convert_to == "Fahrenheit":
        kelvinToFahrenheit()
