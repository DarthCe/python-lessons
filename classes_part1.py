import datetime
import time
import pet

# Create empty array to store instances of pets in
pet_list = []

# Get info about Pet 1 and store it
print("Let's start by gathering basic data about your first pet.\n")
pet_1 = pet.pet('','','')
pet_1.getName()
pet_1.getCategory()
pet_1.getSubtype()
#   Add Pet 1 to array
pet_list.append(pet_1)

# Get info about Pet 2 and store it
print("\nNow let's gather more detailed data about your second pet.\n")
pet_2 = pet.pet('','','')
pet_2.getName()
pet_2.getCategory()
pet_2.getSubtype()
pet_2.getBirthdate()
pet_2.getColors()
pet_2.getHasTail()
pet_2.getHasWings()
pet_2.getNumOfLegs()
pet_2.getLastFed()
#   Add Pet 2 to array
pet_list.append(pet_2)

# Hard code info for Pet 3 and Pet 4
print("\nI know you have also have 2 fish, Flotsam and Jetsam.  Let me enter the info I know about them now...")
time.sleep(2)
#   Add Pet 3 to array
pet_3 = pet.pet('Flotsam', 'fish', 'goldfish', '', '', '', '', '', datetime.date.today() - datetime.timedelta(days=1), '')
pet_list.append(pet_3)
#   Add Pet 4 to array
pet_4 = pet.pet('Jetsam', 'fish', 'betafish', '', '', '', '', '', datetime.date.today() - datetime.timedelta(days=10), '')
pet_list.append(pet_4)

# Check if all pets are hungry
for pet in pet_list:
    if not pet.is_fed():
        time.sleep(2)
        print("\nUh oh, " + pet.name + " is hungry!")
        #  Check how many days it's been since the pet ate
        days_hungry = datetime.date.today() - pet.last_fed
        #  Feed pet if it's been 3 days or last since it ate
        if days_hungry <= datetime.timedelta(days=3):
            pet.feed(datetime.date.today())
            time.sleep(1)
            print("Don't worry, I fed " + pet.name + " and they're fat and happy now!")
        #  The pet dies if it's been more than 3 days since it ate
        else:
            pet.died(datetime.date.today())
            time.sleep(1)
            print("I have terrible news...it's been more than 3 days since " + pet.name + " was fed. " + pet.name + " has tragically passed away :(")
    else:
        time.sleep(2)
        print("\n" + pet.name + " is already fed, nice job!")
