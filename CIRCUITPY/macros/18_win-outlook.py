# MACROPAD Hotkeys: Windows Microsoft Outlook (Dutch)
# BRECHTVE 07/02/2024

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values
from adafruit_hid.mouse import Mouse # REQUIRED if using Mouse.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Outlook          1/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x200020, '[>_`',    [Kc.ALT, Kc.KEYPAD_ONE, -Kc.KEYPAD_ONE, Kc.KEYPAD_SIX, -Kc.KEYPAD_SIX, -Kc.ALT, Kc.CONTROL, Kc.SPACE, -Kc.CONTROL, -Kc.SPACE, Kc.SPACE]), # "►" + Clear All Formatting + space
        (0x002020, '>DIR2',   [Kc.CONTROL, Kc.SHIFT, '2']), # Custom snelle stap
        (0x002020, '>DIR4',   [Kc.CONTROL, Kc.SHIFT, '4']), # Custom snelle stap
        # 2nd row ----------
        (0x002020, '>DIR1',   [Kc.CONTROL, Kc.SHIFT, '1']), # Custom snelle stap
        (0x002020, '>DIR3',   [Kc.CONTROL, Kc.SHIFT, '3']), # Custom snelle stap
        (0x002020, '>DIR5',   [Kc.CONTROL, Kc.SHIFT, '5']), # Custom snelle stap
        # 3rd row ----------
        # (0x202000, '`Read',   [{'buttons':Mouse.RIGHT_BUTTON}, {'buttons':-Mouse.RIGHT_BUTTON}, 'm']), # Rightclick > Markeren als gelezen
        (0x002020, '>DIR6',  [Kc.CONTROL, Kc.SHIFT, '6']), # Custom snelle stap
        # (0x002000, '`-Flag',  [{'buttons':Mouse.RIGHT_BUTTON}, {'buttons':-Mouse.RIGHT_BUTTON}, 'p', 'w']), # Rightclick > Opvolgen > Vlag wissen
        (0x002000, '-Flag',   [Kc.ALT, -Kc.ALT, 'r', 'zt', 'p', 'w']), # Start > Labels > Opvolgen > Vlag Wissen
        (0x002020, '>DIR7',  [Kc.CONTROL, Kc.SHIFT, '7']), # Custom snelle stap
        # 4th row ----------
        # (0x202000, '`UnRead', [{'buttons':Mouse.RIGHT_BUTTON}, {'buttons':-Mouse.RIGHT_BUTTON}, 'z']), # Rightclick > Markeren als ongelezen
        (0x202000, 'Un/Read', [Kc.ALT, -Kc.ALT, 'r', 'zt', 'g1']),     # Start > Labels > Ongelezen/Gelezen
        # (0x200000, '`+Flag',  [{'buttons':Mouse.RIGHT_BUTTON}, {'buttons':-Mouse.RIGHT_BUTTON}, 'p', 'g']), # Rightclick > Opvolgen > Geen datum
        (0x200000, '+Flag',   [Kc.ALT, -Kc.ALT, 'r', 'zt', 'p', 'g']), # Start > Labels > Opvolgen > Geen Datum
        (0x000020, 'Mvg,',    ["Mvg,\nBrecht\n"]),
        # Encoder button ---
        (0x000000, '',        [])
    ]
}
