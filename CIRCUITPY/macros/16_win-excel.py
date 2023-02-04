# MACROPAD Hotkeys: Windows Microsoft Office (Excel) (Dutch)
# BRECHTVE 16/01/2023

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values
# from adafruit_hid.mouse import Mouse # REQUIRED if using Mouse.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Excel            2/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '',        []),
		(0x202000, '*Note',   [Kc.ALT, 'c', Kc.ALT, 'o', Kc.ALT, '1']), # Controleren > Opmerking bewerken
        (0x202000, '+Note',   [Kc.ALT, 'c', Kc.ALT, 'n']),              # Controleren > Opmerking toevoegen
        # 2nd row ----------
        (0x000000, '',        []),
        (0x000000, '',        []),
        (0x000000, '',        []),
        # 3rd row ----------
        (0x200000, '-Highl',  [Kc.ALT, 'r', Kc.ALT, 'h1', Kc.ALT, 'g']), # Start > Opvulkleur > Geen opvulling
        (0x200000, '-Row',    [Kc.ALT, 'r', Kc.ALT, 'w', Kc.ALT, 'i']),  # Start > Verwijderen > Bladrijen verwijderen
		(0x200000, '-Col',    [Kc.ALT, 'r', Kc.ALT, 'w', Kc.ALT, 'd']),  # Start > Verwijderen > Bladkolommen verwijderen
        # 4th row ----------
        (0x002000, '+Highl',  [Kc.ALT, 'r', Kc.ALT, 'h1', Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, 
                               Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW,
                               Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.ENTER]), # Start > Opvulkleur > (Select Yellow) > (ENTER)
        (0x002000, '+Row',    [Kc.ALT, 'r', Kc.ALT, 'nn', Kc.ALT, 'e']), # Start > Invoegen > Bladrijen invoegen
        (0x002000, '+Col',    [Kc.ALT, 'r', Kc.ALT, 'nn', Kc.ALT, 'a']), # Start > Invoegen > Bladkolommen invoegen
        # Encoder button ---
        (0x000000, '',        [])
    ]
}
