#This program needs a text file named Cisco.txt with one meeting per line formatted like this "NAME CODE"
import pyautogui, os, time, PySimpleGUI as sg

def checkFile(): #Check if the file exist
    try:
        f = open(MeetingsFile)
        return True
    except IOError:
        return False

def listMeetings(): #Add a button for every meeting in the file
    file = open(MeetingsFile)
    i=-1
    for i, line in enumerate(file):
        meeting = line.split()
        buttons.append([sg.Button(meeting[0], key=i)])
    return i

def getCode(): #Return the code of the selected meetings
    file = open(MeetingsFile)
    for i, line in enumerate(file):
        code = line.split()
        if i == choice:
            return code[1]

def enterMeeting():
    pyautogui.hotkey('win', 'd') #Go to desktop
    time.sleep(1)
    os.system(f'start /max "" "{CiscoDirectory}"') #Open Cisco Webex
    time.sleep(wait)
    screen = pyautogui.size() #Get screen size
    pyautogui.leftClick(screen[0]-250, 250) #Click code box
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(getCode()) #Write down the code
    pyautogui.press('enter')
    time.sleep(wait)
    pyautogui.press('enter')

CiscoDirectory = r'Cisco Webex Meetings.lnk'

MeetingsFile = r'Cisco.txt'

wait = 10

buttons = []

if not checkFile():
    layout = [[sg.Text('File "Cisco.txt" not found')]]
else:
    i = listMeetings()
    if i == -1:
        layout = [[sg.Text('"Cisco.txt" is blank')]]
    else:
        layout = [ *buttons ] 


window = sg.Window('CiscoAutoMeetings', layout, finalize=True, element_justification='Center')

window.set_min_size((300,0))
    

while True:
    event, values = window.Read()
    if event is None:
        window.Close()
        break
    else:
        choice = event
        window.Close()
        enterMeeting()
        break