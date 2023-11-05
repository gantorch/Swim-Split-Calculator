import math as m
import os
from datetime import timedelta

sum=0
print(os.getcwd())
f = open("percentages.txt", "w").close()
a = open("M100freeLCM.txt")
# a = open("M100flyLCM.txt")
with open('M100freeLCM.txt') as f:
# with open('M100flyLCM.txt') as f:
    text = a.readlines()
    size = len(text)

for x in text: 
    f = open("percentages.txt", "a")
    name = x.split(" ")[0] + " " + x.split(" ")[1]
    # print(name)
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
    f.write(name+": "+ str(percentage)+"\n")
    f.close()
    sum=percentage+sum

f = open("percentages.txt", "a")
f.write(str(sum/size))
f.close()