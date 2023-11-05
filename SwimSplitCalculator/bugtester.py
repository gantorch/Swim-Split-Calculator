import math as m
import os 
from datetime import timedelta
from functions import *
from percentagelistV1 import *

def calcpercentages():
  f = open("bugtester.txt", "w").close()
  f = open("/Users/alvin/Documents/Coding/SwimSplitCalculator/data/M1500freeLCM.txt", "r")
  text = f.readlines()
  size = len(text)
  filename = "test"
  percentages = []
  f = open("bugtester.txt", "a")
  f.write(filename + "\n")
  f.close()
  percentages = percentagelist(text)
  num = splitnumber(text)
  for a in range(num):
    total = every_nth(percentages, num, a)
    avg = total/size
    f = open("bugtester.txt", "a")
    f.write(str(avg) + "\n")
    f.close()
  f = open("bugtester.txt", "a")
  f.write("-- \n\n")
  f.close()
  percentages = []

calcpercentages()