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

    def getName(self):
        self.name = input("What is your pet's name?:  ")

    def getCategory(self):
        self.category = input("What is the category (mammal, reptile, fish, etc...) that your pet falls in?:  ")

    def getSubtype(self):
        self.subtype = input("What is the subtype (dog, snake, goldfish, etc...) that your pet falls in?:  ")

    def getBirthdate(self):
        self.birthdate = input("What is your pet's birthday? Enter the date in a YYYY-MM-DD format:  ")
        year, month, day = map(int, self.birthdate.split('-'))
        self.birthdate = datetime.date(year, month, day)

    def getColors(self):
        self.colors = input("What color is your pet?:  ")

    def getHasTail(self):
        self.has_tail = input("Does your pet have a tail?:  ")

    def getHasWings(self):
        self.has_wings = input("Does your pet have wings?:  ")

    def getNumOfLegs(self):
        self.num_of_legs = input("How many legs does your pet have?:  ")

    def getLastFed(self):
        self.last_fed = input("When was your pet last fed? Enter the date in a YYYY-MM-DD format:  ")
        year, month, day = map(int, self.last_fed.split('-'))
        self.last_fed = datetime.date(year, month, day)

    def age(self):
        age = datetime.date.today().year - self.birthdate.year
        return age

    def is_fed(self):
        if datetime.date.today() == self.last_fed:
            return True
        else:
            return False

    def feed(self, feed_date):
        self.last_fed = datetime.date.today()

    def died(self, deceased_date):
        self.deathdate = datetime.date.today()
