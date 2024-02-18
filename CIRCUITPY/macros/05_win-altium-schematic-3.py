# MACROPAD Hotkeys: Altium (advanced) Schematic commands for Windows
# BRECHTVE 14/07/2023

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values
from adafruit_hid.mouse import Mouse # REQUIRED if using Mouse.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Altium Schematic 1/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x002000, 'UpdSel',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'l', 0.05, 'l', 0.05, Kc.ENTER]),                 # Tools > Updated Selected from Libraries > (Press enter)
        (0x002020, 'Move',     [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'e', 0.05, 'm', 0.05, 'm']),                                 # Edit > Move > Move
        (0x200020, '`RstPrm',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, 0.05, {'buttons':Mouse.LEFT_BUTTON}, 0.25, -Kc.CONTROL, 0.05, '    ']), # (Rotate a component 4 times so it "resets" the parameter-locations)
        # 2nd row ----------
        (0x002000, 'SmaPDF',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'f', 0.05, 'm']),            # File > Smart PDF
        (0x002000, 'NumSch',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'a', 0.05, 't']), # Tools > Annotation > Number Schematic Sheets
        (0x002000, '*NumSch',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'a', 0.05, 'm']), # Tools > Annotation > Annotate Compiled Sheets
        # 3rd row ----------
        (0x200000, 'OffSh',    [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'c']),            # Place > Off Sheet Connector
        (0x200020, 'ToFront',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'e', 0.05, 'm', 0.05, 'f']), # Edit > Move > Send to Front
        (0x200020, 'ToBack',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'e', 0.05, 'm', 0.05, 'b']), # Edit > Move > Send to Back
        # 4th row ----------
        (0x002000, 'Annota',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'a', 0.05, 'u', 0.05, Kc.ENTER]), # Tools > Annotation > Annotate Schematics Quietly > (Press yes)
        (0x002000, 'ValProj',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'c', 0.05, 'c']),                            # Project > Validate PCB Project
        (0x002020, 'Lasso',    [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'e', 0.05, 's', 0.05, 'e']),                 # Edit > Select > Lasso Select
        # Encoder button ---
        (0x000000, '',         [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'c']) # Tools > Cross Probe
    ]
}
