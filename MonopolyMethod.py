from random import *
rn = randint(2, 12)

Monopoly_Board = {"Go": 1, "Mediterranean Ave": 2, "Community Chest 1": 3, "Baltic Ave": 4, "Income Tax": 5, "Reading Railroad": 6, "Oriental Ave": 7, "Chance 1": 8, "Vermont Ave": 9, "Connecticut Ave": 10,
                  "Just Visiting": 11, "St. Charles place": 12, "Electric Company": 13, "States Ave": 14, "Virginia Ave": 15, "Pennsylvania Railroad": 16, "St. James Place": 17, "Community 2": 18, "Tennessee Ave": 19, "New York Ave": 20,
                  "Free Parking": 21, "Kentucky Ave": 22, "Chance 2": 23, "Indiana Ave": 24, "Illinois Ave": 25, "BO Railroad": 26, "Atlantic Ave": 27, "Ventnor Ave": 28, "Water Works": 29, "Marvin Gardens": 30,
                  "Jail": 31, "Pacific Ave": 32, "North Carolina Ave": 33, "Community Chest 3": 34, "Pennsylvania Ave": 35, "Short Line": 36, "Chance 3": 37, "Park Place": 38, "Luxury Tax": 39, "Boardwalk": 40,
                  "Collect": 41}

Chance = {1: "Advance To Go", 2: "Advance To Illinois Ave \nIf you pass Go, collect $200", 3: "Advance To St. Charles Place \nIf you pass Go, collect $200", 4: "Advance To Nearest Utility \nIf Unowned, you can buy it from the BANK \nIf Owned you must Roll The Dice and pay the Owner 10 times the amount rolled",
          5: "Advance To The Nearest Railroad \nIf Unowned, you may buy from the BANK \nIf Owned you must pay the Owner twice the rent stated", 6: "BANK Pays You $50", 7: "Get Out Of Jail Card", 8: "Go Back 3 Spaces",
          9: "Go To Jail", 10: "Make General Repairs On Your Property \n$25 for each house\n$100 for each hotel", 11: "Pay Poor Tax Of $15", 12: "Take A Trip To Reading Railroad \nIf you pass Go, collect $200",
          13: "Move To Boardwalk", 14: "You Have Been Elected Chairmen Of The Board \nPay each player $50", 15: "Your Building And Loans Mature \nCollect $150", 16: "You Won A Crossword Competition \nCollect $100"}

Community_Chest = {1: "Advance To Go", 2: "BANK Error In Your Favor \nCollect $200", 3: "Doctor's Fee \nPay $50",
                   4: "Your Stock Has Been Sold \nYou Get $50", 5: "Get Out Of Jail Free", 6: "Go To Jail",
                   7: "Grand Opera Night \nCollect $50 from each player", 8: "Holiday Fund Matures \nReceive $100", 9: "Income Tax Refund \n Collect $20",
                   10: "It's Your Birthday \nCollect $10", 11: "Life Insurance Matures \n Collect $100", 12: "Pay Hospital Fees of $100",
                   13: "Pay School Fees Of $150", 14: "Receive $25 Consultancy Fee", 15: "You Are Assessed For Street Repairs \n$40 per house \n$115 per hotel",
                   16: "You Have Won The Second Place Prize In A Beauty Contest \nCollect $10", 17: "You Inherit $100"}

# The value at 0 is the position
# The value at 1 is the name of the character piece for the user
# There will be other values at the other positions in the list to hold Money and get out of Jail Cards#
battleship = [1, "Battleship"]
boot = [1, "Boot"]
cannon = [1, "Cannon"]
horse_rider = [1, "Horse Rider"]
iron = [1, "Iron"]
racecar = [1, "Racecar"]
dog = [1, "Dog"]
thimble = [1, "Thimble"]
top_hat = [1, "Top Hat"]
wheel_barrow = [1, "Wheel Barrow"]

characters = []
choose = [battleship[1], boot[1], cannon[1], horse_rider[1], iron[1], racecar[1], dog[1], thimble[1], top_hat[1], wheel_barrow[1]]


def character_choosing():
    print("How many people will be playing")
    playing = int(input(">>>"))
    a = 1
    while a <= playing:
        print("\nChoose your character player", a)

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
    return playing


def rules():
    print("\n\nThe rules goes as follows:"
          "\nEach player will roll the 2 die in an attempt to get the highest value"
          "\nWhoever has the highest value starts first"
          "\nWhenever you land on a land that no one owns, you can buy it from the bank. If you do not want to buy it the Banker sells it at an auction"
          "\nAll of the prices for the land are on the board. Once you own the land, players must pay a rent if they land on your land"
          "\nIf you land on a Chance or a Community Chest card, you must do what it says"
          "\nIf you roll doubles you will have to roll again"
          "\nIf you roll 3 doubles in a row you must go to jail"
          "\nWhen you pass go you will collect $200")
    input("\nPRESS ENTER")

    print("\n\nJail:"
          "\nThere are three ways to get into jail:"
          "\n1)You land on the space labeled Go To Jail"
          "\n2)You pick a Chance or Community Chest card that says Go to Jail"
          "\n3)You roll doubles three times"
          "\nAnd there are also three ways to get out of jail:"
          "\n1)You get three turns to roll a double, if you do not roll a double in the three turns you must pay the fine"
          "\n2)Using a Get out of Jail Free card, which can be obtained in Chance or Community Chest cards)"
          "\n3)Pay a fine of $50")
    input("\nPRESS ENTER")

    print("\n\nLand, houses, and hotels:"
          "\nOnce you own all land of one color, you can start to build houses"
          "\nHouses make the land more costly and every time you add a house the price goes up more"
          "\nOnce there are four houses on each land you can get 1 hotel which replaces the four houses"
          "\nYou can sell any land to another player (at any cost)"
          "\nIf you have houses or a hotel you must sell them back to the bank one house at a time"
          "\nIf you are going to mortgage land to the bank, you have to sell houses or hotels back first"
          "\nYou can find the price of the mortgage on the back of the deed card. If the land has been mortgaged, rent cannot be collected"
          "\nTo unmortgage land, you have to pay the mortgage plus 10% interest")
    input("\nPRESS ENTER")

    print("\n\nBankruptcy:"
          "\nIf you are bankrupt, you cannot pay someone rent or cannot pay a tax"
          "\nIF YOU DECLARE BANKRUPTCY YOU ARE OUT OF THE GAME")

    input("\n\nPRESS ENTER IF YOU UNDERSTAND AND HAVE READ THE RULES")
    return
