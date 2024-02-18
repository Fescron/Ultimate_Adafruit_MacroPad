# MACROPAD Hotkeys: Windows shortcuts for Zuken - CR-8000
# BRECHTVE 29/11/2023

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'CR-8000 Alig/Sel 1/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        # (0x202000, 'hJstGp',  [Kc.ALT, Kc.R, Kc.N, Kc.O]),        # Draw > Align Object > Justify Objects Horizontally at the Specified Gap
        (0x202000, 'Rotate',  [Kc.ALT, Kc.R, Kc.O, -Kc.R, Kc.R]), # Draw > Rotate > Rotate 90 Deg (Clockwise)
        (0x200000, 'TOP',     [Kc.ALT, Kc.R, Kc.N, Kc.T]),        # Draw > Align Object > Justify to Top
        # TODO Move > Rotate > Flip vertically (?)
        (0x202000, 'vJstGp',  [Kc.ALT, Kc.R, Kc.N, Kc.E]),        # Draw > Align Object > Justify Objects Vertically at the Specified Gap
        # 2nd row ----------
        (0x200000, '   LEFT', [Kc.ALT, Kc.R, Kc.N, Kc.L]),        # Draw > Align Object > Justify to Left
        (0x200000, 'GRD',     [Kc.ALT, Kc.R, Kc.N, Kc.G]),        # Draw > Align Object > Align to Grid
        (0x200000, 'RIGHT   ',[Kc.ALT, Kc.R, Kc.N, -Kc.R, Kc.R]), # Draw > Align Object > Justify to Right
        # 3rd row ----------
        (0x002020, '[net]',   [Kc.ALT, Kc.E, Kc.S, Kc.N]),        # Edit > Set Default Focus > Net Object
        (0x200020, '[part]',  [Kc.ALT, Kc.E, Kc.S, Kc.P]),        # Edit > Set Default Focus > Part
        # (0x200000, 'BOT',     [Kc.ALT, Kc.R, Kc.N, Kc.B]),        # Draw > Align Object > Justify to Bottom
        (0x002020, '[>net]',  [Kc.ALT, Kc.E, Kc.S, -Kc.E, Kc.E]), # Edit > Set Default Focus > Net with Equal Potential
        # 4th row ----------
        (0x200020, '[main]',  [Kc.ALT, Kc.E, Kc.S, Kc.M]),        # Edit > Set Default Focus > Main Object
        (0x200020, '[prop]',  [Kc.ALT, Kc.E, Kc.S, Kc.V]),        # Edit > Set Default Focus > Property Viewer
        (0x002020, '[bus]',   [Kc.ALT, Kc.E, Kc.S, Kc.B]),        # Edit > Set Default Focus > Bus Object
        # Encoder button ---
        (0x000000, '',        [Kc.ALT, Kc.E, Kc.L, Kc.I])         # Edit > Select Mode > Include
    ]
}
