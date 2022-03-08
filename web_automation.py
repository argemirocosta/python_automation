import pyautogui
import pyperclip
import time
import os

#pausa entre cada comando
pyautogui.PAUSE = 1

os.system("open https://google.com")
pyautogui.hotkey("command", "t")
pyperclip.copy("https://www.bing.com/?cc=br")
pyautogui.click(x=540, y=80)
pyautogui.hotkey("command", "v")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=534, y=297)
pyautogui.write("Clube de Regatas Vasco da Gama")
pyautogui.press("enter")
pyautogui.click(x=727, y=573)
pyautogui.click(x=934, y=603)
time.sleep(5)

# Para descobrir a posição x e y, dá um tempo, pego a posição e depois preenche no click
#time.sleep(10)
#print(pyautogui.position())
