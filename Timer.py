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
global message

if sys.platform == "linux" or sys.platform == "posix":
    clearorcls = "clear"
else:
    clearorcls = "cls"

whattodonext = "Not done"

total_seconds = 0
MINUTE_SECONDS = 60
HOUR_SECONDS = 60*60
DAY_SECONDS = 24*60*60
message = ""

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


def convert_seconds_to_time(seconds):
    if seconds < 0:
        negative = True
        seconds = abs(seconds)
    else:
        negative = False
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, remainder = divmod(remainder, 60)
    seconds = int(remainder)
    return {
        'negative': negative,
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
    }


def get_formatted_time(seconds=0, minutes=0, hours=0, days=0, negative=False):
    def sub_string_formatter(value, name):
        return '{value} {name}{s}'.format(value=value,
                                          name=name,
                                          s='s' if value != 1 else '')

    def final_string_formatter(time_list, negative):
        text = ' '.join(time_list)
        if negative:
            return '-' + text
        else:
            return text

    days_string = sub_string_formatter(days, 'day')
    hours_string = sub_string_formatter(hours, 'hour')
    minutes_string = sub_string_formatter(minutes, 'minute')
    seconds_string = sub_string_formatter(seconds, 'second')

    if days:
        time_list = [days_string, hours_string, minutes_string, seconds_string]
    elif hours:
        time_list = [hours_string, minutes_string, seconds_string]
    elif minutes:
        time_list = [minutes_string, seconds_string]
    else:
        time_list = [seconds_string]
    final_string = final_string_formatter(time_list, negative)
    return final_string


def playsound(soundfile):  # This is how you play the music
    mixer.init()
    mixer.music.load(soundfile)
    mixer.music.play(-1)


def days():
    global total_seconds
    amountofdays = int(input("How many days? "))
    total_seconds += amountofdays * DAY_SECONDS


def hours():
    global total_seconds
    amountofhours = int(input("How many hours? "))
    total_seconds += amountofhours * HOUR_SECONDS


def minutes():
    global total_seconds
    amountofminutes = int(input("How many minutes? "))
    total_seconds += amountofminutes * MINUTE_SECONDS


def seconds():
    global total_seconds
    amountofseconds = int(input("How many seconds? "))
    total_seconds += amountofseconds


def minusdays():
    global total_seconds
    howmuchtosubtract = int(input("How much do you want to subtract? "))
    total_seconds -= howmuchtosubtract * DAY_SECONDS


def minushours():
    global total_seconds
    howmuchtosubtract = int(input("How much do you want to subtract? "))
    total_seconds -= howmuchtosubtract * HOUR_SECONDS


def minusminutes():
    global total_seconds
    howmuchtosubtract = int(input("How much do you want to subtract? "))
    total_seconds -= howmuchtosubtract * MINUTE_SECONDS


def minusseconds():
    global total_seconds
    howmuchtosubtract = int(input("How much do you want to subtract? "))
    total_seconds -= howmuchtosubtract

def messagemake():
    global message
    message = input("What would you like your custom message to say? ")
    clear_screen()
    print("Message Saved")
    input()
    clear_screen()

while whattodonext != "done":
    clear_screen()
    print("Type the unit to modify, check, write a message, or done ")
    whattodonext = input("What do you want to do? ")
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
        time_dict = convert_seconds_to_time(total_seconds)
        formatted_time = get_formatted_time(**time_dict)
        print(formatted_time)
        input("Press enter to put in a new number")
        clear_screen()
    elif whattodonext == "Message" or whattodonext == "message" or whattodonext == "Write a message" or whattodonext == "write a message" or whattodonext == "Write A Message" or whattodonext == "writeamessage":
        clear_screen()
        messagemake()
    else:
        while total_seconds > 0:
            clear_screen()
            time_dict = convert_seconds_to_time(total_seconds)
            formatted_time = get_formatted_time(**time_dict)
            print(formatted_time)
            total_seconds -= 1
            time.sleep(1)
        else:
            clear_screen()
            song = random.choice(optionalsongs)
            playsound(song)
            print("Press enter to end this song")
            if message != "":
                print("THERE IS A MESSAGE FOR YOU:")
                print(message)
            input(" ")
            message = ""
