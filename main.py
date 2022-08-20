import pyautogui
import time
#Automatizar backapp dos arquivos
pyautogui.alert("O python vai controlar seu pc...")
pyautogui.PAUSE = 0.5
#abrir o google drive
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write("https://drive.google.com/drive/my-drive")
pyautogui.press('enter')
# entra na area de trabalho
pyautogui.hotkey('winleft', 'd')
pyautogui.moveTo(x=1554, y=533)

# cliquei e arrastei
pyautogui.mouseDown()
pyautogui.moveTo(x=649, y=492)
pyautogui.hotkey('alt', 'tab')
pyautogui.mouseUp()
#ntrar no google drive e soltei o arquivo
time.sleep(5)
pyautogui.alert("O codigo ja rodou")