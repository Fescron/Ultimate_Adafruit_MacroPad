# MACROPAD Hotkeys: Windows Microsoft Office (Excel) (Dutch)
# BRECHTVE 14/02/2024

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values
# from adafruit_hid.mouse import Mouse # REQUIRED if using Mouse.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Excel            2/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x202020, '*tBlk',   [Kc.ALT, 'r', 'ke', Kc.ENTER]),      # Start > Tekstkleur > (Select Automatic) > (ENTER)
        (0x200000, '-Note',   [Kc.ALT, 'c', '4']),                 # Controleren > Verwijderen
        (0x202000, '+Highl',  [Kc.ALT, 'r', 'h1', Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, 
                               Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW,
                               Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.ENTER]), # Start > Opvulkleur > (Select Yellow) > (ENTER)
        # 2nd row ----------
        (0x200000, '*tRed',   [Kc.ALT, 'r', 'ke', Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, 
                               Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW,
                               Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.ENTER]), # Start > Tekstkleur > (Select Red) > (ENTER)
        (0x002000, '*Note',   [Kc.SHIFT, Kc.F2]),                  # Opmerking toevoegen/bewerken
        (0x401000, '+Highl',  [Kc.ALT, 'r', 'h1', Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, 
                               Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW,
                               Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.ENTER]), # Start > Opvulkleur > (Select Orange) > (ENTER)
        # 3rd row ----------
        (0x200000, '-Row  ',  [Kc.ALT, 'r', 'w', 'i']),            # Start > Verwijderen > Bladrijen verwijderen
        (0x200000, '-Col  ',  [Kc.ALT, 'r', 'w', 'd']),            # Start > Verwijderen > Bladkolommen verwijderen
        (0x002000, '+Highl',  [Kc.ALT, 'r', 'h1', Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, 
                               Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW,
                               Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.ENTER]), # Start > Opvulkleur > (Select Green) > (ENTER)
        # 4th row ----------
        (0x002000, '+Row_^',  [Kc.ALT, 'r', 'nn', 'e', Kc.ENTER]), # Start > Invoegen > Bladrijen invoegen
        (0x002000, '+Col_<',  [Kc.ALT, 'r', 'nn', 'a']),           # Start > Invoegen > Bladkolommen invoegen
        (0x202020, '-Highl',  [Kc.ALT, 'r', 'h1', 'g']),           # Start > Opvulkleur > Geen opvulling
        # Encoder button ---
        (0x000000, '',        [])
    ]
}
