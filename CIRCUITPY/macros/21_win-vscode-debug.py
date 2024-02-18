# MACROPAD Hotkeys: VScode Embedded Debugging for Windows
# BRECHTVE 06/06/2023

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'VScode debugging 1/1', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        #(0x002020, 'Debug',   [Kc.F11]),
        (0x000000, '',        []),
        (0x000000, '',        []),
        (0x000000, '',        []),
        # 2nd row ----------
        (0x000000, '',        []),
        (0x000000, '',        []),
        (0x200020, 'Restart', [Kc.CONTROL, Kc.SHIFT, Kc.F5]),
        # 3rd row ----------
        (0x002000, 'Cont.',   [Kc.F5]),
        (0x200020, 'Pause',   [Kc.F6]),
        (0x200000, 'Stop',    [Kc.SHIFT, Kc.F5]),
        # 4th row ----------
        (0x202000, 'StInto',  [Kc.F11]),
        (0x202000, 'StOver',  [Kc.F10]),
        (0x202000, 'StRetn',  [Kc.SHIFT, Kc.F11]),
        # Encoder button ---
        (0x000000, '',        [])
    ]
}
