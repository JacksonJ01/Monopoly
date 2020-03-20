# Creating a class to give the properties in monopoly some characteristics
class Square:
    def __init__(self, name, color, cost, rent):
        self.name = name
        self.color = color
        self.cost = int(cost)
        self.rent = int(rent)

    def des(self):
        return 'You landed on: ' + self.name + "; Color: " + self.color

    def cost(self):
        return self.name + " costs " + str(self.cost)

    def rent(self):
        return 'The rent for ' + self.name + " is " + str(self.rent)


# Regular Property
Mediterranean_Ave = Square("Mediterranean Ave", "Brown", 60, 2)
Baltic_Ave = Square("Baltic Ave", "Brown", 60, 4)
Oriental_Ave = Square("Oriental Ave", "Light Blue", 100, 6)
Vermont_Ave = Square("Vermont Ave", "Pink", 100, 6)
Connecticut_Ave = Square("Connecticut Ave", "Pink", 120, 8)
St_Charles_Place = Square("St. Charles Place", "Pink", 140, 10)
State_Ave = Square("States Ave", "Pink", 140, 10)
Virginia_Ave = Square("Virginia Ave", "Pink", 160, 12)
St_James_Place = Square("St. James Place", "Orange", 180, 14)
Tennessee = Square("Tennessee", "Orange", 180, 14)
New_York_Ave = Square("Ney York Ave", "Orange", 200, 16)
Kentucky_Ave = Square("Kentucky Ave", "Red", 220, 18)
Indiana_Ave = Square("Indiana Ave", "Red", 220, 18)
Illinois_Ave = Square("Illinois", "Red", 240, 20)
Atlantic_Ave = Square("Atlantic Ave", "Yellow", 260, 22)
Ventnor_Ave = Square("Ventnor Ave", "Yellow", 260, 22)
Marvin_Gardens = Square("Marvin Gardens", "Yellow", 280, 24)
Pacific_Ave = Square("Pacific Ave", "Green", 300, 26)
North_Carolina_Ave = Square("North Carolina Ave", "Green", 300, 26)
Pennsylvania = Square("Pennsylvania Ave", "Green", 320, 28)
Park_Place = Square("Park Place", "Green", 350, 35)
Boardwalk = Square("Boardwalk", "Green", 400, 50)

# Special Property
Electric_Company = Square('Electric Company', 'Utilities', 150, 10)
Water_Works = Square('Water Works', 'Utilities', 150, 10)
Reading_Railroad = Square('Reading Railroad', 'Railroad', 200, 25)
Pennsylvania_Railroad = Square('Pennsylvania Railroad', 'Railroad', 200, 25)
B_O_Railroad = Square('B. & O. Railroad', 'Railroad', 200, 25)
Short_Line_Railroad = Square('Short Line Railroad', 'Railroad', 200, 25)
