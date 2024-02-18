# MACROPAD Hotkeys: Windows shortcuts for Zuken - CR-8000
# BRECHTVE 25/09/2023

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'CR-8000          1/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x202000, 'Text',    [Kc.ALT, Kc.R, Kc.T]),        # Draw > Text
        (0x202000, 'Line',    [Kc.ALT, Kc.R, Kc.L]),        # Draw > Line/Polyline
        (0x202000, 'Rect',    [Kc.ALT, Kc.R, -Kc.R, Kc.R]), # Draw > Rectangle
        # 2nd row ----------
        (0x002000, '+conn',   [Kc.ALT, Kc.D, Kc.T]),        # Design > Connect
        (0x200000, '-conn',   [Kc.ALT, Kc.D, Kc.R]),        # Design > Release Connection
        (0x200020, '<incl>',  [Kc.ALT, Kc.E, Kc.L, Kc.I]),  # Edit > Select Mode > Include
        # 3rd row ----------
        (0x002020, '+comp',   [Kc.ALT, Kc.D, Kc.C]),        # Design > Components Library
        (0x000020, 'Label',   [Kc.ALT, Kc.D, Kc.L]),        # Design > Net/Bus Label
        (0x200020, '<ovrl>',  [Kc.ALT, Kc.E, Kc.L, Kc.O]),  # Edit > Select Mode > Overlap
        # 4th row ----------
        (0x000020, 'Net',     [Kc.ALT, Kc.D, Kc.N]),        # Design > Net
        (0x000020, 'Bus',     [Kc.ALT, Kc.D, Kc.B]),        # Design > Bus
        (0x600000, 'Attr',    [Kc.ALT, Kc.V, Kc.Y]),        # View > Property
        # Encoder button ---
        (0x000000, '',        [Kc.ALT, Kc.E, Kc.L, Kc.I])   # Edit > Select Mode > Include
    ]
}
