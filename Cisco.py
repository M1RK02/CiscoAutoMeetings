#This program needs a text file named Cisco.txt with one meeting per line formatted like this "NAME CODE"
import pyautogui, os, time

def printSubjects(): #Print the list of possible meetings and return the max possible index
    file = open('Cisco.txt')
    for i, line in enumerate(file):
        subject = line.split()
        print(f'{i+1}) {subject[0]}')
    return i

def searchCode(): #Return the code of the selected meetings
    file = open('Cisco.txt')
    for i, line in enumerate(file):
        code = line.split()
        if i+1 == choice:
            return code[1]

def checkInput(user_input): #Check if the input is valid
    if not isNum(user_input): return False
    user_input = int(user_input)
    if not bounds(user_input): return False
    return True

def isNum(user_input): #Check if the input is a number
    if not user_input.isnumeric():
        print('This is not a valid number')
        return False
    else: return True

def bounds(user_input): #Check if the input is in bounds
    if user_input > max or user_input < 1:
        print('This number is out of bounds')
        return False
    else: return True

def sendMessage(message): #Auto send message in the chat
    pyautogui.press('tab', presses=2)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('f6')
    pyautogui.press('tab', presses=3)
    pyautogui.typewrite(message)
    pyautogui.press('enter')

wait = 10

max = printSubjects() + 1 #Print the list of possible meetings and save the max possible choice

while True:
    choice = input('Select a meeting: ')
    if not checkInput(choice): #Check if the input is valid
        print('Please try again')
        continue
    choice = int(choice)
    break

message = input('Insert a message to send after joining, leave blank for none: ')

pyautogui.hotkey('win', 'd') #Go to desktop

os.system(r'start "" "C:\Program Files (x86)\Webex\Webex\Applications\ptoneclk.exe"') #Open Cisco Webex

time.sleep(wait)

screen = pyautogui.size() #Get screen size

pyautogui.leftClick(screen[0]-250, 250) #Click code box

pyautogui.hotkey('ctrl', 'a')

pyautogui.typewrite(searchCode()) #Write down the code

pyautogui.press('enter', presses=2, interval=wait) #Enter the class

if message: #If message is not black send message
    sendMessage(message)