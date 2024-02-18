# MACROPAD Hotkeys: Windows Microsoft Office (Word) (Dutch)
# BRECHTVE 21/12/2023

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values
# from adafruit_hid.mouse import Mouse # REQUIRED if using Mouse.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Word Spacing     2/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x000020, '<col>',   [Kc.ESCAPE, -Kc.ESCAPE, Kc.ALT, 'jl', 'br']), # Indeling > Breedte
        (0x000020, '^fig^',   [Kc.ESCAPE, -Kc.ESCAPE, Kc.ALT, 'jp', 'h']),  # Afbeeldingsindeling > Hoogte
        (0x000020, '<fig>',   [Kc.ESCAPE, -Kc.ESCAPE, Kc.ALT, 'jp', 'rr']), # Afbeeldingsindeling > Breedte
        # 2nd row ----------
        (0x200000, '< -1.5',  [Kc.ALT, 'u', 'k', '-1.5', Kc.ENTER]),        # Indeling > Inspringing (Links)
        (0x200020, '10/_pt',  [Kc.ALT, 'u', 'v', '10', Kc.ENTER]),          # Indeling > Afstand (Voor)
        (0x200020, '_/10pt',  [Kc.ALT, 'u', 'b', '10', Kc.ENTER]),          # Indeling > Afstand (Na)
        # 3rd row ----------
        (0x200000, '< 0.1',   [Kc.ALT, 'u', 'k', '0.1', Kc.ENTER]),         # Indeling > Inspringing (Links)
        # (0x200000, '*Itmz1',  [Kc.ALT, 'u', 'k', '0.1', Kc.ENTER]),         # Indeling > Inspringing (Links)
        # (0x200000, '*Itm1/2', [Kc.ALT, 'u', 'k', '0.5', Kc.ENTER]),         # Indeling > Inspringing (Links)
        # (0x200000, '*Itmz2',  [Kc.ALT, 'u', 'k', '0.9', Kc.ENTER]),         # Indeling > Inspringing (Links)
        (0x200020, ' 2/2pt',  [Kc.ALT, 'u', 'v', '2', Kc.ENTER, Kc.ALT, 'u', 'b', '2', Kc.ENTER]), # Indeling > Afstand (Voor & Na)
        (0x200020, ' _/2pt',  [Kc.ALT, 'u', 'b', '2', Kc.ENTER]),           # Indeling > Afstand (Na)
        # 4th row ----------
        (0x200000, '< 0',     [Kc.ALT, 'u', 'k', '0', Kc.ENTER]),           # Indeling > Inspringing (Links)
        (0x200020, ' 0/0pt',  [Kc.ALT, 'u', 'v', '0', Kc.ENTER, Kc.ALT, 'u', 'b', '0', Kc.ENTER]), # Indeling > Afstand (Voor & Na)
        (0x200020, ' _/1pt',  [Kc.ALT, 'u', 'b', '1', Kc.ENTER]),           # Indeling > Afstand (Na)
        
        # Encoder button ---
        (0x000000, '',        [])
    ]
}
