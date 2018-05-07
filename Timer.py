#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Title: My own personal timer
#Author: Riley Carpenter
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import time
from pygame import mixer
import os
import glob
import sys
import random
global totalseconds
global totaldays
global totalhours
global totalminutes
global totalcountdown
global secondspassed
global hourspassed
global minutespassed
global dayspassed
global hourspassed
if sys.platform == "linux" or sys.platform == "posix":
    clearorcls = "clear"
else:
    clearorcls = "cls"
whattodonext = "Not done"
totaldays = 0
totalhours = 0
totalminutes = 0
totalseconds = 0
totalcountdown = 0
secondspassed = 0
minutespassed = 0
hourspassed = 0
dayspassed = 0
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#THESE ARE THE PATHS TO MY MUSIC DIRECTORY CHANGE THESE TO YOUR DIRECTOR LEAVE THE /*mp3* AND /*wav* SO IT WORKS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
dir_path = os.path.dirname(os.path.realpath(__file__))
optionalsongs = (glob.glob(dir_path + "/Alarm Mark II/Songs/*.wav*"))
optionalsongs += (glob.glob(dir_path + "/Songs/*.mp3"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#THESE ARE THE PATHS TO MY MUSIC DIRECTORY CHANGE THESE TO YOUR DIRECTOR LEAVE THE /*mp3* AND /*wav* SO IT WORKS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def recalculate():
    global totalseconds
    global totaldays
    global totalhours
    global totalminutes
    global totalcountdown
    global secondspassed
    global hourspassed
    global minutespassed
    global dayspassed
    global hourspassed
    while totalseconds >= 60 or totalminutes >= 60 or totalhours >= 24:
        if totalseconds >= 60:
            totalseconds -= 60
            totalminutes += 1
        if totalminutes >= 60:
            totalminutes -= 60
            totalhours += 1
        if totalhours >= 24:
            totaldays += 1
            totalhours -= 24
def playsound(soundfile): #This is how you play the music
    mixer.init()
    mixer.music.load(soundfile)
    mixer.music.play(-1)
def days():
    global totalseconds
    global totaldays
    global totalhours
    global totalminutes
    global totalcountdown
    global secondspassed
    global hourspassed
    global minutespassed
    global dayspassed
    global hourspassed
    amountofdays = int(input("How many days? "))
    totaldays += amountofdays
    recalculate()
def hours():
    global totalseconds
    global totaldays
    global totalhours
    global totalminutes
    global totalcountdown
    global secondspassed
    global hourspassed
    global minutespassed
    global dayspassed
    global hourspassed
    amountofhours = int(input("How many hours? "))
    totalhours += amountofhours
    recalculate()
def minutes():
    global totalseconds
    global totaldays
    global totalhours
    global totalminutes
    global totalcountdown
    global secondspassed
    global hourspassed
    global minutespassed
    global dayspassed
    global hourspassed
    amountofminutes = int(input("How many minutes? "))
    totalminutes += amountofminutes
    recalculate()
def seconds():
    global totalseconds
    global totaldays
    global totalhours
    global totalminutes
    global totalcountdown
    global secondspassed
    global hourspassed
    global minutespassed
    global dayspassed
    global hourspassed
    amountofseconds = int(input("How many seconds? "))
    totalseconds += amountofseconds
    if totalseconds >= 60:
        totalseconds -= 60
        totalminutes += 1
    if totalminutes >= 60:
        totalminutes -= 60
        totalhours += 1
while whattodonext != "done":
    whattodonext = input("What unit of time do you want to count from? Type done if done ")
    if whattodonext == "days" or whattodonext == "Days":
        days()
    elif whattodonext == "hours" or whattodonext == "Hours":
        hours()
    elif whattodonext == "minutes" or whattodonext == "Minutes":
        minutes()
    elif whattodonext == "seconds" or whattodonext == "Seconds":
        seconds()
    else:
        while totaldays != 0 or totalhours != 0 or totalminutes != 0 or totalseconds != 0:
            os.system(clearorcls)
            if totalseconds == 60:
                totalminutes += 1
                totalseconds = 0
            if totalminutes == 60:
                totalhours += 1
                totalminutes = 0
            if totalhours == 24:
                totaldays += 1
                totalhours = 0
            if totaldays > 0 and totalhours < 0:
                totalhours = 23
                totaldays -= 1
            if totalhours > 0 and totalminutes < 0:
                totalminutes = 59
                totalhours -= 1
            if totalminutes > 0 and totalseconds < 0:
                totalseconds = 59
                totalminutes -= 1
            if totaldays == 1:
                day = "day"
            else:
                day = "days"
            if totalhours == 1:
                hour = "hour"
            else:
                hour = "hours"
            if totalminutes == 1:
                minute = "minute"
            else:
                minute = "minutes"
            if totalseconds == 1:
                second = "second"
            else:
                second = "seconds"
            if totaldays >= 1:
                fulltime = [totaldays,day,totalhours,hour,totalminutes,minute,totalseconds,second]
            elif totalhours >= 1:
                fulltime = [totalhours,hour,totalminutes,minute,totalseconds,second]
            elif totalminutes >= 1:
                fulltime = [totalminutes,minute,totalseconds,second]
            else:
                fulltime = [totalseconds,second]
            print(*fulltime,sep = " ")
            totalseconds -= 1
            time.sleep(1)
        else:
            song = random.choice(optionalsongs)
            playsound(song)
            input("Press enter to end this song")
