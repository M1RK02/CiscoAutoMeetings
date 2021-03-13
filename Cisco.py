#This program needs a text file named Cisco.txt with one subject per line formatted like this "NAME CODE"
import pyautogui, os, time

def printSubjects():
    file = open('Cisco.txt')
    for i, line in enumerate(file):
        subject = line.split()
        print(f'{i+1}) {subject[0]}')

def searchCode():
    file = open('Cisco.txt')
    for i, line in enumerate(file):
        code = line.split()
        if i+1 == choice:
            return code[1]

printSubjects() #Print the list of possible subjects

choice = int(input('Select a subject: ')) #Select a subject

pyautogui.hotkey('win', 'd') #Go to desktop

time.sleep(2)

os.system(r'start "" "C:\Program Files (x86)\Webex\Webex\Applications\ptoneclk.exe"') #Open Cisco Webex

time.sleep(2)

pyautogui.press('tab', presses=5) #Go to the code box

pyautogui.typewrite(searchCode()) #Write down the code

pyautogui.press('enter', presses=2, interval=2) #Enter the class