# MACROPAD Hotkeys: Windows Microsoft Office (Word) (Dutch)
# BRECHTVE 08/02/2024

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values
# from adafruit_hid.mouse import Mouse # REQUIRED if using Mouse.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Word Table/Varia 2/2', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x200000, '-Brdr',   [Kc.ALT, 'jt2', 'ba', 'g']), # Tabelontwerp > Randen > Geen rand
        (0x002000, '+Brdr',   [Kc.ALT, 'jt2', 'ba', 'a']), # Tabelontwerp > Randen > Alle randen
        # (0x202020, '#tblBg',  ['E5E5E5']),
        (0x202020, '+tblBg',  [Kc.ALT, 'jt2', 'br', 'm', -Kc.ALT, Kc.RIGHT_ARROW, -Kc.RIGHT_ARROW, Kc.ALT, 'h', -Kc.ALT, 'E5E5E5', Kc.ENTER]), # Tabelontwerp > Arcering > Meer kleuren > (Aangepast) > Hexadecimaal > enter color & (enter)
        # (0x202020, '#tblBg ', ['D3D3D3']), # Same color as light-grey highlight
        # 2nd row ----------
        (0x200000, '*lSt_v',  [Kc.ALT, 'jt2', 'g', Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.ENTER]), # Tabelontwerp > Penstijl
        (0x200000, '*lSt_^',  [Kc.ALT, 'jt2', 'g', Kc.UP_ARROW, -Kc.UP_ARROW, Kc.ENTER]),     # Tabelontwerp > Penstijl
        (0x202020, '-tblBg',  [Kc.ALT, 'jt2', 'br', 'g']), # Tabelontwerp > Arcering > Geen kleur
        # 3rd row ----------
        (0x200000, 'SplTbl',  [Kc.ALT, 'jl', 'tt']),       # Indeling > Tabel splitsen
        (0x202020, '#tblBr',  ['808080']),
        (0x000020, 'fulRow',  [Kc.ALT, 'jl', 'ei', 'r', -Kc.ALT, Kc.TAB, -Kc.TAB, 's', Kc.ENTER]), # Indeling > Eigenschappen > Rij > (go out of tabs) > Rij eventueel splitsen bij nieuwe pagina > (press OK)
        # 4th row ----------
        (0x202020, '*CouNw',  [Kc.ALT, 'r', 'le', 'Courier New', Kc.ENTER]), # Lettertype > "Courier New"
        (0x200020, '%Flds',   [Kc.CONTROL, 'a', Kc.F9]),   # Update all fields
        (0x200000, '*Wtmrk',  [Kc.ALT, 'a', 'w', 'a']),    # Ontwerp > Watermerk > Aangepast watermerk
        # (0x202000, 'Grid',    [Kc.ALT, 'v', 'rr']),        # Beeld > Rasterlijnen
        # (0x202000, 'frac',    [Kc.ALT, 'je', Kc.ALT, 'b', Kc.ENTER]), # Vergelijking > Breuk > (enter)
        # (0x202000, '`C+V Tx', [{'buttons':Mouse.RIGHT_BUTTON}, {'buttons':-Mouse.RIGHT_BUTTON}, 't']), # Rightclick > Only keep text (paste)
        # (0x002020, '`TblCol', [{'buttons':Mouse.RIGHT_BUTTON}, {'buttons':-Mouse.RIGHT_BUTTON}, 'h', 'k', Kc.TAB]), # (Rightclick in cell) > Tabeleigenschappen > Kolom > TAB
        # (0x002020, 'TblCol',  [Kc.ALT, 'jl', 'ei', 'k']), # Indeling > Eigenschappen > Kolom
        # (0x002020, '-Width',  [Kc.ALT, 'u', 'v']), # Voorkeursbreedte > Volgende kolom
        # (0x002020, 'Close',   [Kc.TAB, -Kc.TAB, Kc.ENTER]), # (Press OK)
        # Encoder button ---
        (0x000000, '',        [])
    ]
}
