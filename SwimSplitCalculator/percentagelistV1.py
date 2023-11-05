import math as m
import os 
from datetime import timedelta

def percentagelist(text):
    percentages = []
    for x in text: 
        name = x.split(" (")[0] # extract name 
        time = x.split(") ")[1] # extract time 
        s = x.split("(")[1]
        start = x.index("(")
        end = x.index(")")
        splits = x[start+1:end] # extract splits in whole
        num = s.count(",") + 1 # number of splits
        for i in range(0, len(splits), 7):
            split = s[i:i+5]

            # Splitting time string
            time_parts = time.split(':')
            mm = int(time_parts[0]) if len(time_parts) > 1 else 0
            ss, msms = map(int, time_parts[-1].split('.'))
            
            # Creating timedelta object for t1
            t1 = timedelta(minutes=mm, seconds=ss, milliseconds=msms * 10)

            # Splitting split string
            ss, msms = map(int, split.split('.'))

            # Creating timedelta object for t2
            t2 = timedelta(seconds=ss, milliseconds=msms * 10)
            
            # ss, msms = map(int, time.split('.'))
            # t1 = timedelta(seconds=ss, milliseconds=msms*10)
            # ss, msms = map(int, split.split('.'))
            # t2 = timedelta(seconds=ss, milliseconds=msms*10)

            # print(t1, t2)
            percentage = t2/t1
            percentages.append(percentage)
    return percentages

def splitnumber(text):
    for x in text: 
        s = x.split("(")[1]
        num = s.count(",") + 1 
        return num
        
