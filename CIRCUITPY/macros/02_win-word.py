# MACROPAD Hotkeys: Windows Microsoft Office (Word) (Dutch)
# BRECHTVE 09/11/2022

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values
from adafruit_hid.mouse import Mouse # REQUIRED if using Mouse.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Word             1/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x200020, '[>`',     [Kc.ALT, Kc.KEYPAD_ONE, -Kc.KEYPAD_ONE, Kc.KEYPAD_SIX, -Kc.KEYPAD_SIX, -Kc.ALT, Kc.CONTROL, Kc.SPACE]), # "►" + Clear All Formatting
		(0x202000, 'frac',    [Kc.ALT, 'je', Kc.ALT, 'b', Kc.ENTER]), # Vergelijking > Breuk > (enter)
        (0x202000, '`C+V Tx', [{'buttons':Mouse.RIGHT_BUTTON}, {'buttons':-Mouse.RIGHT_BUTTON}, 't']), # Rightclick > Only keep text (paste)
        # 2nd row ----------
        # (0x002020, '`VCell',  [{'buttons':Mouse.RIGHT_BUTTON}, {'buttons':-Mouse.RIGHT_BUTTON}, 'h', Kc.ALT, 'e', -Kc.ALT, Kc.TAB, -Kc.TAB, 'c', Kc.TAB, -Kc.TAB, Kc.TAB, -Kc.TAB, Kc.ENTER]), # (Rightclick in (selected) cells) > Tabeleigenschappen > Cel > TAB > Centrum > (press OK)
        (0x000020, 'VCell',   [Kc.ALT, 'jl', Kc.ALT, 'ei', Kc.ALT, 'e', Kc.ALT, 'c', -Kc.ALT, Kc.TAB, -Kc.TAB, Kc.TAB, -Kc.TAB, Kc.ENTER]), # Indeling > Eigenschappen > Cel > Centrum > (press OK)
        (0x002000, '+Captn',  [Kc.ALT, 'l', Kc.ALT, 'p']),   # Verwijzingen > Bijschrift invoegen
        (0x002000, '+Refer',  [Kc.ALT, 'l', Kc.ALT, 'e']),   # Verwijzingen > Kruisverwijzing
        # 3rd row ----------
        # (0x002020, '`TblCol', [{'buttons':Mouse.RIGHT_BUTTON}, {'buttons':-Mouse.RIGHT_BUTTON}, 'h', 'k', Kc.TAB]), # (Rightclick in cell) > Tabeleigenschappen > Kolom > TAB
        (0x002020, 'TblCol',  [Kc.ALT, 'jl', Kc.ALT, 'ei', Kc.ALT, 'k']), # Indeling > Eigenschappen > Kolom
		(0x002020, '-Width',  [Kc.ALT, 'u', Kc.ALT, 'v']),                # Voorkeursbreedte > Volgende kolom
		(0x002020, 'Close',   [Kc.TAB, -Kc.TAB, Kc.ENTER]),               # (Press OK)
        # 4th row ----------
        # (0x002000, '`+Row',   [{'buttons':Mouse.RIGHT_BUTTON}, {'buttons':-Mouse.RIGHT_BUTTON}, 'i', Kc.ENTER, -Kc.ENTER, 'r']), # (Rightclick in cell) > Invoegen (ENTER to select) > Rijen onder invoeren
        (0x200000, '+Row',    [Kc.ALT, 'jl', Kc.ALT, 'fi']), # Indeling > Hieronder invoegen
        (0x200000, '+Itmze',  [Kc.ALT, 'r', Kc.ALT, 'oo', Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.ENTER]), # Start > Opsomming > Right-arrow (select bullet) > Enter
        (0x202000, '-Size',   [Kc.ALT, 'r', Kc.ALT, '71', Kc.ALT, 'r', Kc.ALT, '71', Kc.ALT, 'r', Kc.ALT, '71']), # Start > Tekstgrootte verkleinen (3x)
        # Encoder button ---
        (0x000000, '',        [])
    ]
}
