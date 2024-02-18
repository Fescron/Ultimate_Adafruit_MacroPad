# MACROPAD Hotkeys: Windows Altium Colors
# BRECHTVE 21/12/2023

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Altium Colors    1/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x000010, '#Wire',   ['000080']), # Dark Blue (wire, text)
        (0x000060, '#Comp',   ['0000FF']), # Blue (component)
        (0x002060, '#FrFil`', ['C9DAF8']), # Light Blue (text frame fill) [custom color]
        # 2nd row ----------
        (0x100000, '#LblBr',  ['800000']), # Dark Red (net/port label, borders, power)
        (0x600000, '#NfBlk',  ['FF0000']), # Red (NF, blanket)
        (0x600010, '#FrFil`', ['FFE0E0']), # Light Red (TODO-notes) [custom color]
        # 3rd row ----------
        (0x101000, '#ShtPr',  ['FFFF80']), # Light Yellow (sheet entry, port)
        (0x606000, '#CmpFil', ['FFFFB0']), # Light Yellow (component fill)
        (0x808010, '#Note  ', ['FFFF96']), # Light Yellow (note)
        # 4th row ----------
        (0x002000, '#Sheet',  ['80FF80']), # Light Green (sheet symbol)
        (0x808080, '#HrCnFil',['EDF2FB']), # White (harness connector fill)
        # (0x101010, '#RctFil', ['C0C0C0']), # Light Grey (ellipse/rectangle fill)
        (0x101010, '#RcFil`', ['999999']), # Light Grey (ellipse/rectangle fill) [custom color]
        # Encoder button ---
        (0x000000, '',        ['FF9900'])  # Orange (TODO-notes) [custom color]
    ]
}
