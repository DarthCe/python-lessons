import time

#build the array with user input
employeeList = [input("Enter the first employee's name: "), input("Enter the second employee's name: "), input("Enter the third employee's name: "), input("Enter the fourth employee's name: "), input("Enter the fifth employee's name: "), input("Enter the sixth employee's name: "), input("Enter the seventh employee's name: "), input("Enter the eighth employee's name: "), input("Enter the ninth employee's name: "), input("Enter the tenth employee's name: ")]

#access the array elements
emp3 = employeeList[2]
emp5 = employeeList[4]
emp7 = employeeList[6]

#print everything out
time.sleep(1.5)
print("\nThanks!")
time.sleep(1.5)
print("\nYou ready for some array magic?!")
time.sleep(1.5)
print("\nThe third employee in the list is "+emp3+".")
print("The fifth employee in the list is "+emp5+".")
print("The seventh employee in the list is "+emp7+".")
