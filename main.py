import pyautogui
import keyboardhandle as kbh
import threading
import mss
import numpy as np

def scan_left_lane():
    while True:
        scanned_pixel = screenshot[1000, 550, :3]
        if tuple(scanned_pixel) == (0, 0, 253):
            kbh.hold_left()
        else:
            kbh.release_left()

def scan_down_lane():
    while True:
        scanned_pixel = screenshot[1000, 760, :3]
        if tuple(scanned_pixel) == (252, 42, 12):
            kbh.hold_down()
        else:
            kbh.release_down()

def scan_up_lane():
    while True:
        scanned_pixel = screenshot[1000, 970, :3]
        if tuple(scanned_pixel) == (0, 140, 0):
            kbh.hold_up()
        else:
            kbh.release_up()

def scan_right_lane():
    while True:
        scanned_pixel = screenshot[1000, 1180, :3]
        if tuple(scanned_pixel) == (0, 222, 231):
            kbh.hold_right()
        else:
            kbh.release_right()

with mss.mss() as sct:
    monitor = sct.monitors[0]
    screenshot = np.array(sct.grab(monitor))

lthread = threading.Thread(target=scan_left_lane, daemon=True).start()
dthread = threading.Thread(target=scan_down_lane, daemon=True).start()
uthread = threading.Thread(target=scan_up_lane, daemon=True).start()
rthread = threading.Thread(target=scan_right_lane, daemon=True).start()
            
while True:
    with mss.mss() as sct:
        screenshot = np.array(sct.grab(monitor))