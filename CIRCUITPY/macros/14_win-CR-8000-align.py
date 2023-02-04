# MACROPAD Hotkeys: Windows shortcuts for Zuken - CR-8000
# BRECHTVE 16/01/2023

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'CR-8000 Alig/Sel 1/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
		# (0x202000, 'hJstGp',  [Kc.ALT, 'r', 'n', 'o']),    # Draw > Align Object > Justify Objects Horizontally at the Specified Gap
        (0x202000, 'Rotate',  [Kc.ALT, 'r', 'o', 'r']),    # Draw > Rotate > Rotate 90 Deg (Clockwise)
        (0x200000, 'TOP',     [Kc.ALT, 'r', 'n', 't']),    # Draw > Align Object > Justify to Top
        (0x202000, 'vJstGp',  [Kc.ALT, 'r', 'n', 'e']),    # Draw > Align Object > Justify Objects Vertically at the Specified Gap
        # 2nd row ----------
        (0x200000, '   LEFT', [Kc.ALT, Kc.R, Kc.N, Kc.L]), # Draw > Align Object > Justify to Left (keep holding down the buttons otherwise the program things you press "l" without being in the alt-menu's)
        (0x200000, 'GRD',     [Kc.ALT, 'r', 'n', 'g']),    # Draw > Align Object > Align to Grid
        (0x200000, 'RIGHT   ',[Kc.ALT, 'r', 'n', 'r']),    # Draw > Align Object > Justify to Right
        # 3rd row ----------
        (0x002020, '[net]',   [Kc.ALT, 'e', 's', 'n']),    # Edit > Set Default Focus > Net Object
        (0x200000, 'BOT',     [Kc.ALT, 'r', 'n', 'b']),    # Draw > Align Object > Justify to Bottom
        (0x002020, '[>net]',  [Kc.ALT, 'e', 's', 'e']),    # Edit > Set Default Focus > Net with Equal Potential
        # 4th row ----------
        (0x200020, '[main]',  [Kc.ALT, 'e', 's', 'm']),    # Edit > Set Default Focus > Main Object
        (0x200020, '[prop]',  [Kc.ALT, 'e', 's', 'v']),    # Edit > Set Default Focus > Property Viewer
        (0x002020, '[bus]',   [Kc.ALT, 'e', 's', 'b']),    # Edit > Set Default Focus > Bus Object
        # Encoder button ---
        (0x000000, '',        [Kc.ALT, Kc.E, Kc.L, Kc.I])  # Edit > Select Mode > Include (keep holding down the buttons otherwise the program things you press "l" without being in the alt-menu's)
    ]
}
