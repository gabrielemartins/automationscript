import webbrowser
import subprocess
import pyautogui
import time


def openBrowserTab(url):
    webbrowser.open(url)
    time.sleep(3)


def openProgram(program, sleepTime):
    subprocess.Popen(program)
    time.sleep(sleepTime)


def createNewDesktop():
    pyautogui.hotkey('ctrl', 'winleft', 'd')
    pyautogui.hotkey('ctrl', 'winleft', 'right')
    time.sleep(3)


sites = ['https://www.youtube.com/', 'https://www.amazon.com.br']

for site in sites:
    openBrowserTab(site)

createNewDesktop()

ide = pyautogui.prompt('vscode or vs2019?')

if (ide == 'vscode'):
    openProgram('B:\\Programs\\visualstudio\\Microsoft VS Code\\Code.exe', 5)
elif (ide == 'vs2019'):
    openProgram(
        'U:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Enterprise\\Common7\\IDE\\devenv.exe', 8)
else:
    pyautogui.write('you should open manually')
    time.sleep(2)

pyautogui.hotkey('ctrl', 'winleft', 'left')
time.sleep(2)
pyautogui.write('bye :)')
