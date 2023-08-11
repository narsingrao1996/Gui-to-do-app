import PySimpleGUI as sg
from functions import *

label = sg.Text("Enter Your Note Here")
inbox = sg.InputText(tooltip="enter note")
add_button = sg.Button("add")
window = sg.Window("My Ditigal notes ", layout = [[label] ,[inbox,add_button]])
window.read()
window.close()