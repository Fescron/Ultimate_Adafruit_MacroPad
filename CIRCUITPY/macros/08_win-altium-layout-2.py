# MACROPAD Hotkeys: Altium PCB-Layout commands for Windows
# BRECHTVE 28/06/2023

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Altium Layout    1/1', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        # (0x200020, '+union`', [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, Kc.ALT, Kc.SHIFT, 'u']),                # Tools > Convert > Create union from selected objects (custom command)
        (0x200020, 'Import',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'd', 0.05, 'i']),            # Design > Import Changes from .PrjPcb
        # (0x200020, '-union`', [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, Kc.ALT, Kc.SHIFT, 'o']),                # Break Objects from union (custom command)
        (0x200020, '+DRC',    [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'd', 0.05, 'r']), # Tools > Design Rule Check > Run Design Rule Check
        (0x200020, '-DRC',    [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'm']),            # Tools > Reset Error Markers
        # 2nd row ----------
        (0x002020, 'RepoSe',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'o', 0.05, 'c']), # Tools > Component Placement > Rearrange Selected Components
        # (0x002020, 'Swap`',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, Kc.ALT, 'w']),                          # Tools > Component Placement > Swap Components (custom command)
        (0x002020, 'Swap',    [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'o', Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.ENTER]), # Tools > Component Placement > (select "Swap Components")
        (0x002020, 'toRect',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'o', 0.05, 'l']), # Tools > Component Placement > Arrange Within Rectangle
        # 3rd row ----------
        (0x202000, 'CompTx',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'e', 0.05, 'g', 0.05, 'p']), # Edit > Align > Position Component Text
        # (0x202000, 'Arc`',    [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, Kc.ALT, Kc.SHIFT, 'b']),                # Place > Arc > Arc (edge) (custom command)
        (0x202000, 'Arc',     [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'a', Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.ENTER]), # Place > Arc > (select "Arc (Edge)")
        (0x000020, 'MultiRt', [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'u', 0.05, 'm']),            # Route > Interactive Multi-Routing
        # (0x202000, 'Rect',    [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'e']),            # Place > Rectangle
        # (0x202000, 'Dimen',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'd', 0.05, 'l']), # Place > Dimensions > Lineair
        # 4th row ----------
        (0x200000, 'Slice',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'e', 0.05, 'k']),            # Edit > Slice Tracks
        (0x200000, 'ReRout',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'e', 0.05, 'm', 0.05, 'r']), # Edit > Move > Re-Route
        # (0x000020, 'DiffRt',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'u', 0.05, 'i']),            # Route > Interactive Differential pair Routing
        (0x200000, 'Drag',    [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'e', 0.05, 'm', 0.05, 'd']), # Edit > Move > Drag
        # (0x000020, 'DiffTu',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'u', 0.05, 'p']),            # Route > Interactive Differential pair Routing Length Tuning
        # (0x000020, 'Repour`', [Kc.CONTROL, Kc.ALT, 'A']),                                                                                                # Tools > Polygon Pours > Repour All (custom command)
        # Encoder button ---
        (0x000000, '',        [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'c'])             # Tools > Cross Probe
    ]
}
