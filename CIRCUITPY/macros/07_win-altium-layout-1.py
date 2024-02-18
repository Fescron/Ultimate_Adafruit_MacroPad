# MACROPAD Hotkeys: Altium PCB-Layout commands for Windows
# BRECHTVE 28/06/2023

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values
from adafruit_hid.mouse import Mouse # REQUIRED if using Mouse.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Altium Layout    1/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x202000, 'Text',    [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 's']), # Place > String
        (0x202000, 'Line',    [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'l']), # Place > Line
        (0x200020, 'Gloss',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, Kc.ALT, 'g']),               # Gloss (~simplify tracks)
        # 2nd row ----------
        (0x200000, '-Conn',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'u', 0.05, 'u', 0.05, 'c']), # Route > Unroute > Connection
        (0x200000, '-Comp',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'u', 0.05, 'u', 0.05, 'o']), # Route > Unroute > Component
        (0x200000, '-Net',    [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'u', 0.05, 'u', 0.05, 'n']), # Route > Unroute > Net
        # 3rd row ----------
        (0x002000, 'Resto',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'g', 0.05, 'e']), # Tools > Polygon Pours > Restore xx Shelved Polygon(s)
        (0x200000, '`Shelv',  [{'buttons':Mouse.RIGHT_BUTTON}, 0.05, {'buttons':-Mouse.RIGHT_BUTTON}, 0.05, 'y', 0.05, 's']),                            # Rightclick > Polygon Actions > Shelve Selected
        (0x000020, 'PolyMn',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'g', 0.05, 'm']), # Tools > Polygon Pours > Polygon Manager
        # 4th row ----------
        (0x000020, 'Via',     [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'v']), # Place > Via
        (0x000020, 'Poly',    [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'g']), # Place > Polygon Pour
        # (0x000020, 'Cutout`', [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, Kc.ALT, Kc.SHIFT, 'p']),     # Place > Polygon Pour Cutout (custom command)
        (0x000020, 'Cutout',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'k', Kc.LEFT_ARROW, -Kc.LEFT_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.ENTER]), # Place > (select "Polygon Pour Cutout")
        # Encoder button ---
        (0x000000, '',        [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'c'])  # Tools > Cross Probe
    ]
}
