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


Mediterranean_Ave = Square("Mediterranean Ave", "Brown", 60, 0)
Baltic_Ave = Square("Baltic Ave", "Brown", 60, 0)
Oriental_Ave = Square("Oriental Ave", "Light Blue", 100, 0)
Vermont_Ave = Square("Vermont Ave", "Pink", 100, 0)
Connecticut_Ave = Square("Connecticut Ave", "Pink", 120, 0)
St_Charles_Place = Square("St. Charles Place", "Pink", 140, 0)
State_Ave = Square("States Ave", "Pink", 140, 0)
Virginia_Ave = Square("Virginia Ave", "Pink", 160, 0)
St_James_Place = Square("St. James Place", "Orange", 180, 0)
Tennessee = Square("Tennessee", "Orange", 180, 0)
New_York_Ave = Square("Ney York Ave", "Orange", 200, 0)
Kentucky_Ave = Square("Kentucky Ave", "Red", 220, 0)
Indiana_Ave = Square("Indiana Ave", "Red", 220, 0)
Illinois_Ave = Square("Illinois", "Red", 240, 0)
Atlantic_Ave = Square("Atlantic Ave", "Yellow", 260, 0)
Ventnor_Ave = Square("Ventnor Ave", "Yellow", 260, 0)
Marvin_Gardens = Square("Marvin Gardens", "Yellow", 280, 0)
Pacific_Ave = Square("Pacific Ave", "Green", 300, 0)
North_Carolina_Ave = Square("North Carolina Ave", "Green", 300, 0)
Pennsylvania = Square("Pennsylvania Ave", "Green", 320, 0)
Park_Place = Square("Park Place", "Green", 350, 0)
Boardwalk = Square("Boardwalk", "Green", 400, 0)
