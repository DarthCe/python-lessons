import datetime

# Define class
class pet:
    
    def __init__(self, name, category, subtype, birthdate = None, colors = None, has_tail = False, has_wings = False, num_of_legs = 4, last_fed = datetime.date.today(), deathdate = None):
        self.name = name
        self.category = category
        self.subtype = subtype
        self.birthdate = birthdate
        self.colors = colors
        self.has_tail = has_tail
        self.has_wings = has_wings
        self.num_of_legs = num_of_legs
        self.last_fed = last_fed
        self.deathdate = deathdate

    def age(self): # Calculate age
        age = datetime.date.today().year - self.birthdate.year
        return age

    def is_fed(self): # If the pet was fed today, then it's considered fed
        if datetime.date.today() == self.last_fed:
            return True
        else:
            return False

    def feed(self, feed_date): # Feed the pet by setting last_fed to today
        self.last_fed = datetime.date.today()

    def died(self, deceased_date): # Record the pet's deathdate as today
        self.deathdate = datetime.date.today()
