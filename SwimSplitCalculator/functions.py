import math as m
import os 
from datetime import *
from flask import Flask, render_template, request
from datetime import datetime, timedelta

def iterativeround(time) -> float:
  time = float(time)
  ph = str(time)
  index = ph.find(".")
  iterate = len(str(ph[index+1:len(ph)]))
  for i in range(iterate-1): 
    time = round(time, iterate-i)
  return time

def every_nth(items, n, offset) -> int:
  total = 0
  for i, value in enumerate(items, n-offset):
    if i % n == 0:
      total += value
  return total

def timedis(m, s, ms) -> str: 
  timedisplay = ""
  m = int(m)
  s = int(s)
  ms = int(ms)
  if m == 0: 
    if s == 0: 
        s = "00"
    elif s < 10:
        s = "0"+str(s)
    if ms == 0: 
        ms = "00"
    elif ms < 10:
        ms = "0"+str(ms)
    timedisplay = str(s)+"."+str(ms)
  else:
    if s == 0: 
        s = "00"
    elif s < 10:
        s = "0"+str(s)
    if ms == 0: 
        ms = "00"
    elif ms < 10:
        ms = "0"+str(ms)
    timedisplay = str(m)+":"+str(s)+"."+str(ms)
  return timedisplay

def formatsplit(isplit): 
  if isplit >= 60:
    isplit = str(datetime.timedelta(seconds=isplit))
    isplit = isplit[2:10]
    if isplit[0] == "0": 
        isplit = isplit[1:]
  return isplit

def requestval():
  m = request.values.get("mm")
  s = request.values.get("ss")
  ms = request.values.get("ms")
  stroke = request.values.get("stroke")
  dist = request.values.get("distance")
  g = request.values.get("gender")
  if stroke == None or dist == None or g == None:
     return False
  else: 
     return True, m, s, ms, stroke, dist, g
  

def convert_to_timedelta(time_string):
  value = []
  accum = 0
  dot = False
  for c in time_string:
      if c.isdigit():
          accum = accum * 10 + int(c)
      else:
          value.append(accum)
          dot = c == '.'
          accum = 0
  value.append(accum)
  ms = 0 if not dot else value.pop()
  accum = 0
  for v in value:
      accum = accum * 60 + v
  return timedelta(seconds=accum + ms/1000)

def calculate_remaining_time(total_time, sub_times):
  total_time = convert_to_timedelta(total_time)

  for sub_time in sub_times:
      total_time -= convert_to_timedelta(sub_time)

  return total_time
