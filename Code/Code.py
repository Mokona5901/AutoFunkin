import time
import threading
from pynput.keyboard import Listener, KeyCode
import tkinter as tk
from tkinter import ttk
import os
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://fnfmod.online/popular-mods/"

# Fetch the page content
response = requests.get(url)
html_content = response.content

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <a> tags with the class 'personages__link' and get 'data-tippy-content'
mod_elements = soup.find_all('a', class_='personages__link')
mod_names = [element.get('data-tippy-content').strip() for element in mod_elements if element.get('data-tippy-content')]
mod_names_sorted = sorted(mod_names)

# Selection list
selection = ([f"{mod}" for mod in mod_names_sorted])

def on_select(event):
    print(f"Selected: {selected_mod.get()}")

# Create main window
root = tk.Tk()
root.title("AutoFunkin'")
icon_path = os.path.join(os.path.dirname(__file__), 'game_icon.ico')
root.iconbitmap(icon_path)
root.geometry("300x150")

# Text label
label = tk.Label(root, text="Please select your mod:")
label.pack(pady=10)

# Dropdown menu
selected_mod = tk.StringVar()
dropdown = ttk.Combobox(root, textvariable=selected_mod, values=selection, state="readonly")
dropdown.bind("<<ComboboxSelected>>", on_select)
dropdown.pack(pady=10)

# OK button to close the window
ok_button = tk.Button(root, text="OK", command=root.quit)
ok_button.pack(pady=10)

# Run the GUI
root.mainloop()
