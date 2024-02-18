# MACROPAD Hotkeys: Windows Microsoft Office (Word) (Dutch)
# BRECHTVE 08/02/2024

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values
# from adafruit_hid.mouse import Mouse # REQUIRED if using Mouse.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Word Table/Varia 1/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x200020, '^(...)',  [Kc.CONTROL, Kc.SHIFT, '+']),   # Superscript
        (0x000020, 'VCell',   [Kc.ALT, 'jl', 'q']),           # Indeling > Centreren
        (0x002020, 'ShwTbl',  [Kc.ALT, 'jl', 'lr']),          # Indeling > Rasterlijnen weergeven
        # 2nd row ----------
        (0x002000, '+Tbl',    [Kc.ALT, 'n', 'ba', Kc.ENTER]), # Invoegen > Tabel > (enter)
        (0x002000, 'DrwTbl',  [Kc.ALT, 'jl', 'aa']),          # Indeling > Tekenen
        (0x200000, 'GumTbl',  [Kc.ALT, 'jl', '7']),           # Indeling > Gum
        # 3rd row ----------
        (0x200000, '-Row  ',  [Kc.ALT, 'jl', 'we', 'r']),     # Indeling > Verwijderen > Rijen verwijderen
        (0x200000, '-Col  ',  [Kc.ALT, 'jl', 'we', 'k']),     # Indeling > Verwijderen > Kolommen verwijderen
        (0x202000, '+Size3',  [Kc.ALT, 'r', 'tl', Kc.ALT, 'r', 'tl', Kc.ALT, 'r', 'tl']), # Start > Tekstgrootte vergroten (3x)
        # 4th row ----------
        (0x002000, '+Row_v',  [Kc.ALT, 'jl', 'fi']),          # Indeling > Hieronder invoegen
        (0x002000, '+Col_>',  [Kc.ALT, 'jl', 'te']),          # Indeling > Rechts invoegen
        (0x202000, '-Size3',  [Kc.ALT, 'r', '71', Kc.ALT, 'r', '71', Kc.ALT, 'r', '71']), # Decrease text size (3x)
        # Encoder button ---
        (0x000000, '',        [])
    ]
}
