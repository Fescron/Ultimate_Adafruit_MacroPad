# MACROPAD Hotkeys: Windows shortcuts for Zuken - CR-8000
# BRECHTVE 22/11/2022

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'CR-8000 Hierch   2/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x200000, 'DRC',     [Kc.ALT, 't', 'r', 'c', Kc.ENTER]), # Tools > Rule Check > Circuit > (ENTER)
        (0x000000, '',        []),
        (0x000000, '',        []),
        # 2nd row ----------
        # (0x002000, '*shSym',  [Kc.ALT, 'i', 'e']), # Hierarchy > Edit Sheet Symbol
        # (0x200000, 'I*Sym',   [Kc.ALT, 'e', 'x']), # Edit > Start of Edit Symbol Figure on Circuit (x)
        # (0x200000, 'O*Sym',   [Kc.ALT, 'e', 'z']), # Edit > End of Edit Symbol Figure on Circuit (z)
        (0x000000, '',        []),
        (0x000000, '',        []),
        (0x000000, '',        []),
        # 3rd row ----------
        (0x200000, '*Sym',    [Kc.ALT, 'e', 'g']), # Edit > Edit Symbol Figure
        (0x200000, '%hieCon', [Kc.ALT, 'i', 'm']), # Hierarchy > Generate Block Symbol Pins
        (0x002020, '%comp',   [Kc.ALT, Kc.A, Kc.L, Kc.S]), # Design Assist > Reload Symbol Figure > Load Symbol using Current Path (keep holding down the buttons otherwise the program things you press "l" without being in the alt-menu's)
        # 4th row ----------
        (0x002000, '+shSym',  [Kc.ALT, 'i', 'g']), # Hierarchy > Generate Sheet Symbol
        (0x000020, 'HieBlk',  [Kc.ALT, 'i', '2']), # Hierarchy > Circuit Block (2)
        (0x000020, 'HieCon',  [Kc.ALT, 'i', 'y']), # Hierarchy > Hierarchy Connector
        # Encoder button ---
        (0x000000, '',        [Kc.ALT, Kc.E, Kc.L, Kc.I]) # Edit > Select Mode > Include (keep holding down the buttons otherwise the program things you press "l" without being in the alt-menu's)
    ]
}
