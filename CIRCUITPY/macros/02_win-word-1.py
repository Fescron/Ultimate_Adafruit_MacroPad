# MACROPAD Hotkeys: Windows Microsoft Office (Word) (Dutch)
# BRECHTVE 22/12/2023

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values
# from adafruit_hid.mouse import Mouse # REQUIRED if using Mouse.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Word             1/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x202020, '-Format', [Kc.ALT, 'r', '41']),           # Start > Alle opmaak wissen
        (0x002020, '*Src',    [Kc.ALT, 'l', 'o']),            # Verwijzingen > Bronnen beheren
        (0x202000, '+Highl',  [Kc.ALT, 'r', 'me', Kc.ENTER]), # Start > Tekstmarkeringskleur > (enter)
        # 2nd row ----------
        (0x202020, '*tWhit',  [Kc.ALT, 'r', 'ke', Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.ENTER]), # Start > Tekstkleur
        (0x002000, '+Refer',  [Kc.ALT, 'l', 'e']),            # Verwijzingen > Kruisverwijzing
        (0x002020, '+Highl',  [Kc.ALT, 'r', 'me', Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.ENTER]), # Start > Tekstmarkeringskleur > (cyan)
        # 3rd row ----------
        (0x002000, '+fNote',  [Kc.ALT, 'l', 'v']),            # Verwijzingen > Voetnoot invoegen
        (0x002000, '+Captn',  [Kc.ALT, 'l', 'p']),            # Verwijzingen > Bijschrift invoegen
        (0x202020, '+Highl',  [Kc.ALT, 'r', 'me', Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW,
                               Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.ENTER ]), # Start > Tekstmarkeringskleur > (grijs))
        # 4th row ----------
        (0x002000, '+Itmze',  [Kc.ALT, 'r', 'oo', Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.ENTER]), # Start > Opsomming > 2x Right-arrow (select bullet) > Enter
        (0x002000, '+SrcRef', [Kc.ALT, 'l', 'a']),            # Verwijzingen > Citaat invoegen
        (0x202020, '-Highl',  [Kc.ALT, 'r', 'me', 'g']),      # Start > Tekstmarkeringskleur > Geen kleur
        # Encoder button ---
        (0x000000, '',        [])
    ]
}
