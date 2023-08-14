import functions
from functions import *
import PySimpleGUI as sg

label = sg.Text("Enter Your Note Here")
inbox = sg.InputText(tooltip="enter note", key="note")
add_button = sg.Button("Add")
list_box = sg.Listbox(values= functions.read_mode() , key="notes" ,
                       enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")
exit_button = sg.Button("Exit")

window = sg.Window("My Ditigal notes ",
                   layout = [[label]
                       ,[inbox,add_button]
                       , [list_box,edit_button , delete_button] ,
                           [exit_button]  ] ,
                   font=('Helvetica', 10))

while True:
    event, values = window.read()
    print(event,"1")
    print(values,"2")
    print(values["notes"],"3")
    match event:
        case "Add":
            notes = functions.read_mode()
            new_notes = values["note"] + "\n"
            notes.append(new_notes)
            functions.write_mode(notes)
            window["notes"].update(values=notes)
        case "Edit":
            note_to_edit = values["notes"][0]
            new_note = values['note']

            notes = functions.read_mode()
            index = notes.index(note_to_edit)
            notes[index] = new_note
            functions.write_mode(notes)
            window["notes"].update(values=notes)
        case "Delete":
            note_to_delete = values['notes'][0]
            notes = functions.read_mode()
            notes.remove(note_to_delete)
            functions.write_mode(notes)
            window["notes"].update(values=notes)
            window["note"].update(value='')
        case "Exit":
            break

        case "notes":
            window["note"].update(value=values["notes"][0])

        case sg.WINDOW_CLOSED:
            break


window.close()