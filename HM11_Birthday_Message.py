# import pyautogui
# import keyboard
# import time

# # wait for the user to open a text editor
# time.sleep(5)

# # message or wishes in loop
# for i in range(1, 30):  # Change the range to ensure multiple iterations
#     if 2 / i == 0:
#         pyautogui.write(f"HAPPY BIRTHDAY MISS - MAY - GRACE {i} TIMES ")
#         keyboard.write('\U0001F642')
#         pyautogui.press('enter')
#     elif i % 3 == 0:
#         pyautogui.write(f"HAPPY BIRTHDAY CUTE - CARING - EMOTIONAL {i} TIMES ")
#         keyboard.write('\U0001F633')
#         pyautogui.press('enter')
#     elif i % 4 == 0:
#         pyautogui.write(f"HAPPY BIRTHDAY LINGXIO - SONG - WEILONG {i} TIMES ")
#         keyboard.write('\U0001F9B8')
#         pyautogui.press('enter')
#     elif i % 5 == 0:
#         pyautogui.write(f"HAPPY BIRTHDAY SMILING - ALONE - CRYING {i} TIMES ")
#         keyboard.write('\U0001F979')
#         pyautogui.press('enter')
#     elif i % 6 == 0:
#         pyautogui.write(f"HAPPY BIRTHDAY BIGLAUGH - LITTLE - GIRL {i} TIMES ")
#         keyboard.write('\U0001F62D')
#         pyautogui.press('enter')
#     elif i % 7 == 0:
#         pyautogui.write(f"HAPPY BIRTHDAY CUTIE - PIE - KID {i} TIMES ")
#         keyboard.write('\U0001F370')
#         pyautogui.press('enter')
#     elif i % 8 == 0:
#         pyautogui.write(f"HAPPY BIRTHDAY CARELESS - PRETTY - SHORT {i} TIMES ")
#         keyboard.write('🤦🏻‍♂️')
#         pyautogui.press('enter')
#     elif i % 9 == 0:
#         pyautogui.write(f"HAPPY BIRTHDAY INNOCENT - GOD'S - CHILD {i} TIMES ")
#         keyboard.write('\U0001F607')
#         pyautogui.press('enter')
#     else:
#         pyautogui.write(f"HAPPY BIRTHDAY HAVE A GOOD DAY {i} TIMES")
#         keyboard.write('\U0001F60A')
#         pyautogui.press('enter')

import pyautogui
import time
import keyboard

# Wait for the user to open a text editor
time.sleep(5)

# Dictionary to store the conditions and their corresponding messages
messages = {
    2: "HAPPY BIRTHDAY Hansil The Great {i} TIMES 😊",
    3: "HAPPY BIRTHDAY CUTE - CARING - EMOTIONAL {i} TIMES 😳",
    4: "HAPPY BIRTHDAY LINGXIO - SONG - WEILONG {i} TIMES 🦸",
    5: "HAPPY BIRTHDAY SMILING - ALONE - CRYING {i} TIMES 🙂",
    6: "HAPPY BIRTHDAY BIGLAUGH - LITTLE - GIRL {i} TIMES 😭",
    7: "HAPPY BIRTHDAY CUTIE - PIE - KID {i} TIMES 🍰",
    8: "HAPPY BIRTHDAY CARELESS - PRETTY - SHORT {i} TIMES 🤦🏻‍♂️",
    9: "HAPPY BIRTHDAY INNOCENT - GOD'S - CHILD {i} TIMES 😇"
}

emojis = {
    2: "\U0001F642",
    3: "\U0001F633",
    4: "\U0001F9B8",
    5: "\U0001F979",
    6: "\U0001F62D",
    7: "\U0001F370",
    8: "🤦🏻‍♂️",
    9: "\U0001F607"
}

# Message for default case
default_message = "HAPPY BIRTHDAY HAVE A GOOD DAY {i} TIMES 😊"

# Loop 1455 times
for i in range(140, 1445):
    message_sent = False

    for key in sorted(messages.keys()):
        if i % key == 0:
            pyautogui.write(messages[key].format(i=i))
            keyboard.write(emojis[key])
            pyautogui.press('enter')
            message_sent = True

    if not message_sent:
        pyautogui.write(default_message.format(i=i))
        keyboard.write('\U0001F60A')
        pyautogui.press('enter')

    # Small delay to prevent overwhelming the system
