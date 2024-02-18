# MACROPAD Hotkeys: Altium Alignment commands for Windows
# BRECHTVE 14/07/2023

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Altium Alignment 2/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x002000, 'V cent',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'e', 0.05, 'g', 0.05, 'v']), # Vertical Centers
        (0x200000, 'TOP',      [Kc.CONTROL, 'T']), # Align Top
        (0x000020, 'Dist V',   [Kc.CONTROL, 'V']), # Distribute Vertically
        # 2nd row ----------
        (0x200000, '    LEFT', [Kc.CONTROL, 'L']), # Align Left
        (0x200000, 'GRD',      [Kc.CONTROL, 'D']), # Align to Grid
        (0x200000, 'RIGHT   ', [Kc.CONTROL, 'R']), # Align Right
        # 3rd row ----------
        (0x002000, 'H cent',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'e', 0.05, 'g', 0.05, 'c']), # Edit > Align > Horizontal Centers
        (0x200000, 'BTM',      [Kc.CONTROL, 'B']), # Align Bottom
        (0x000020, 'Dist H',   [Kc.CONTROL, 'H']), # Distribute Horizontally
        # 4th row ----------
        (0x202000, 'Move',     [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'e', 0.05, 'm', 0.05, 'm']), # Edit > Move > Move
        (0x202000, 'MvSel',    [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'e', 0.05, 'm', 0.05, 's']), # Edit > Move > Move Selection
        (0x202000, 'MvSelXY',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'e', 0.05, 'm', 0.05, 'x']), # Edit > Move > Move Selection by X,Y
        # Encoder button ---
        (0x000000, '',         [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'c']) # Tools > Cross Probe
    ]
}
