import math as m
import os 
import datetime
from datetime import timedelta
from functions import *
from percentagelistV1 import *
from calcpercentages import *
from re import template
from flask import Flask, render_template, request
app = Flask(__name__) 

@app.route('/')
def start():
    return render_template('start.html.j2')

@app.route('/calcyards', methods=['GET'])
def calcyards():
    return render_template('calc-yards.html.j2')

@app.route('/calcmeters', methods=['GET'])
def calcmeters():
    m = request.values.get("mm")
    s = request.values.get("ss")
    ms = request.values.get("ms")
    stroke = request.values.get("stroke")
    dist = request.values.get("distance")
    g = request.values.get("gender")
    if stroke == None or dist == None or g == None: 
        return render_template('calc-meters.html.j2', empty=True)
    if m == "": 
        m = 0
    if s == "": 
        s = 0
    if ms == "": 
        ms = 0
    results = []
    distdisplay = []
    iterator = []
    if m != None and s != None and ms != None: 
        dist = int(dist)
        if len(str(ms)) == 1: 
            ms = str(ms) + "0"
        time = int(m)*60+int(s)+(int(ms)/100)
        query= g.upper()+str(dist)+stroke+"LCM"
        splits = []
        with open("percentages.txt", 'r') as input:
            for line in input:
                if query in line:
                    for x in range(int(dist)//50):
                        splits.append(float(input.readline()))
                    break
        count = 1
        totaltime = 0
        for a in splits:
            totaltime = totaltime + a
            isplit = round(a*time, 2)
            if a == splits[len(splits)-1]: 
                rounderror = (1-totaltime)*time
                isplit = round(isplit+rounderror, 2)                  
            isplit = formatsplit(isplit)
            results.append(isplit)
            distdisplay.append(str(50*count) + "m")
            iterator.append(count-1)
            count = count + 1 
        count = 1
        timedisplay = timedis(m, s, ms)
    return render_template('calc-meters.html.j2', empty=False, iterator=iterator, timedisplay=timedisplay, results=results, distdisplay=distdisplay)