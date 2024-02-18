# MACROPAD Hotkeys: Windows "shortcuts" for Zuken - Design View
# BRECHTVE 25/01/2024

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values
from adafruit_hid.mouse import Mouse # REQUIRED if using Mouse.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'CR-8000 BrdView  2/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        # (0x002000, 'Layers',  [Kc.ALT, 'v', 's']), # View > Layer Settings
        (0x002000, 'Layers',  [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}]),
        # (0x200000, 'Cond1',   [{'x':-3000}, {'y':-1000}, {'x':+1320}, {'y':+573}, {'buttons':Mouse.LEFT_BUTTON}]),
        # (0x202000, 'Cond2',   [{'x':-3000}, {'y':-1000}, {'x':+1320}, {'y':+592}, {'buttons':Mouse.LEFT_BUTTON}]),
        # (0x200020, 'Cond3',   [{'x':-3000}, {'y':-1000}, {'x':+1320}, {'y':+610}, {'buttons':Mouse.LEFT_BUTTON}]),
        # (0x000020, 'Cond4',   [{'x':-3000}, {'y':-1000}, {'x':+1320}, {'y':+630}, {'buttons':Mouse.LEFT_BUTTON}]),
        # (0x002000, 'LayOrd',  [Kc.ALT, 'v', 'l']), # View > Layer Display Order
        (0x002000, 'LayOrd',  [{'x':-3000}, {'y':-1000}, {'x':+87}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}]),
        # (0x002000, 'NetCol',  [Kc.ALT, 'v', 'n']), # View > Net Displayed Color Settings
        # (0x002020, 'NetClr',  [{'x':-3000}, {'y':-1000}, {'x':+115}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x002020, '-NtClr',  [{'x':-3000}, {'y':-1000}, {'x':+115}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1048}, {'y':+465}, {'buttons':Mouse.RIGHT_BUTTON}, {'buttons':-Mouse.RIGHT_BUTTON}, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.ENTER, -Kc.ENTER, {'x':-83}, {'y':+310}, {'buttons':Mouse.LEFT_BUTTON}]),
        # 2nd row ----------
        # (0x002000, 'Lay OK',  [{'x':-3000}, {'y':-1000}, {'x':+1060}, {'y':+905}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x202000, '(TP=A)',  []),
        (0x202020, '(BT=B)',  []),
        # (0x002000, 'PreVw',   [Kc.ALT, 'v', 'r']), # View > Previous View
        (0x202020, 'PreVw',   [{'x':-3000}, {'y':-1000}, {'x':+315}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}]),
        # 3rd row ----------
        # (0x200000, '1_TOP',   [Kc.ALT, 'v', 's', -Kc.ALT, {'x':-3000}, {'y':-1000}, {'x':+1813}, {'y':+572}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-242}, {'y':+368}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x200000, '1_TOP',   [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+498}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-260}, {'y':+332}, {'buttons':Mouse.LEFT_BUTTON}]),
        # (0x202000, '2_MID',   [Kc.ALT, 'v', 's', -Kc.ALT, {'x':-3000}, {'y':-1000}, {'x':+1813}, {'y':+590}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-242}, {'y':+350}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x202000, '2_MID',   [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+517}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-260}, {'y':+313}, {'buttons':Mouse.LEFT_BUTTON}]),
        # (0x002020, '3_MID',   [Kc.ALT, 'v', 's', -Kc.ALT, {'x':-3000}, {'y':-1000}, {'x':+1813}, {'y':+608}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-242}, {'y':+332}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x002020, '3_MID',   [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+535}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-260}, {'y':+295}, {'buttons':Mouse.LEFT_BUTTON}]),
        # 4th row ----------
        # (0x000020, '4_BOT',   [Kc.ALT, 'v', 's', -Kc.ALT, {'x':-3000}, {'y':-1000}, {'x':+1813}, {'y':+626}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-242}, {'y':+314}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x000020, '4_BOT',   [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+555}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-260}, {'y':+275}, {'buttons':Mouse.LEFT_BUTTON}]),
        # (0x200020, '5_MID',   [Kc.ALT, 'v', 's', -Kc.ALT, {'x':-3000}, {'y':-1000}, {'x':+1813}, {'y':+643}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-242}, {'y':+297}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x200020, '5_MID',   [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+575}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-260}, {'y':+255}, {'buttons':Mouse.LEFT_BUTTON}]),
        # (0x002000, '6_BOT',   [Kc.ALT, 'v', 's', -Kc.ALT, {'x':-3000}, {'y':-1000}, {'x':+1813}, {'y':+663}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-242}, {'y':+280}, {'buttons':Mouse.LEFT_BUTTON}]),
        (0x002000, '6_BOT',   [{'x':-3000}, {'y':-1000}, {'x':+35}, {'y':+75}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':+1285}, {'y':+595}, {'buttons':Mouse.LEFT_BUTTON}, {'buttons':-Mouse.LEFT_BUTTON}, {'x':-260}, {'y':+235}, {'buttons':Mouse.LEFT_BUTTON}]),
        # Encoder button ---
        (0x000000, '',        [])
    ]
}
