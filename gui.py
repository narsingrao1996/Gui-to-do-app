import functions
from functions import *
import PySimpleGUI as sg

label = sg.Text("Enter Your Note Here")
inbox = sg.InputText(tooltip="enter note", key="note")
add_button = sg.Button("add")
window = sg.Window("My Ditigal notes ",
                   layout = [[label] ,[inbox,add_button]] ,
                   font=('Helvetica', 10))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "add":
            notes = functions.read_mode()
            new_notes = values["note"] + "\n"
            notes.append(new_notes)
            functions.write_mode(notes)
        case sg.WINDOW_CLOSED:
            break


window.close()