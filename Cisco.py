import keyboard, time, PySimpleGUI as sg
from pywinauto import Application

def checkFile(file): #Check if the file exist
    try:
        f = open(file)
        return True
    except IOError:
        return False

def listMeetings(): #Add a button for every meeting in the file
    file = open(MeetingsFile)
    i=-1
    CheckFlag = False
    for i, line in enumerate(file):
        meeting = line.split()
        if meeting[1].isnumeric() and int(meeting[1])>99999999 and int(meeting[1])<10000000000:
            buttons.append([sg.Button(meeting[0], key=i)])
            CheckFlag = True
        else:
            buttons.append([sg.Button(f'{meeting[0]} (Code not valid)', key=-1)])
    return i, CheckFlag

def getCode(): #Return the code of the selected meetings
    file = open(MeetingsFile)
    for i, line in enumerate(file):
        code = line.split()
        if i == choice:
            return code[1]

def enterMeeting():
    keyboard.send('win+d') #Go to desktop
    time.sleep(1)
    app = Application(backend="uia").start(f'{CiscoDirectory}') #Open Cisco Webex
    app = Application(backend="uia").connect(path=f'{CiscoDirectory}')
    time.sleep(5)
    app.Pane.Edit.click_input() #Click the code box
    keyboard.send('ctrl+a')
    keyboard.write(getCode()) #Write down the code
    keyboard.send('enter')
    time.sleep(10)
    keyboard.send('enter')

CiscoDirectory = r'C:\Program Files (x86)\Webex\Webex\Applications\ptoneclk.exe'

MeetingsFile = r'Cisco.txt'

if not checkFile(CiscoDirectory):
    layout = [[sg.Text('Cisco executable not found')]]

if not checkFile(MeetingsFile):
    layout = [[sg.Text('File "Cisco.txt" not found')]]
else:
    buttons = []
    i , CheckFlag = listMeetings()
    if i == -1:
        layout = [[sg.Text('"Cisco.txt" is blank')]]
    elif not CheckFlag:
        layout = [[sg.Text('All the codes are invalid')]]
    else:
        layout = [ *buttons ]

window = sg.Window('CiscoAutoMeetings', layout, finalize=True, element_justification='Center')

window.set_min_size((300,0))
    

while True:
    event, values = window.Read()
    if event is None:
        window.Close()
        break
    elif event == -1:
        continue
    else:
        choice = event
        window.Close()
        enterMeeting()
        break