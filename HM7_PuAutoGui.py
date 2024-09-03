# import turtle
# turtle.speed (3)
# turtle.bgcolor('black')
# turtle.pensize(3)
# def func():
#     for i in range(200):
#         turtle.right (1)
#         turtle.forward(1)
#         turtle.color('red', 'pink')
#         turtle.begin_fill()
#         turtle.left(140)
#         turtle.forward(111.65)
# func()
# turtle.left(120)
# func()
# turtle.forward(111.65)
# turtle.end_fill()
# turtle.hideturtle()
# turtle.done()

# import pyautogui as pa
# import time
# time.sleep(3)
# for i in range(100):
#     pa.write("Poo")
#     pa.press('enter')

import pyautogui
import time

# Wait for the user to open a text editor
time.sleep(5)

# # Press the Windows key to open the Start menu
# pyautogui.press('win')

# # Type "emoji" to search for the emoji picker
# pyautogui.write('emoji')

# # Wait for the emoji picker to appear
# time.sleep(1)

# # Press the Enter key to open the emoji picker
# pyautogui.press('enter')

# # Wait for the emoji picker to fully load
# time.sleep(1)

# # Type "heart eyes" to search for the heart eyes emoji
# pyautogui.write('heart eyes')

# # Press the Enter key to select the heart eyes emoji
# pyautogui.press('enter')

# # Wait for the emoji to be inserted
# time.sleep(1)

# # Press the Enter key to add a new line
# pyautogui.press('enter')
for i in range(1,500):
# Type a message to go with the emoji
    pyautogui.write('picked up call')
    # pyautogui.hotkey('tab')
    # Press the Enter key to submit the message
    pyautogui.press('enter')