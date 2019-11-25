# Jackson J.
# 11/24/19
# My mom told me to make monopoly, so i will try
"""I have to try to make a turn based algorithm and characters have rotate"""

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

battleship = [1]
boot = [1]
cannon = [1]
horse_rider = [1]
iron = [1]
racecar = [1]
dog = [1]
thimble = [1]
top_hat = [1]
wheel_barrow = [1]

input("CLICK HERE THEN PRESS ENTER")
print("How many people will be playing")
playing = int(input(">>>"))
