import time
import threading
import PySimpleGUI as sg
from pynput.keyboard import Listener, KeyCode

layout = [
            [sg.Text("Please select your mod :")], [sg.Button("OK")]
         ]

# Create the window
window = sg.Window("AutoFunkin'", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()

selection =
(
'31 Minutos','A.G.O.T.I.','ABSOLUTE RAGE','ALL-OUT','Abandoned Arcade Machine',
'Abigail','Ace','Aflac','Ambion Corrupt Frenzy','Amogus','Anders','Ankha','Annie',
'Arcade Showdown - Vs. Kapi','Arch','Auditor','Auditricky','Ayana','B-Side Ron',
'B.O.L.E','BREAKOUT','Baby Blue Brother','Bad Luck QT','Baldi','Banjo & Kazooie',
'Beach Brother','Bem-te-vi','Bendy','Berzerk','Big Brother','Big Sister',
'Bikini Bottom Funkin’','Blantados','Blocky','Bloxxin’','Boy Girlfriend',
'Brick Frog','Brightside','Brostep Bugfest','Burger King Arabia','Byte Funkin’',
'CG5 Edition','Candi','Captain Viridian','Carol','Cartoon Cat','Cashier','Charlie',
'Cheeky','Cheese','Chira','Clip','Concert Conundrum','Corrupt','Crash Bandicoot',
'Crypto','Cyber Sensation','Cye','Cyrix','Dave and Bambi','Dawktrap','Deep-Sea Date',
'Demonic Discourse','Displo','Divorcin’','Doki Doki Takeover',
'Door to Door Door Salesman','Doxxie','Dr. Jack Springheel','Dr. Robotnik','eteled',
'Everywhere At The End Of Funk','FL Chan','FNF Dusttale','FNF in a Wimpy Day',
'FNF: The Origami King','Fancy Pants','Flaky','Fliqpy (J0nnytest)','Fliqpy (miguel185)',
'Friday Night Fever','Friday Night Foundation','Friday Night Funkin’ (The base)',
'Friday Night Funkin: Soft','Friday Night Funkin’ - A World of Our Own',
'Friday Night Funkin’ Pixels','Friday Night Funkin’ Unfinished Business: Vs. Adam',
'Friday Night Postin’','Friday Night Shootin’','Friday Night Trepidation',
'Friendly Night Funkin’','Fruit Medley Mayhem','Gacha Mod','Ghost Twins',
'Golf Minigame','Grunt Gaming','Hank (High Effort)','Hank (Vs. Online)','Hart',
'Hat Kid','Hecker','Henry Stickmin','Herobrine','Hex','Hololive Funkin’','Homer',
'Idiot','If Mario Was In FNF','Impostors','Isaac','Jester','Kiryu Kazuma','Kou',
'Kris','literally every fnf mod ever - VS. Bob Ron Little Man','Little Man 2',
'Logic','Lune','Maginage Matches','Mami','Matt','Matt Wiik 3','Matt Wiik 4',
'Matt Wiik 100','Melty','Mid-Fight Masses','Mokey and Grooby','Mope Mope',
'Mouse','Mr. Trololo','Napstablook','Necromancer','Nekofreak','Neon','Nick',
'Night of the Funky Bot','Nonsense','Nova','Older Bro','Omori','Peculiar Colours',
'Pinkie','Pompom','Pou','Project Enigma','Pulp','QT','Quest','Randy','Red',
'RidZak + Cybbr','Roblox Noob','Romp','Ron','Ronald McDonald','Rosie','Ross',
'Salad Fingers','Salty’s Sunday Night','Sandboxin’','Sasha',
'Saturday Stuck in Soulstrike','Sayori','Scratch Cat','Selever','Shaggy',
'Shaggy x Matt','Shard','Shinobi Scramble','Sketchy','Slaughter Me Funkin’',
'Slenderman','Slime Showdown','Smoke Em’ Out Struggle','Sonic’s Rhythm Rush',
'Sonic.exe','Stairs','Starecrown','Starlight Mayhem','Starving Artist','Static',
'Stickman','Subject 93','Suicide Mouse','Sunday','Susie','Tabi','Tails Gets Trolled',
'The Blueballs Incident','The Date Week','The Impossible Trio Chart',
'The Impostor Boyfriend Saga','The Monstrosity of Experiments','Times & Tribulations',
'Tinky Winky','Tord','Tree','Tricky','Trollface','Trollface/Trollge','Trollge',
'Viernes Noche Webiando’','Void','Weeg Mod','Weegee','Whitty','Windows XP','X-Event',
'Xe','Yukichi','Yung Lixo','Zardy'
)

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
