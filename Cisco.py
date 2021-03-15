#This program needs a text file named Cisco.txt with one meeting per line formatted like this "NAME CODE"
import pyautogui, os, time, PySimpleGUI as sg

def checkFile(): #Check if the file exist
    try:
        f = open('Cisco.txt')
        return True
    except IOError:
        return False

def listMeetings(): #Add a button for every meeting in the file
    file = open('Cisco.txt')
    i=-1
    for i, line in enumerate(file):
        meeting = line.split()
        buttons.append([sg.Button(meeting[0], key=i)])
    return i

def getCode(): #Return the code of the selected meetings
    file = open('Cisco.txt')
    for i, line in enumerate(file):
        code = line.split()
        if i == choice:
            return code[1]

def enterMeeting():
    pyautogui.hotkey('win', 'd') #Go to desktop
    os.system(r'start "" "C:\Program Files (x86)\Webex\Webex\Applications\ptoneclk.exe"') #Open Cisco Webex
    time.sleep(wait)
    screen = pyautogui.size() #Get screen size
    pyautogui.leftClick(screen[0]-250, 250) #Click code box
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(getCode()) #Write down the code
    pyautogui.press('enter', presses=2, interval=wait) #Enter the meeting

wait = 10

buttons = []

if not checkFile():
    layout = [[sg.Text('The file "Cisco.txt" does not exist')]]
else:
    i = listMeetings()
    if i == -1:
        layout = [[sg.Text('There are no meetings in the "Cisco.txt" file')]]
    else:
        layout = [ *buttons ] 


window = sg.Window('CiscoAutoMeetings', layout, finalize=True, element_justification='Center')

window.set_min_size((300,0))
    

while True:
    event, values = window.Read()
    if event is None:
        break
    else:
        choice = event
        enterMeeting()
        break
    
window.Close()