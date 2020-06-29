import datetime
from datetime import date
import time
import pet

# Create empty array to store instances of pets in
pet_list = []

# Define methods for getting user input
def setName():
    temp_name = input("What is your pet's name?:  ")
    return temp_name

def setCategory():
    temp_category = input("What is the category (mammal, reptile, fish, etc...) that your pet falls in?:  ")
    return temp_category

def setSubtype():
    temp_subtype = input("What is the subtype (dog, snake, goldfish, etc...) that your pet falls in?:  ")
    return temp_subtype

def setBirthdate():
    temp_birthdate = input("What is your pet's birthday? Enter the date in a YYYY-MM-DD format:  ")
    year, month, day = map(int, temp_birthdate.split('-'))
    temp_birthdate = datetime.date(year, month, day)
    return temp_birthdate

def setColors():
    temp_colors = input("What color is your pet?:  ")
    return temp_colors

def setHasTail():
    temp_has_tail = input("Does your pet have a tail?:  ")
    return temp_has_tail

def setHasWings():
    temp_has_wings = input("Does your pet have wings?:  ")
    return temp_has_wings

def setNumOfLegs():
    temp_num_of_legs = input("How many legs does your pet have?:  ")
    return temp_num_of_legs

def setLastFed():
    temp_last_fed = input("When was your pet last fed? Enter the date in a YYYY-MM-DD format:  ")
    year, month, day = map(int, temp_last_fed.split('-'))
    temp_last_fed = datetime.date(year, month, day)
    return temp_last_fed

def setDeathdate():
    temp_deathdate = datetime.date.today()
    return temp_deathdate

# Get info about Pet 1 and store it by creating an instance of the class, and adding that instance (Pet 1) to the array
print("Let's start by gathering basic data about your first pet.\n")
pet_1 = pet.pet(setName(), setCategory(), setSubtype())
pet_list.append(pet_1)

# Get info about Pet 2 and store it by creating an instance of the class, and adding that instance (Pet 1) to the array
print("\nNow let's gather more detailed data about your second pet.\n")
pet_2 = pet.pet(setName(), setCategory(), setSubtype(), setBirthdate(), setColors(), setHasTail(), setHasWings(), setNumOfLegs(), setLastFed(), setDeathdate())
pet_list.append(pet_2)

# Hard code info for Pet 3 and Pet 4, create instances of class for Pet 3 and 4, and add instances to array
print("\nI know you have also have 2 fish, Flotsam and Jetsam.  Let me enter the info I know about them now...")
time.sleep(2)
pet_3 = pet.pet('Flotsam', 'fish', 'goldfish')
pet_3.last_fed = datetime.date.today() - datetime.timedelta(days=1) # Flotsam was fed yesterday
pet_list.append(pet_3)
pet_4 = pet.pet('Jetsam', 'fish', 'betafish')
pet_4.last_fed = datetime.date.today() - datetime.timedelta(days=10) # Jetsam was fed 10 days ago
pet_list.append(pet_4)

# Check if all pets are hungry
for pet in pet_list:
    if not pet.is_fed():
        time.sleep(2)
        print("\nUh oh, " + pet.name + " is hungry!")
        days_hungry = datetime.date.today() - pet.last_fed  # Check how many days it's been since the pet ate
        if days_hungry <= datetime.timedelta(days=3): #  Feed pet if it's been 3 days or last since it ate
            pet.feed(datetime.date.today())
            time.sleep(1)
            print("Don't worry, I fed " + pet.name + " and they're fat and happy now!")
        else: # The pet dies if it's been more than 3 days since it ate
            pet.died(datetime.date.today())
            time.sleep(1)
            print("I have terrible news...it's been more than 3 days since " + pet.name + " was fed. " + pet.name + " has tragically passed away :(")
    else:
        time.sleep(2)
        print("\n" + pet.name + " is already fed, nice job!")
