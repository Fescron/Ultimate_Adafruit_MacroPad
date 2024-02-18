# MACROPAD Hotkeys: Windows alt-codes
# BRECHTVE 15/08/2023

# If the alt-codes are not producing the right symbols there are two main options:
#   - Change the "system locale" to use the expected "code page": Control Panel > Clock and Region > Region > Administrative> Change system locale: "English (United States)"
#     To check if the expected code-page is used (437) type "chcp" in the terminal ("Dutch (Belgium)" produces "850")
#   - Enable Unicode-alt-entry in Windows and use the macro-lines using this way of entry (the labels end with "`")
#     To enable this functionality in windows, type the following in the terminal: "REG ADD "HKCU\Control Panel\Input Method" /v EnableHexNumpad /t REG_SZ /d 1"

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'AltCodes         1/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x200020, '[>',      [Kc.ALT, Kc.KEYPAD_ONE, -Kc.KEYPAD_ONE, Kc.KEYPAD_SIX]),   # "►" = alt+16
        (0x002020, 'Omega',   [Kc.ALT, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_THREE, -Kc.KEYPAD_THREE, Kc.KEYPAD_FOUR]), # "Ω" = alt+234
        # (0x002020, 'Omega`',  [Kc.ALT, Kc.KEYPAD_PLUS, -Kc.KEYPAD_PLUS, Kc.KEYPAD_ZERO, -Kc.KEYPAD_ZERO, Kc.KEYPAD_THREE, -Kc.KEYPAD_THREE, Kc.A, -Kc.A, Kc.KEYPAD_NINE]), # "Ω" = +03A9 (unicode)
        (0x200020, 'x',       [Kc.ALT, Kc.KEYPAD_ZERO, -Kc.KEYPAD_ZERO, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_ONE, -Kc.KEYPAD_ONE, Kc.KEYPAD_FIVE]), # "×" = alt+0215
        # (0x200020, 'x`',      [Kc.ALT, Kc.KEYPAD_PLUS, -Kc.KEYPAD_PLUS, Kc.KEYPAD_ZERO, -Kc.KEYPAD_ZERO, Kc.KEYPAD_ZERO, -Kc.KEYPAD_ZERO, Kc.D, -Kc.D, Kc.KEYPAD_SEVEN]), # "×" = +00D7 (unicode)
        # 2nd row ----------
        (0x202000, '->',      [Kc.ALT, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_SIX]),   # "→" = alt+26
        (0x202000, '<->',     [Kc.ALT, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_NINE]),  # "↔" = alt+29
        (0x202000, '<-',      [Kc.ALT, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_SEVEN]), # "←" = alt+27
        # 3rd row ----------
        (0x200020, '+-',      [Kc.ALT, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_FOUR, -Kc.KEYPAD_FOUR, Kc.KEYPAD_ONE]), # "±" = alt+241 (= alt+0177)
        (0x200000, 'Minus`',  [Kc.ALT, Kc.KEYPAD_PLUS, -Kc.KEYPAD_PLUS, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_ONE, -Kc.KEYPAD_ONE, Kc.KEYPAD_TWO]), # "−" = +2212 (unicode)
        (0x200020, 'cdot',    [Kc.ALT, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_FIVE, -Kc.KEYPAD_FIVE, Kc.KEYPAD_ZERO]), # "·" = alt+250 (= alt+0183 = alt+8729)
        # (0x200020, 'cdot`',   [Kc.ALT, Kc.KEYPAD_PLUS, -Kc.KEYPAD_PLUS, Kc.KEYPAD_ZERO, -Kc.KEYPAD_ZERO, Kc.KEYPAD_ZERO, -Kc.KEYPAD_ZERO, Kc.B, -Kc.B, Kc.KEYPAD_SEVEN]), # "·" = +00B7 (unicode)
        # 4th row ----------
        (0x200000, '<=',      [Kc.ALT, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_FOUR, -Kc.KEYPAD_FOUR, Kc.KEYPAD_THREE]), # "≤" = alt+243
        # (0x200000, '<=`',     [Kc.ALT, Kc.KEYPAD_PLUS, -Kc.KEYPAD_PLUS, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_SIX, -Kc.KEYPAD_SIX, Kc.KEYPAD_FOUR]), # "≤" = +2264 (unicode)
        (0x200000, '~~',      [Kc.ALT, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_FOUR, -Kc.KEYPAD_FOUR, Kc.KEYPAD_SEVEN]), # "≈" = alt+247
        # (0x200000, '~~`',     [Kc.ALT, Kc.KEYPAD_PLUS, -Kc.KEYPAD_PLUS, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_FOUR, -Kc.KEYPAD_FOUR, Kc.KEYPAD_EIGHT]), # "≈" = +2248 (unicode)
        (0x200000, '>=',      [Kc.ALT, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_FOUR, -Kc.KEYPAD_FOUR, Kc.KEYPAD_TWO]), # "≥" = alt+242
        # (0x200000, '>=`',     [Kc.ALT, Kc.KEYPAD_PLUS, -Kc.KEYPAD_PLUS, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_TWO, -Kc.KEYPAD_TWO, Kc.KEYPAD_SIX, -Kc.KEYPAD_SIX, Kc.KEYPAD_FIVE]), # "≥" = +2265 (unicode)
        # Encoder button ---
        (0x000000, '',        [])
    ]
}
