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