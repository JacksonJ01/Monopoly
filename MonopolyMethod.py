from Monopoly import *
characters = []
choose = [battleship[1], boot[1], cannon[1], horse_rider[1], iron[1], racecar[1], dog[1], thimble[1], top_hat[1], wheel_barrow[1]]


def character_choosing():
    a = 1
    while a <= playing:
        print("Choose your character player", a)

        print("You can choose:", choose)
        option = input(">>>").title()
        if option == "Battleship" or option == "Battle" or option == "Ship" or option == "Bs":
            characters.append(battleship)
            choose.remove(battleship[1])
        elif option == "Boot" or option == "B":
            characters.append(boot)
            choose.remove(boot[1])
        elif option == "Cannon" or option == "C":
            characters.append(cannon)
            choose.remove(cannon[1])
        elif option == "Horse" or option == "Rider" or option == "H" or option == "R":
            characters.append(horse_rider)
            choose.remove(horse_rider[1])
        elif option == "Iron" or option == "I":
            characters.append(iron)
            choose.remove(iron[1])
        elif option == "Racecar" or option == "Car" or option == "Rc":
            characters.append(racecar)
            choose.remove(racecar[1])
        elif option == "Dog" or option == "D":
            characters.append(dog)
            choose.remove(dog[1])
        elif option == "Thimble" or option == "T":
            characters.append(thimble)
            choose.remove(thimble[1])
        elif option == "Top Hat" or option == "Th":
            characters.append(top_hat)
            choose.remove(top_hat[1])
        elif option == "Wheel Barrow" or option == "Wheel" or option == "Barrow" or option == "W" or option == "Wb":
            characters.append(wheel_barrow)
            choose.remove(wheel_barrow[1])

        if a != playing:
            print("Alright, next up")
        elif a == playing:
            print("Let's continue")

        a += 1


def rules():
    print("The rules goes as follows:"
          "\nEach player will roll the 2 die in an attempt to get the highest value"
          "\n")
    return


character_choosing()

print("Okay so we have")
for character in characters:
    print("The", character[1])

print("Now to determine who goes first...")
print("Wait, do you want to hear the rules?")
rule = input(">>>").title()
if rule == "Yes" or rule == "Y":
    rules()
elif rule == "No" or rule == "N":
    print("Okay, that speeds things up a bit")
