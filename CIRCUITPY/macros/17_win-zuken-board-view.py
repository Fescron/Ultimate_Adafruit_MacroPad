# MACROPAD Hotkeys: Windows "shortcuts" for Zuken - Design View
# BRECHTVE 30/12/2022

# SETTINGS: GoToMyPC = windowed, OCE-PC = 2560x1440 (100%), Dekimo-PC = 3440x1440 (100%), PowerToys>FancyZones: left-zone = 2400x1400

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values
from adafruit_hid.mouse import Mouse # REQUIRED if using Mouse.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'CR-8000 BrdView  2/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x002000, 'Layers',  [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}]),
        # (0x200000, 'Cond1',   [{'x':-3000}, {'y':-1000}, {'x':+1320}, {'y':+573}, {'buttons':Mouse.LEFT_BUTTON}]),
        # (0x202000, 'Cond2',   [{'x':-3000}, {'y':-1000}, {'x':+1320}, {'y':+592}, {'buttons':Mouse.LEFT_BUTTON}]),
        # (0x200020, 'Cond3',   [{'x':-3000}, {'y':-1000}, {'x':+1320}, {'y':+610}, {'buttons':Mouse.LEFT_BUTTON}]),
        # (0x000020, 'Cond4',   [{'x':-3000}, {'y':-1000}, {'x':+1320}, {'y':+630}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x002020, 'LayOrd',  []),
        (0x002020, 'NetCol',  [{'x':-3000}, {'y':-1000}, {'x':+115}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1048}, {'y':+465}, {'buttons':Mouse.RIGHT_BUTTON}, {'buttons':-Mouse.RIGHT_BUTTON}, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.ENTER, -Kc.ENTER, {'x':-83}, {'y':+310}, {'buttons':Mouse.LEFT_BUTTON}]),
        # 2nd row ----------
        (0x002000, 'OK',      [{'x':-3000}, {'y':-1000}, {'x':+1060}, {'y':+905}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x000000, '',        []),
        (0x000000, '',        []),
        # 3rd row ----------
        (0x000000, '',        []),
        (0x202000, ' 2_MID',  [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+517}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-260}, {'y':+313}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x200020, ' 3_MID',  [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+535}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-260}, {'y':+295}, {'buttons':Mouse.LEFT_BUTTON}]),
        # 4th row ----------
        (0x202020, 'PreVw',   [{'x':-3000}, {'y':-1000}, {'x':+315}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x200000, 'A1_TOP',  [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+498}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-260}, {'y':+332}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x000020, 'B4_BOT',  [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+555}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-260}, {'y':+275}, {'buttons':Mouse.LEFT_BUTTON}]),
        # Encoder button ---
        (0x000000, '',        [])
    ]
}
