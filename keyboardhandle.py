import time
import os
offset = 0.020

#----------- PRESSES -----------#
def press_left():
    time.sleep(offset)
    os.system("xdotool key a")

def press_down():
    time.sleep(offset)
    os.system("xdotool key s")

def press_up():
    time.sleep(offset)
    os.system("xdotool key k")

def press_right():
    time.sleep(offset)
    os.system("xdotool key l")

# ----------- HOLDS -----------#
def hold_left():
    time.sleep(offset)
    os.system("xdotool keydown a")

def hold_down():
    time.sleep(offset)
    os.system("xdotool keydown s")

def hold_up():
    time.sleep(offset)
    os.system("xdotool keydown k")

def hold_right():
    time.sleep(offset)
    os.system("xdotool keydown l")

#----------- RELEASES -----------#
def release_left():
    time.sleep(offset)
    os.system("xdotool keyup a")

def release_down():
    time.sleep(offset)
    os.system("xdotool keyup s")

def release_up():
    time.sleep(offset)
    os.system("xdotool keyup k")

def release_right():
    time.sleep(offset)
    os.system("xdotool keyup l")