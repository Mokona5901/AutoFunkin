import time
import threading
import PySimpleGUI as sg
from pynput.keyboard import Listener, KeyCode

layout = [[sg.Text("Please select your mod :")], [sg.Button("OK")]]

# Create the window
window = sg.Window("AutoFunkin'", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()

selection = (
    'Apple', 'Apricots', 'Avocado', 'Banana', 'Blackberries', 'Blackcurrant',
    'Blueberries', 'Breadfruit', 'Cantaloupe', 'Carambola', 'Cherimoya',
    'Cherries', 'Clementine', 'Coconut Meat', 'Cranberries', 'Custard-Apple',
    'Date Fruit', 'Durian', 'Elderberries', 'Feijoa', 'Figs', 'Gooseberries',
    'Grapefruit', 'Grapes', 'Guava', 'Honeydew Melon', 'Jackfruit', 'Java-Plum',
    'Jujube Fruit', 'Kiwifruit', 'Kumquat', 'Lemon', 'Longan', 'Loquat',
    'Lychee', 'Mandarin', 'Mango', 'Mangosteen', 'Mulberries', 'Nectarine',
    'Olives', 'Orange', 'Papaya', 'Passion Fruit', 'Peaches', 'Pear',
    'Persimmon', 'Pitaya', 'Pineapple', 'Pitanga', 'Plantain', 'Plums',
    'Pomegranate', 'Prickly Pear', 'Prunes', 'Pummelo', 'Quince', 'Raspberries',
    'Rhubarb', 'Rose-Apple', 'Sapodilla', 'Sapote, Mamey', 'Soursop',
    'Strawberries', 'Sugar-Apple', 'Tamarind', 'Tangerine', 'Watermelon')

width = max(map(len, selection))+1

layout = [
    [sg.Combo(selection, size=(width, 5), enable_events=True, key='-COMBO-')]
]

window = sg.Window("Title", layout, finalize=True)
combo = window['-COMBO-']
combo.bind("<Enter>", "ENTER-")

while True:

    event, values = window.read()
    print(event, values)

    if event == sg.WINDOW_CLOSED:
        break
    elif event == "-COMBO-ENTER-":
        combo.Widget.event_generate('<Button-1>')

window.close()
