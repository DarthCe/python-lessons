# Temperature Conversion Tool
# by Cesare Tidler

# Initialize things to use later
import time
unit_range = ["C","F","K"]
quit_value = ""


# Defining conversion functions
def celsiusToFahrenheit (c):
    f = float(((c/5)*9)+32)
    return f
    
def fahrenheitToCelsius (f):
    c = float(((f-32)*5)/9)
    return c
    
def celsiusToKelvin (c):
    k = float(c+273.15)
    return k
    
def kelvinToCelsius (k):
    c = float(k-273.15)
    return c
    
def fahrenheitToKelvin (f):
    k = float((((f-32)*5)/9)+273.15)
    return k
    
def kelvinToFahrenheit (k):
    f = float((((k-273.15)/5)*9)+32)
    return f


# Start the program
print("Welcome to the Temperature Conversion Tool!")
time.sleep(2)


# Loop forever
while quit_value != "Q":


    # Get the starting unit
    convert_from = input("\nWhat do you want to convert from? Type C for Celsius, F for Fahrenheit, or K for Kelvin: ").strip().upper()
    while convert_from not in unit_range:
        convert_from = input("Please only type C for Celsius, F for Fahrenheit, or K for Kelvin: ").strip().upper()


    # Get the unit to convert to
    time.sleep(1)
    convert_to = input("\nWhat do you want to convert to? Type C for Celsius, F for Fahrenheit, or K for Kelvin: ").strip().upper()
    while (convert_to not in unit_range) or (convert_to == convert_from):
        convert_to = input("Please only type either C, F, or K, and make sure it's different than the one you're converting from: ").strip().upper()


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


    # Do the conversions
    if convert_from == "Celsius" and convert_to == "Fahrenheit":
        converted_temp = celsiusToFahrenheit(temp)
        
    elif convert_from == "Fahrenheit" and convert_to == "Celsius":
        converted_temp = fahrenheitToCelsius(temp)
        
    elif convert_from == "Celsius" and convert_to == "Kelvin":
        converted_temp = celsiusToKelvin(temp)
        
    elif convert_from == "Kelvin" and convert_to == "Celsius":
        converted_temp = kelvinToCelsius(temp)
        
    elif convert_from == "Fahrenheit" and convert_to == "Kelvin":
        converted_temp = fahrenheitToKelvin(temp)
        
    elif convert_from == "Kelvin" and convert_to == "Fahrenheit":
        converted_temp = kelvinToFahrenheit(temp)


    # Print the results and give the option to continue or quit
    print("\n" + str(temp) + " in " + convert_from + " is " + str(converted_temp) + " in " + convert_to + "!")
    quit_value = input("   If you want to quit, type Q and press Enter.  Otherwise, press Enter to run it again! ").strip().upper()
