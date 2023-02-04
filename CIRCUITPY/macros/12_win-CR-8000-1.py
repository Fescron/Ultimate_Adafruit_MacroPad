# MACROPAD Hotkeys: Windows shortcuts for Zuken - CR-8000
# BRECHTVE 18/11/2022

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'CR-8000          1/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
		(0x202000, 'Text',    [Kc.ALT, 'r', 't']),                                  # Draw > Text
        (0x202000, 'Line',    [Kc.ALT, Kc.R, Kc.L]),                                # Draw > Line/Polyline (keep holding down the buttons otherwise the program things you press "l" without being in the alt-menu's)
        (0x202000, 'Rect',    [Kc.ALT, 'r', 'r']),                                  # Draw > Rectangle
        # 2nd row ----------
        (0x002000, '+conn',   [Kc.ALT, 's', Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, 't']), # Sheet > Right-arrow (Design) > Connect
		(0x200000, '-conn',   [Kc.ALT, 's', Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, 'r']), # Sheet > Right-arrow (Design) > Release Connection
        (0x200020, '<incl>',  [Kc.ALT, Kc.E, Kc.L, Kc.I]),                          # Edit > Select Mode > Include (keep holding down the buttons otherwise the program things you press "l" without being in the alt-menu's)
        # 3rd row ----------
        (0x002020, '+comp',   [Kc.ALT, 's', Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, 'c']), # Sheet > Right-arrow (Design) > Components Library
        (0x000020, 'Label',   [Kc.ALT, Kc.S, Kc.RIGHT_ARROW, Kc.L]),                # Sheet > Right-arrow (Design) > Net/Bus Label (keep holding down the buttons otherwise the program things you press "l" without being in the alt-menu's)
        (0x200020, '<ovrl>',  [Kc.ALT, Kc.E, Kc.L, Kc.O]),                          # Edit > Select Mode > Overlap (keep holding down the buttons otherwise the program things you press "l" without being in the alt-menu's)
        # 4th row ----------
        (0x000020, 'Net',     [Kc.ALT, 's', Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, 'n']), # Sheet > Right-arrow (Design) > Net
        (0x000020, 'Bus',     [Kc.ALT, 's', Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, 'b']), # Sheet > Right-arrow (Design) > Bus
		(0x600000, 'Attr',    [Kc.ALT, 'v', 'y']),                                  # View > Property
        # Encoder button ---
        (0x000000, '',        [Kc.ALT, Kc.E, Kc.L, Kc.I])                           # Edit > Select Mode > Include (keep holding down the buttons otherwise the program things you press "l" without being in the alt-menu's)
    ]
}
