# MACROPAD Hotkeys: Windows shortcuts for Zuken - CR-8000
# BRECHTVE 29/11/2023

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'CR-8000 Hierch   2/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x200000, 'DRC',     [Kc.ALT, Kc.T, Kc.R, Kc.C, -Kc.ALT, -Kc.T, -Kc.R, -Kc.C, Kc.ENTER]), # Tools > Rule Check > Circuit > (ENTER)
        (0x202000, 'ReDes',   [Kc.ALT, Kc.A, Kc.R, Kc.C]), # Design Assist > Reference Allocator > Circuit Reference Allocator
        (0x202000, '+PDF',    [Kc.ALT, Kc.F, Kc.D, Kc.P]), # File > Document Data Generator > Pdf Generator
        # 2nd row ----------
        # (0x002000, '*shSym',  [Kc.ALT, Kc.I, Kc.E]),       # Hierarchy > Edit Sheet Symbol
        # (0x200000, 'I*Sym',   [Kc.ALT, Kc.E, Kc.X]),       # Edit > Start of Edit Symbol Figure on Circuit (x)
        # (0x200000, 'O*Sym',   [Kc.ALT, Kc.E, Kc.Z]),       # Edit > End of Edit Symbol Figure on Circuit (z)
        (0x002020, '1.%Sym',  [Kc.ALT, Kc.A, Kc.L, Kc.S]), # Design Assist > Reload Symbol Figure > Load Symbol using Current Path
        (0x002020, '2.%Part', [Kc.ALT, Kc.A, Kc.P, Kc.S, -Kc.ALT, -Kc.A, -Kc.P, -Kc.S, Kc.ENTER]), # Design Assist > Reload Parts Info > Selected Component > (ENTER)
        (0x202000, 'Grid',    [Kc.ALT, Kc.V, Kc.G]),        # View > Grid
        # 3rd row ----------
        (0x200000, '*Sym',    [Kc.ALT, Kc.E, Kc.G]),       # Edit > Edit Symbol Figure
        (0x200000, '%HieCon', [Kc.ALT, Kc.I, Kc.M]),       # Hierarchy > Generate Block Symbol Pins
        (0x200020, '*Sheet',  [Kc.ALT, Kc.S, Kc.T]),       # Sheet > Sheet Settings
        # 4th row ----------
        (0x002000, '+shSym',  [Kc.ALT, Kc.I, Kc.G]),       # Hierarchy > Generate Sheet Symbol
        (0x000020, 'HieBlk',  [Kc.ALT, Kc.I, Kc.TWO]),     # Hierarchy > Circuit Block (2)
        (0x000020, 'HieCon',  [Kc.ALT, Kc.I, Kc.Y]),       # Hierarchy > Hierarchy Connector
        # Encoder button ---
        (0x000000, '',        [Kc.ALT, Kc.E, Kc.L, Kc.I])  # Edit > Select Mode > Include
    ]
}
