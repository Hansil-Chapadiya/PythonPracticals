import pyautogui
import time

# Wait for WhatsApp to open and select the chat window where you want to send the emoji
time.sleep(5)

# Type the skull emoji using the keyboard shortcut
pyautogui.hotkey('win', '.')
pyautogui.typewrite('Skull')
pyautogui.press('enter')

# Send the message
pyautogui.press('enter')