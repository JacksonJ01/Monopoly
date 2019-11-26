# Jackson J.
# 11/24/19
# My mom told me to make monopoly, so i will try
"""I have to try to make a turn based algorithm and characters have the turns rotate"""
from MonopolyMethod import *

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
    print("Okay, that speeds things up a bit")
