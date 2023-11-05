import math as m
import os 
from datetime import timedelta

sum=0
f = open("percentages.txt", "w").close()
path = "/Users/alvin/Documents/Coding/SwimSplitCalculator/data"
for filename in os.listdir(path):
   print(filename)
   if filename.find(".txt") != -1: 
      with open(os.path.join(path, filename), 'r') as f: # open in readonly mode
        sum=0
        text = f.readlines()
        size = len(text)
        print(size)
        for x in text: 
            name = x.split(" ")[0] + " " + x.split(" ")[1]
            print(name)
            time = x.split(") ")[1]
            # print(time)
            s = x.split("(")[1]
            split = s[0:5]
            # print(split)
            # print("\n")
            ss, msms = map(int, time.split('.'))
            t1 = timedelta(seconds=ss, milliseconds=msms*10)
            ss, msms = map(int, split.split('.'))
            t2 = timedelta(seconds=ss, milliseconds=msms*10)
            # print(t1, t2)
            percentage = t2/t1
            # f.write(name+": "+ str(percentage)+"\n")
            # f.close()
            sum=percentage+sum

        f = open("percentages.txt", "a")
        f.write(filename + " - " + str(sum/(size)) + "\n")
        f.close()