# MACROPAD Hotkeys: Altium Layout validation queries for Windows
# BRECHTVE 07/12/2023

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Altium layCheck  2/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x202000, 'cDesi',  ["(ObjectKind = 'Text') And (StringType = 'Designator') And (AsMM(TextHeight) <> 0.7) And (AsMM(TextWidth) <> 0.13)"]),
        (0x202000, 'cPin1',  ["(ObjectKind = 'Text') And (StringText = '1') And ((Layer = 'TopOverlay') Or (Layer = 'Bottom Overlay')) And (AsMM(TextHeight) <> 0.7) And (AsMM(TextWidth) <> 0.13)"]),
        (0x000000, '',       []),
        # 2nd row ----------
        (0x202000, 'cComm',  ["(ObjectKind = 'Text') And (StringType = 'Comment') And (AsMM(TextHeight) <> 0.85) And (AsMM(TextWidth) <> 0.18)"]),
        (0x202000, 'cComm2', ["((ObjectKind = 'Text') And (StringText <> '1')) And ((Layer = 'TopOverlay') Or (Layer = 'Bottom Overlay')) And (StringType = 'Free') And (AsMM(TextHeight) <> 0.85) And (AsMM(TextWidth) <> 0.18)"]),
        (0x000000, '',       []),
        # 3rd row ----------
        (0x000000, '',       []),
        (0x000000, '',       []),
        (0x000000, '',       []),
        # 4th row ----------
        (0x000000, '',       []),
        (0x000000, '',       []),
        (0x000000, '',       []),
        # Encoder button ---
        (0x000000, '',       [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'c'])  # Tools > Cross Probe
    ]
}
