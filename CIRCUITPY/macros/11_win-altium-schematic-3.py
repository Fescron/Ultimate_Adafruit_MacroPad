# MACROPAD Hotkeys: Altium Schematic Net Color commands for Windows
# BRECHTVE 23/06/2022

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Altium Schem Col 2/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x202020, 'Custom`', [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, Kc.ALT, Kc.SHIFT, '0']), # View > Set Net Colors > Custom Color (custom command)
		(0x000000, '',        []),
		(0x202020, 'ClnCol`', [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, Kc.ALT, Kc.SHIFT, '-']), # View > Set Net Colors > Clean Net Color (custom command)
        # 2nd row ----------
        (0x000020, 'Blue`',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, Kc.ALT, Kc.SHIFT, '1']), # View > Set Net Colors > Blue (custom command)
        (0x052005, 'lGreen`', [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, Kc.ALT, Kc.SHIFT, '2']), # View > Set Net Colors > Light Green (custom command)
        (0x002020, 'lBlue`',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, Kc.ALT, Kc.SHIFT, '3']), # View > Set Net Colors > Light Blue (custom command)
        # 3rd row ----------
		(0x200000, 'Red`',    [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, Kc.ALT, Kc.SHIFT, '4']), # View > Set Net Colors > Red (custom command)
        (0x200020, 'Fuchsi`', [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, Kc.ALT, Kc.SHIFT, '5']), # View > Set Net Colors > Fuchsia (custom command)
        (0x202000, 'Yellow`', [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, Kc.ALT, Kc.SHIFT, '6']), # View > Set Net Colors > Yellow (custom command)
        # 4th row ----------
        (0x002000, 'dGreen`', [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, Kc.ALT, Kc.SHIFT, '7']), # View > Set Net Colors > Dark Green (custom command)
		(0x000000, '',        []),
        (0x000000, '',        []),
        # Encoder button ---
        (0x000000, '',        [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'c']) # Tools > Cross Probe
    ]
}
