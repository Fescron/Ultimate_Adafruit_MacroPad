# MACROPAD Hotkeys: Altium (advanced) Schematic commands for Windows
# BRECHTVE 11/01/2023

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values
from adafruit_hid.mouse import Mouse # REQUIRED if using Mouse.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Altium Schematic 2/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x002000, 'Sh Ent',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'e']), # Place > Sheet Entry
        (0x002000, 'Sh Sym ', [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 's']), # Place > Sheet Symbol
        (0x002000, '`Sh Sym', [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, {'buttons':Mouse.RIGHT_BUTTON}, 0.05, {'buttons':-Mouse.RIGHT_BUTTON}, 'h', 0.05, 'y']), # Rightclick > Sheet Actions > Create Sheet Symbol From Sheet
	    # (0x002000, 'Dev Sh',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'i']), # Place > Device Sheet Symbol
        # 2nd row ----------
        # (0x202000, 'Annotat', [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'a', 0.05, 'a']), # Tools > Annotation > Annotate Schematics
        # (0x200000, '`F/NF',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, {'buttons':Mouse.RIGHT_BUTTON}, 0.05, {'buttons':-Mouse.RIGHT_BUTTON}, 't', 0.1, Kc.ENTER]), # Rightclick > Part Actions > Toggle Fitted/Not Fitted
        (0x200000, 'SVNlk',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'c', 0.05, 'e', 0.05, 'l', 0.05, Kc.ENTER]), # Project > History & Version Control > Lock
        (0x202000, 'ToBack',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'e', 0.05, 'm', 0.05, 'b']), # Edit > Move > Send to Back
		(0x002000, '`Syn Sh', [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, {'buttons':Mouse.RIGHT_BUTTON}, 0.05, {'buttons':-Mouse.RIGHT_BUTTON}, 's', 0.05, Kc.ENTER, 0.05, -Kc.ENTER, 'p']), # Rightclick > Sheet Symbol Actions > Synchronize Sheet Entries and Ports
        # 3rd row ----------
        (0x200020, 'HarEnt',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'h', 0.05, 'e']), # Place > Harness > Harness Entry
		(0x200020, 'SigHar',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'h', 0.05, 'h']), # Place > Harness > Signal Harness
		(0x200020, 'HarCon',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'h', 0.05, 'c']), # Place > Harness > Harness Connector
        # 4th row ----------
		(0x000020, 'BusEnt',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'u']), # Place > Bus Entry
		(0x000020, 'Bus',     [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'b']), # Place > Bus
        # (0x200020, 'PreHar',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'h', 0.05, 'p']), # Place > Harness > Predefined Harness Connector
        (0x002000, 'Port',    [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'r', 0.05, Kc.ENTER]), # Place > Port
        # Encoder button ---
        (0x000000, '',        [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'c'])  # Tools > Cross Probe
    ]
}
