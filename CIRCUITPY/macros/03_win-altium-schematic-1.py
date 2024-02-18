# MACROPAD Hotkeys: Altium (simple) Schematic commands for Windows
# BRECHTVE 28/06/2023

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Altium Schematic 1/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x202000, 'Text',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 't']), # Place > Text
        # (0x202000, 'Note`',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, Kc.ALT, 'n']),               # Place > Note (custom command)
        (0x202000, 'Note',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'd', 0.05, Kc.LEFT_ARROW, 0.05, -Kc.LEFT_ARROW, Kc.UP_ARROW, 0.05, -Kc.UP_ARROW, Kc.ENTER]), # Place > (select "Note")
        (0x200020, 'BrkWir', [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'e', 0.05, 'w']), # Edit > Wire (break wire)
        # 2nd row ----------
        (0x202000, 'tBox',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'f']),            # Place > Text Frame
        (0x202000, 'Rect',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'd', 0.05, 'r']), # Place > Drawing Tools > Rectangle
        (0x202000, 'Line',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'd', 0.05, 'l']), # Place > Drawing Tools > Line
        # 3rd row ----------
        (0x200000, 'NoERC',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'v', 0.05, 'n']), # Place > Directives > Generic No ERC
        (0x200000, 'Diff',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'v', 0.05, 'f']), # Place > Directives > Differential Pair
        (0x200000, 'Param',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'v', 0.05, 'm']), # Place > Directives > Parameter Set
        # 4th row ----------
        (0x200000, 'Net',    [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'n']), # Place > Net Label
        (0x200000, 'Power',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'o']), # Place > Power Port
        (0x200000, 'Blankt', [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'v', 0.05, 'l']), # Place > Directives > Blanket
        # Encoder button ---
        (0x000000, '',       [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'c'])  # Tools > Cross Probe
    ]
}
