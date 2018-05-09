# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Title: My own personal timer
# Author: Riley Carpenter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import time
from pygame import mixer
import os
import glob
import sys
import random

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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# THESE ARE THE PATHS TO MY MUSIC DIRECTORY CHANGE THESE TO YOUR DIRECTOR LEAVE THE /*mp3* AND /*wav* SO IT WORKS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
dir_path = os.path.dirname(os.path.realpath(__file__))
optionalsongs = (glob.glob(dir_path + "/Alarm Mark II/Songs/*.wav*"))
optionalsongs += (glob.glob(dir_path + "/Songs/*.mp3"))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# THESE ARE THE PATHS TO MY MUSIC DIRECTORY CHANGE THESE TO YOUR DIRECTOR LEAVE THE /*mp3* AND /*wav* SO IT WORKS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def clear_screen():
    os.system(clearorcls)


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


def playsound(soundfile):  # This is how you play the music
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
    recalculate()


def minusdays():
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
    print(totaldays, day, "is the amount how much do you want to subtract")
    howmuchtosubtract = int(input("How much do you want to subtract? "))
    totaldays -= howmuchtosubtract
    if totaldays < 0:
        totaldays = 0
    recalculate()


def minushours():
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
    print(totalhours, hour, "is the amount how much do you want to subtract")
    howmuchtosubtract = int(input("How much do you want to subtract? "))
    totalhours -= howmuchtosubtract
    if totalhours < 0:
        totalminutes = 0
    recalculate()


def minusminutes():
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
    print(totalminutes, minute, "is the amount how much do you want to subtract")
    howmuchtosubtract = int(input("How much do you want to subtract? "))
    totalminutes -= howmuchtosubtract
    if totalminutes < 0:
        totalminutes = 0
    recalculate()


def minusseconds():
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
    print(totalseconds, second, "is the amount how much do you want to subtract")
    howmuchtosubtract = int(input("How much do you want to subtract? "))
    totalseconds -= howmuchtosubtract
    if totalseconds < 0:
        totalseconds = 0
    recalculate()


while whattodonext != "done":
    print("Type the unit to modify, check, or done ")
    whattodonext = input("What do you want to do? ")
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
        fulltime = [totaldays, day, totalhours, hour, totalminutes, minute, totalseconds, second]
    elif totalhours >= 1:
        fulltime = [totalhours, hour, totalminutes, minute, totalseconds, second]
    elif totalminutes >= 1:
        fulltime = [totalminutes, minute, totalseconds, second]
    else:
        fulltime = [totalseconds, second]
    if whattodonext == "days" or whattodonext == "Days" or whattodonext == "day" or whattodonext == "Day":
        clear_screen()
        addorminus = input("Do you want to add or subtract days ")
        if addorminus == "add" or addorminus == "Add":
            days()
        else:
            minusdays()
        clear_screen()
    elif whattodonext == "hours" or whattodonext == "Hours" or whattodonext == "hour" or whattodonext == "Hour":
        clear_screen()
        addorminus = input("Do you want to add or subtract hours ")
        if addorminus == "add" or addorminus == "Add":
            hours()
        else:
            minushours()
        clear_screen()
    elif whattodonext == "minutes" or whattodonext == "Minutes" or whattodonext == "minute" or whattodonext == "Minute":
        clear_screen()
        addorminus = input("Do you want to add or subtract minutes ")
        if addorminus == "add" or addorminus == "Add":
            minutes()
        else:
            minusminutes()
        clear_screen()
    elif whattodonext == "seconds" or whattodonext == "Seconds" or whattodonext == "second" or whattodonext == "Second":
        clear_screen()
        addorminus = input("Do you want to add or subtract seconds? ")
        if addorminus == "add" or addorminus == "Add":
            seconds()
        else:
            minusseconds()
        clear_screen()
    elif whattodonext == "Check" or whattodonext == "check":
        clear_screen()
        print(*fulltime, sep=" ")
        input("Press enter to put in a new number")
        clear_screen()
    else:
        while totaldays != 0 or totalhours != 0 or totalminutes != 0 or totalseconds != 0:
            clear_screen()
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
                fulltime = [totaldays, day, totalhours, hour, totalminutes, minute, totalseconds, second]
            elif totalhours >= 1:
                fulltime = [totalhours, hour, totalminutes, minute, totalseconds, second]
            elif totalminutes >= 1:
                fulltime = [totalminutes, minute, totalseconds, second]
            else:
                fulltime = [totalseconds, second]
            print(*fulltime, sep=" ")
            totalseconds -= 1
            if totaldays > 0 and totalhours == 0 and totalminutes == 0 and totalseconds < 0:
                totaldays -= 1
                totalhours = 23
                totalminutes = 59
                totalseconds = 59
            if totalhours > 0 and totalminutes == 0 and totalseconds < 0:
                totalhours -= 1
                totalminutes = 59
                totalseconds = 59
            if totalminutes > 0 and totalseconds == -1:
                totalminutes -= 1
                totalseconds = 59
            time.sleep(1)
        else:
            song = random.choice(optionalsongs)
            playsound(song)
            input("Press enter to end this song")
