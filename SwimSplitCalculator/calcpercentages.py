import math as m
import os 
from datetime import timedelta
from functions import *
from percentagelistV1 import *

def calcpercentages():
  f = open("percentages.txt", "w").close()
  path = "/Users/alvin/Documents/Coding/SwimSplitCalculator/data"
  for filename in os.listdir(path):
    if filename.find(".txt") != -1: 
        with open(os.path.join(path, filename), 'r') as f: # open in readonly mode
          text = f.readlines()
          size = len(text)
          percentages = []
          f = open("percentages.txt", "a")
          f.write(filename + "\n")
          f.close()
          percentages = percentagelist(text)
          num = splitnumber(text)
          for a in range(num):
            total = every_nth(percentages, num, a)
            avg = total/size
            f = open("percentages.txt", "a")
            f.write(str(avg) + "\n")
            f.close()
          f = open("percentages.txt", "a")
          f.write("-- \n\n")
          f.close()
          percentages = []

calcpercentages()