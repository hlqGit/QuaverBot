import cv2
import numpy as np
import pyautogui
pyautogui.FAILSAFE = False
import time
import PIL as pil
import threading
import Xlib.threaded
import keyboardhandle as kbh

arrow_l = cv2.imread("assets/arrow_left.png")
arrow_r= cv2.imread("assets/arrow_right.png")
arrow_u = cv2.imread("assets/arrow_up.png")
arrow_d = cv2.imread("assets/arrow_down.png")

arrow_lsh = cv2.imread("assets/holdstart_left.png")
arrow_rsh= cv2.imread("assets/holdstart_right.png")
arrow_ush = cv2.imread("assets/holdstart_up.png")
arrow_dsh = cv2.imread("assets/holdstart_down.png")

arrow_leh = cv2.imread("assets/holdend_left.png")
arrow_reh= cv2.imread("assets/holdend_right.png")
arrow_ueh = cv2.imread("assets/holdend_up.png")
arrow_deh = cv2.imread("assets/holdend_down.png")

region = (435, 800, 850, 300) # left, top, width, height
method = cv2.TM_SQDIFF_NORMED
threshold = 0.25

# rect_info = []

#----------------------------------#
#                                  #
#      scroll speed 31.7 pls       #
#                                  #
#----------------------------------#

def npscreenshot() -> np.array:
    image = np.array(pyautogui.screenshot(region=region))
    return image[:, :, ::-1].copy()

screen_capture = npscreenshot()

def detect_left():
    while True:
        results = {
            'left': cv2.matchTemplate(screen_capture, arrow_l, method),
            'holdstart_left': cv2.matchTemplate(screen_capture, arrow_lsh, method),
            'holdend_left': cv2.matchTemplate(screen_capture, arrow_leh, method)
        }
        best_match = None
        best_score = float('inf')
        best_variant = None
        for variant, result in results.items():
            mn, _, mnLoc, _ = cv2.minMaxLoc(result)
            if mn < best_score:
                best_score = mn
                best_match = mnLoc
                best_variant = variant

        if best_match and best_score < threshold:
            MPx, MPy = best_match
            trows, tcols = arrow_l.shape[:2]
            # cv2.rectangle(screen_capture, (MPx, MPy), (MPx + tcols, MPy + trows), (0, 0, 255), 2)
            # cv2.putText(screen_capture, best_variant, (MPx, MPy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            # rect_info.append((MPx, MPy, tcols, trows, best_variant))
            kbh.press_left()
            print("pressing left")
            # match best_variant:
            #     case 'left':
            #         kbh.press_left()
            #     case 'holdstart_left':
            #         kbh.hold_left()
            #     case 'holdend_left':
            #         kbh.release_left()
            
            
def detect_down():
    while True:
        results = {
            'down': cv2.matchTemplate(screen_capture, arrow_d, method),
            'holdstart_down': cv2.matchTemplate(screen_capture, arrow_dsh, method),
            'holdend_down': cv2.matchTemplate(screen_capture, arrow_deh, method)
        }
        best_match = None
        best_score = float('inf')
        best_variant = None
        for variant, result in results.items():
            mn, _, mnLoc, _ = cv2.minMaxLoc(result)
            if mn < best_score:
                best_score = mn
                best_match = mnLoc
                best_variant = variant

        if best_match and best_score < threshold:
            MPx, MPy = best_match
            trows, tcols = arrow_l.shape[:2]
            # cv2.rectangle(screen_capture, (MPx, MPy), (MPx + tcols, MPy + trows), (0, 0, 255), 2)
            # cv2.putText(screen_capture, best_variant, (MPx, MPy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            # rect_info.append((MPx, MPy, tcols, trows, best_variant))
            kbh.press_down()
            print("pressing down")
            # match best_variant:
            #     case 'down':
            #         kbh.press_down()
            #     case 'holdstart_down':
            #         kbh.hold_down()
            #     case 'holdend_down':
            #         kbh.release_down()
            
            
def detect_up():
    while True:
        results = {
            'up': cv2.matchTemplate(screen_capture, arrow_u, method),
            'holdstart_up': cv2.matchTemplate(screen_capture, arrow_ush, method),
            'holdend_up': cv2.matchTemplate(screen_capture, arrow_ueh, method)
        }
        best_match = None
        best_score = float('inf')
        best_variant = None
        for variant, result in results.items():
            mn, _, mnLoc, _ = cv2.minMaxLoc(result)
            if mn < best_score:
                best_score = mn
                best_match = mnLoc
                best_variant = variant

        if best_match and best_score < threshold:
            MPx, MPy = best_match
            trows, tcols = arrow_l.shape[:2]
            # cv2.rectangle(screen_capture, (MPx, MPy), (MPx + tcols, MPy + trows), (0, 0, 255), 2)
            # cv2.putText(screen_capture, best_variant, (MPx, MPy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            # rect_info.append((MPx, MPy, tcols, trows, best_variant))
            kbh.press_up()
            print("pressing up")
            # match best_variant:
            #     case 'up':
            #         kbh.press_up()
            #     case 'holdstart_up':
            #         kbh.hold_up()
            #     case 'holdend_up':
            #         kbh.release_up()
            
            
def detect_right():
    while True:
        results = {
            'right': cv2.matchTemplate(screen_capture, arrow_r, method),
            'holdstart_right': cv2.matchTemplate(screen_capture, arrow_rsh, method),
            'holdend_right': cv2.matchTemplate(screen_capture, arrow_reh, method)
        }
        best_match = None
        best_score = float('inf')
        best_variant = None
        for variant, result in results.items():
            mn, _, mnLoc, _ = cv2.minMaxLoc(result)
            if mn < best_score:
                best_score = mn
                best_match = mnLoc
                best_variant = variant

        if best_match and best_score < threshold:
            MPx, MPy = best_match
            trows, tcols = arrow_l.shape[:2]
            # cv2.rectangle(screen_capture, (MPx, MPy), (MPx + tcols, MPy + trows), (0, 0, 255), 2)
            # cv2.putText(screen_capture, best_variant, (MPx, MPy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            # rect_info.append((MPx, MPy, tcols, trows, best_variant))
            kbh.press_right()
            print("pressing right")
            # match best_variant:
            #     case 'right':
            #         kbh.press_right()
            #     case 'holdstart_right':
            #         kbh.hold_right()
            #     case 'holdend_right':
            #         kbh.release_right()
            
            
# def renderer():
#     while True:
#         for elem in rect_info:
#             MPx, MPy, tcols, trows, best_variant = elem
#             cv2.rectangle(screen_capture, (MPx, MPy), (MPx + tcols, MPy + trows), (0, 0, 255), 2)
#             cv2.putText(screen_capture, best_variant, (MPx, MPy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
#             cv2.imshow('game capture', screen_capture)
#         rect_info.clear()

left_thread = threading.Thread(target=detect_left)
down_thread = threading.Thread(target=detect_down)
up_thread = threading.Thread(target=detect_up)
right_thread = threading.Thread(target=detect_right)
# render_thread = threading.Thread(target=renderer)

left_thread.daemon = True
down_thread.daemon = True
up_thread.daemon = True
right_thread.daemon = True
# render_thread.daemon = True


left_thread.start()
down_thread.start()
up_thread.start()
right_thread.start()
# render_thread.start()

# cv2.imshow('game capture', screen_capture)

while True:
    screen_capture = npscreenshot()
    cv2.imshow('capture', screen_capture)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        stop = True
        break

cv2.destroyAllWindows()