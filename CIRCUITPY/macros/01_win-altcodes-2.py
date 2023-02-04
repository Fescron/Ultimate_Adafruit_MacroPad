# MACROPAD Hotkeys: Windows alt-codes
# BRECHTVE 12/01/2023

# If the alt-codes are not producing the right symbols there are two main options:
#   - Enable Unicode-alt-entry in Windows and use the macro-lines using this way of entry (the labels end with "`")
#     To enable this functionality in windows, type the following in the terminal: "REG ADD "HKCU\Control Panel\Input Method" /v EnableHexNumpad /t REG_SZ /d 1"
#   - Change the "system locale" to use the expected "code page": Control Panel > Clock and Region > Region > Administrative> Change system locale: "English (United States)"
#     To check if the expected code-page is used (437) type "chcp" in the terminal ("Dutch (Belgium)" produces "850")

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'AltCodes         2/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x200020, 'bullet',  [Kc.ALT, Kc.KEYPAD_SEVEN]), # "•" = alt+7 (= alt+0149)
        # (0x002020, 'Lambda`', [Kc.ALT, Kc.KEYPAD_PLUS, -Kc.KEYPAD_PLUS, Kc.KEYPAD_ZERO, -Kc.KEYPAD_ZERO, Kc.KEYPAD_THREE, -Kc.KEYPAD_THREE, Kc.B, -Kc.B, Kc.B]), # "λ" = +03BB (unicode)
        # (0x002020, 'Lambda',  [Kc.ALT, Kc.KEYPAD_NINE, -Kc.KEYPAD_NINE, Kc.KEYPAD_FIVE, -Kc.KEYPAD_FIVE, Kc.KEYPAD_FIVE]), # "λ" = alt+955 [BROKEN]
        (0x200020, 'NBSp',    [Kc.ALT, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_FIVE, -Kc.KEYPAD_FIVE, Kc.KEYPAD_FIVE]), # Non breaking space = alt+255
		(0x202000, '^',       [Kc.ALT, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_FOUR]), # "↑" = alt+24
        # 2nd row ----------
        # (0x200000, 'Infty`',  [Kc.ALT, Kc.KEYPAD_PLUS, -Kc.KEYPAD_PLUS, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_ONE, -Kc.KEYPAD_ONE, Kc.E]), # "∞" = +221E (unicode)
        (0x002020, 'Infty',   [Kc.ALT, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_THREE, -Kc.KEYPAD_THREE, Kc.KEYPAD_SIX]), # "∞" = alt+236
        # (0x002020, 'Pi`',     [Kc.ALT, Kc.KEYPAD_PLUS, -Kc.KEYPAD_PLUS, Kc.KEYPAD_ZERO, -Kc.KEYPAD_ZERO, Kc.KEYPAD_THREE, -Kc.KEYPAD_THREE, Kc.C, -Kc.C, Kc.KEYPAD_ZERO]), # "π" = +03C0 (unicode)
        (0x002020, 'Pi',      [Kc.ALT, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_SEVEN]), # "π" = alt+227
		(0x202000, 'V',       [Kc.ALT, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_FIVE]), # "↓" = alt+25
        # 3rd row ----------
        (0x200020, 'EnDash',  [Kc.ALT, Kc.KEYPAD_ZERO, -Kc.KEYPAD_ZERO, Kc.KEYPAD_ONE, -Kc.KEYPAD_ONE, Kc.KEYPAD_FIVE, -Kc.KEYPAD_FIVE, Kc.KEYPAD_ZERO]), # "–" = alt+0150
        (0x200020, 'EmDash',  [Kc.ALT, Kc.KEYPAD_ZERO, -Kc.KEYPAD_ZERO, Kc.KEYPAD_ONE, -Kc.KEYPAD_ONE, Kc.KEYPAD_FIVE, -Kc.KEYPAD_FIVE, Kc.KEYPAD_ONE]),  # "—" = alt+0151
        (0x000000, '',        []),
		# (0x200000, '=>',      [Kc.ALT, Kc.KEYPAD_PLUS, -Kc.KEYPAD_PLUS, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_ONE, -Kc.KEYPAD_ONE, Kc.D, -Kc.D, Kc.KEYPAD_TWO]),  # "⇒" = +21D2 (unicode)
		# (0x200000, '<=>',     [Kc.ALT, Kc.KEYPAD_PLUS, -Kc.KEYPAD_PLUS, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_ONE, -Kc.KEYPAD_ONE, Kc.D, -Kc.D, Kc.KEYPAD_FOUR]), # "⇔" = +21D4 (unicode)
		# (0x200000, '<=',      [Kc.ALT, Kc.KEYPAD_PLUS, -Kc.KEYPAD_PLUS, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_ONE, -Kc.KEYPAD_ONE, Kc.D, -Kc.D, Kc.KEYPAD_ZERO]), # "⇐" = +21D0 (unicode)
        # (0x202000, '<scrn',   [Kc.WINDOWS, Kc.SHIFT, Kc.LEFT_ARROW]),  # Move window to left screen
        # (0x200000, 'MAX',     [Kc.WINDOWS, Kc.UP_ARROW]),              # Maximize window
        # (0x202000, 'scrn>',   [Kc.WINDOWS, Kc.SHIFT, Kc.RIGHT_ARROW]), # Move window to right screen
        # 4th row ----------
        (0x000000, '',        []),
        (0x000000, '',        []),
        (0x000000, '',        []),
        # (0x200000, '<wind',   [Kc.WINDOWS, Kc.LEFT_ARROW]),  # Move window to left-side
        # (0x200000, 'MIN',     [Kc.WINDOWS, Kc.DOWN_ARROW]),  # Minimize window
        # (0x200000, 'wind>',   [Kc.WINDOWS, Kc.RIGHT_ARROW]), # Move window to right-side
        # Encoder button ---
        (0x000000, '',        [])
    ]
}
