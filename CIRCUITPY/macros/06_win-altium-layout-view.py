# MACROPAD Hotkeys: Altium PCB-Layout commands for Windows
# BRECHTVE 28/06/2023

from adafruit_macropad import keycodes as Kc # REQUIRED if using Kc.* values

app = {                              # REQUIRED dict, must be named 'app'
    'name' : 'Altium PCB View  1/1', # Application name (<20 chars)
    'macros' : [                     # List of button macros...
        # COLOR    LABEL (<7 chars)    KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'AllLay',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'd', 0.05, 't', 0.05, 'a']), # Design > Manage Layer Sets > All Layers
        (0x000020, 'WrkLay',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'd', 0.05, 't', 0.05, 'w']), # Design > Manage Layer Sets > Working Layers
        (0x200020, 'ClnNet',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'd', 0.05, 'n', 0.05, 'a']), # Design > Netlist > Clean All Nets
        # 2nd row ----------
        (0x202000, 'Hguide',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'w', 0.05, 'h']), # Place > Work Guides > Place Horizontal Guide
        (0x202000, 'Vguide',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'w', 0.05, 'v']), # Place > Work Guides > Place Vertical Guide
        (0x202000, 'Pguide',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'p', 0.05, 'w', 0.05, 'p']), # Place > Work Guides > Place Point Guide
        # 3rd row ----------
        (0x002000, '1 All',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'v', 0.05, 'c', 0.05, 's']), # View > Connections > Show All
        (0x002000, '1 Comp',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'v', 0.05, 'c', 0.05, 'c']), # View > Connections > Show Component Nets
        (0x002000, '1 Net',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'v', 0.05, 'c', 0.05, 'n']), # View > Connections > Show Net
        # 4th row ----------
        (0x200000, '0 All',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'v', 0.05, 'c', 0.05, 'h']), # View > Connections > Hide All
        # (0x200000, '0 Comp`', [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, Kc.ALT, Kc.SHIFT, 'c']),                # View > Connections > Hide Component Nets (custom command)
        (0x200000, '0 Comp',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'v', 0.05, 'c', Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.ENTER]), # View > Connections > (select "Hide Component Nets")
        # (0x200000, '0 Net`',  [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.CONTROL, Kc.ALT, Kc.SHIFT, 'n']),                # View > Connections > Hide Net (custom command)
        (0x200000, '0 Net',   [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 'v', 0.05, 'c', Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.DOWN_ARROW, -Kc.DOWN_ARROW, Kc.ENTER]), # View > Connections > (select "Hide Net")
        # Encoder button ---
        (0x000000, '',        [Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ESCAPE, 0.05, -Kc.ESCAPE, 0.05, Kc.ALT, 0.05, -Kc.ALT, 't', 0.05, 'c'])             # Tools > Cross Probe
    ]
}
