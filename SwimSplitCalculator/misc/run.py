import math as m 
from datetime import timedelta

print("Welcome to the Swim Split Calculator! \nFollow the prompts. Press q to exit anytime.")
length = input("Yards or Meters? ")
match = False
while match == False: 
    length = input("Invalid. Is your pool in yards or meters? ")
    if length == "Yards" or "yards" or "y" or "Meters" or "meters" or "m": 
        match = True
    else: 
        match = False

if length == "Yards" or "yards" or "y": 
    print("initiating yards calc")

elif length == "Meters" or "meters" or "m": 
    print("initiating meters calc")


