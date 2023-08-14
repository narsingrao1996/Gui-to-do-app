import functions
from functions import *
import time
import PySimpleGUI as sg
sg.theme("DarkAmber")
clock= sg.Text('',key="clock")
label = sg.Text("Enter Your Note Here")
inbox = sg.InputText(tooltip="enter note", key="note")
add_button = sg.Button("Add",size=10)
list_box = sg.Listbox(values= functions.read_mode() , key="notes" ,
                       enable_events=True, size=[45,10])
edit_button = sg.Button("Edit",size=10)
delete_button = sg.Button("Delete",size=10)
exit_button = sg.Button("Exit",size=10)

window = sg.Window("My Ditigal notes ",
                   layout = [ [clock]
                        ,[label]
                       ,[inbox,add_button]
                       , [list_box,edit_button , delete_button] ,
                           [exit_button]  ] ,
                   font=('Helvetica', 10))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value = time.strftime("%d-%m-%y %H:%M:%S"))

    match event:
        case "Add":
            notes = functions.read_mode()
            new_notes = values["note"] + "\n"
            notes.append(new_notes)
            functions.write_mode(notes)
            window["notes"].update(values=notes)
        case "Edit":
            try:
                note_to_edit = values["notes"][0]
                new_note = values['note']

                notes = functions.read_mode()
                index = notes.index(note_to_edit)
                notes[index] = new_note
                functions.write_mode(notes)
                window["notes"].update(values=notes)

            except IndexError:
                sg.popup("Please select the item you want to edit", font=('Helvetica', 10))

        case "Delete":
            try:
                note_to_delete = values['notes'][0]
                notes = functions.read_mode()
                notes.remove(note_to_delete)
                functions.write_mode(notes)
                window["notes"].update(values=notes)
                window["note"].update(value='')
            except IndexError:
                sg.popup("Please select the item you want to delete", font=('Helvetica', 10))

        case "Exit":
            break

        case "notes":
            window["note"].update(value=values["notes"][0])

        case sg.WINDOW_CLOSED:
            break


window.close()