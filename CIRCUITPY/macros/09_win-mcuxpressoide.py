# MACROPAD Hotkeys: Embedded Debugging commands for Windows
# BRECHTVE 21/06/2022

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'MCUXpresso IDE   2/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
		(0x002020, 'Debug',   [Kc.F11]),
        (0x000000, '',        []),
        (0x200020, 'Reset`',  [Kc.SHIFT, Kc.F11]), # Custom keybind
        # 2nd row ----------
		(0x002000, 'Resume`', [Kc.F8]), # Custom keybind
        (0x200020, 'Suspnd',  [Kc.CONTROL, Kc.F8]),
        (0x200000, 'Termnt',  [Kc.CONTROL, Kc.F2]),
        # 3rd row ----------
		(0x202000, 'Into',    [Kc.F5]),
        (0x202000, 'Over',    [Kc.F6]),
        (0x202000, 'Return',  [Kc.F7]),
        # 4th row ----------
		(0x000020, 'PrEdit',  [Kc.CONTROL, 'q']),
        (0x000000, '',        []),
        (0x000020, 'NeEdit',  [Kc.CONTROL, Kc.ALT, Kc.RIGHT_ARROW]),
        # Encoder button ---
        (0x000000, '',        [])
    ]
}
