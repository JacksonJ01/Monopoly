# Jackson J.
# 11/24/19
# My mom told me to make monopoly, so i will try
"""I have to try to make a turn based algorithm and characters have the turns rotate"""
from MonopolyMethod import *
from time import sleep
input("CLICK HERE THEN PRESS ENTER")

character_choosing()

print("\nOkay so we have:")
for character in characters:
    print("The", character[1])

print("\nNow to determine who goes first...")
print("Wait, do you want to hear the rules?")
rule = input(">>>").title()
if rule == "Yes" or rule == "Y":
    rules()
elif rule == "No" or rule == "N":
    print("\nOkay, that speeds things up a bit")

b = 1
for character in characters:
    rn = randint(1, 6)
    print(f"\nOkay {character[1]}, you're up")
    sleep(.05)
    if character[1] == "Battle Ship":
        battleship.append(rn)
        print("You rolled", rn)
    elif character[1] == "Boot":
        boot.append(rn)
        print("You rolled", rn)
    elif character[1] == "Cannon":
        cannon.append(rn)
        print("You rolled", rn)
    elif character[1] == "Horse Rider":
        horse_rider.append(rn)
        print("You rolled", rn)
    elif character[1] == "Iron":
        iron.append(rn)
        print("You rolled", rn)
    elif character[1] == "Racecar":
        racecar.append(rn)
        print("You rolled", rn)
    elif character[1] == "Dog":
        dog.append(rn)
        print("You rolled", rn)
    elif character[1] == "Thimble":
        thimble.append(rn)
        print("You rolled", rn)
    elif character[1] == "Top Hat":
        top_hat.append(rn)
        print("You rolled", rn)
    elif character[1] == "Wheel Barrow":
        wheel_barrow.append(rn)
        print("You rolled", rn)
    b += 1

print("\nNow lets see who had the highest roll")

highest = [0]
higher = 0
this = 0
for char in characters:
    if char[3] > higher:
        higher = char[3]
        highest.clear()
        highest.append(char[1])
    elif char[3] == higher:
        highest.append(char[1])
    characters[this].pop()
    this += 1
try:
    for character in characters:
        if highest[1] == character:
            break
    place_holder = 0
    while place_holder != str:
        print('\nLooks like we have to roll again for you top rollers:',
              highest, '\n')
        for high in highest:
            rn = randint(1, 15)
            print(high, "\b:", rn, '\n')
            if high == "Battle Ship":
                battleship.append(rn)
            elif high == "Boot":
                boot.append(rn)
            elif high == "Cannon":
                cannon.append(rn)
            elif high == "Horse Rider":
                horse_rider.append(rn)
            elif high == "Iron":
                iron.append(rn)
            elif high == "Racecar":
                racecar.append(rn)
            elif high == "Dog":
                dog.append(rn)
            elif high == "Thimble":
                thimble.append(rn)
            elif high == "Top Hat":
                top_hat.append(rn)
            elif high == "Wheel Barrow":
                wheel_barrow.append(rn)
        higher = 0
        tricked = 0
        this = 0
        for char1 in characters:
            try:
                if char1[3] > higher:
                    higher = char1[3]
                    highest.clear()
                    highest.append(char1[1])
                elif char1[3] == higher:
                    highest.append(char1[1])
                for character in characters:
                    try:
                        if character[3] != 20:
                            characters[this].pop()
                            this += 1
                    except IndexError:
                        this += 1
            except IndexError:
                tricked += 1
                this += 1
        try:
            for character in characters:
                if highest[1] == character:
                    print('How... how did you manage to match again?')
        except IndexError:
            for char2 in characters:
                if char2[1] == highest[0]:
                    characters.remove(char2)
                    characters.insert(0, char2)
                    print(char2[1], 'came out on top')
            break
except IndexError:
    for char3 in characters:
        if char3[1] == highest[0]:
            characters.remove(char3)
            characters.insert(0, char3)
            print('\nHey, looks like', char3[1], 'is the victor')
            break
print(characters)
