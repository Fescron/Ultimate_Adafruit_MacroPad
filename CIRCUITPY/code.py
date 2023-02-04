"""
[04/02/2023 BRECHTVE]

A macro/hotkey program for the Adafruit MACROPAD, modified from the original Adafruit example
(see also https://learn.adafruit.com/macropad-hotkeys?view=all).

Macro setups are stored in the "/macros" folder, configurable below ("MACRO_FOLDER").
Plug the MACROPAD into the computer's USB port, use the extra NeoKey buttons
to select an application macro set (also configurable below, "neokey_buttons"),
and press the main MACROPAD keys to send key sequences and other USB protocols.
Use the dial to scroll through additional NeoKey layers.

The used keyboard-layout can also be configured ("KEYBOARD_LAYOUT")
(see also https://github.com/Neradoc/Circuitpython_Keyboard_Layouts).

The OLED-display and button LEDs will dim after a specified amount of time
("TIMEOUT_S"). When dimmed and pressed, the keys still send the same key-sequences
when they are not dimmed. Any press will wake up the MACROPAD lights again
(see also https://github.com/M-Eldin/Adafruit-MacroPad-RP2040-Sleep).
"""

# pylint: disable=import-error, unused-import, too-few-public-methods


# TODO Make sure to not light-up the Neokey1x4 LED's if the board can't get a USB-connection, ...


# 04/02/2023 BRECHTVE: Added line to select the used keyboard-layout
#  - 0 = US QWERTY
#  - 1 = Belgian AZERTY
#  - 2 = Modified Belgian AZERTY (numbers and characters on number-row swapped)
KEYBOARD_LAYOUT = 2


import os
import time
import displayio
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad

# 01/05/2022 BRECHTVE: Added lines below for the added (custom) keyboard layout support using "adafruit_macropad" v2.1.0 and later
if (KEYBOARD_LAYOUT == 2):
    from keyboard_layout_win_be_custom import KeyboardLayout as CustomKeyboardLayout
    from keyboard_layout_win_be import KeyboardLayout as KeyboardLayout
    from keycode_win_be import Keycode
elif (KEYBOARD_LAYOUT == 1):
    from keyboard_layout_win_be import KeyboardLayout
    from keycode_win_be import Keycode
elif (KEYBOARD_LAYOUT == 0):
    from adafruit_hid.keyboard_layout_us import KeyboardLayout
    from adafruit_hid.keycode import Keycode

# 27/04/2022 BRECHTVE: Added lines below to add Neokey1x4 functionality
import board
from adafruit_neokey.neokey1x4 import NeoKey1x4

# 28/09/2022 BRECHTVE: Added lines below to add timeout functionality
from autoscreen import AutoOffScreen
from adafruit_displayio_sh1107_wrapper import SH1107_Wrapper


# CONFIGURABLES ------------------------

MACRO_FOLDER = '/macros'

# 01/05/2022 BRECHTVE: Added lines below to configure which macropad-pages can be accessed using the NeoKey1x4 buttons
neokey_buttons = [
    [ # Layer 0
        # First row
        (0x004000, [0, 1]),   # Alt-codes
        (0x404000, [3, 4]),   # Altium Schematic
        # Second row
        (0x004000, [2, 16]),  # Word & Excel
        (0x400000, [5, 15]),  # Altium Alignment & Colors
        # Third row
        (0x004040, [14, 17]), # CR-8000 Alignment & Board View
        (0x400000, [6, 11]),  # Altium Layout View & Schematic Colors
        # Fourth row
        (0x004040, [12, 13]), # CR-8000
        (0x404000, [7, 8])    # Altium Layout
    ],
    [ # Layer 1
        # First row
        (0x004000, [0, 1]),   # Alt-codes
        (0x000000, [0]),
        # Second row
        (0x400040, [10, 9]),  # Embedded C & MCUXpresso IDE
        (0x000000, [0]),
        # Third row
        (0x000000, [0]),
        (0x000000, [0]),
        # Fourth row
        (0x000000, [0]),
        (0x000000, [0])
    ]
    # Even more layers can be added if necessary
]

# 28/09/2022 BRECHTVE: Added line to add timeout functionality
TIMEOUT_S = 10 * 60 # Time in seconds after which the macropad should go to sleep (turn display and button LED's off, press any button to wake up)


# CLASSES AND FUNCTIONS ----------------

class App:
    """ Class representing a host-side application, for which we have a set
        of macro sequences. Project code was originally more complex and
        this was helpful, but maybe it's excessive now?"""
    def __init__(self, appdata):
        self.name = appdata['name']
        self.macros = appdata['macros']
    
    # 28/09/2022 BRECHTVE: Added lines below to add timeout functionality
    def set_pixels(self):
        for i in range(12):
            if i < len(self.macros): # Key in use, set label + LED color
                macropad.pixels[i] = self.macros[i][0]
            else:  # Key not in use, no label or LED
                macropad.pixels[i] = 0
        macropad.pixels.show()
        updateNeokeyColors() # Turn NeoKey buttons back on

    def switch(self):
        """ Activate application settings; update OLED labels and LED
            colors. """
        group[13].text = self.name   # Application name
        for i in range(12):
            if i < len(self.macros): # Key in use, set label + LED color
                macropad.pixels[i] = self.macros[i][0]
                group[i].text = self.macros[i][1]
            else:  # Key not in use, no label or LED
                macropad.pixels[i] = 0
                group[i].text = ''
        macropad.keyboard.release_all()
        macropad.consumer_control.release()
        macropad.mouse.release_all()
        macropad.stop_tone()
        macropad.pixels.show()
        macropad.display.refresh()

# 01/05/2022 BRECHTVE: Added lines below to add NeoKey1x4 functionality
def updateNeokeyColors():
    # Loop through each button
    for i in range(len(neokey_buttons[0])):
        # Set the configured button-color if it was not pressed
        if ((i % 2) == 0): # Left NeoKey button
            if (neokey_last_button_pressed[neokey_layer_index] != i): neokey_l.pixels[neokey_lut[i]] = neokey_buttons[neokey_layer_index][i][0]
        else: # Right NeoKey button
            if (neokey_last_button_pressed[neokey_layer_index] != i): neokey_r.pixels[neokey_lut[i]] = neokey_buttons[neokey_layer_index][i][0]
    # Make the last-pressed button white
    if ((neokey_last_button_pressed[neokey_layer_index] % 2) == 0): # Left NeoKey button
        neokey_l.pixels[neokey_lut[neokey_last_button_pressed[neokey_layer_index]]] = 0xFFFFFF
    else:
        neokey_r.pixels[neokey_lut[neokey_last_button_pressed[neokey_layer_index]]] = 0xFFFFFF
def handleNeokeyButtonPress(button):
    global neokey_last_button_pressed, neokey_button_pressed_flag # Make sure we address the correct variables
    if (neokey_last_button_pressed[neokey_layer_index] == button): # Change the "sub-page" if the same button was pressed before
        neokey_button_file_index[neokey_layer_index][button] = (neokey_button_file_index[neokey_layer_index][button] + 1) % len(neokey_buttons[neokey_layer_index][button][1])
    else: # If the same button was not pressed before, indicate that this button was pressed
        neokey_last_button_pressed[neokey_layer_index] = button
    neokey_button_pressed_flag = 1
    autoscreen.update_active() # 28/09/2022 BRECHTVE: Added line to add timeout functionality (wakeup/stay woken up)
# 30/09/2022 BRECHTVE: Added lines below to add additional NeyKey1x4 functionality
def disableNeoKeyColors():
    # Turn off Neokey1x4 LED's
    for i in range(4):
        neokey_l.pixels[i] = 0x000000
        neokey_r.pixels[i] = 0x000000

# 28/09/2022 BRECHTVE: Added lines below to add timeout functionality
def lights_on():
    # display_sleeper.wake() # Turn on OLED display
    macropad.display.brightness = 1 # Un-dim OLED display
    macropad.pixels.brightness = 1
    apps[app_index].set_pixels()
def lights_off():
    # display_sleeper.sleep() # Turn off OLED display
    macropad.display.brightness = 0 # Dim OLED display
    macropad.pixels.brightness = 0
    disableNeoKeyColors()
    # Make the last-pressed button (dim) white
    if ((neokey_last_button_pressed[neokey_layer_index] % 2) == 0): # Left NeoKey button
        neokey_l.pixels[neokey_lut[neokey_last_button_pressed[neokey_layer_index]]] = 0x303030
    else:
        neokey_r.pixels[neokey_lut[neokey_last_button_pressed[neokey_layer_index]]] = 0x303030
    macropad.pixels.show()


# INITIALIZATION -----------------------

# 01/05/2022 BRECHTVE: Added lines below to add Neokey1x4 functionality
i2c_bus = board.I2C() # Use default I2C bus
neokey_l = NeoKey1x4(i2c_bus, addr=0x31) # Create a NeoKey object (A0 jumper closed)
neokey_r = NeoKey1x4(i2c_bus, addr=0x30) # Create a NeoKey object

# 30/09/2022 BRECHTVE: Added line below to add additional NeyKey1x4 functionality
disableNeoKeyColors()

# 13/07/2022 BRECHTVE: Added lines below to change to the "regular" AZERTY keyboard-layout upon a startup-button-press
if (KEYBOARD_LAYOUT == 2):
    if neokey_l[0]:
        # Use the "regular" AZERTY keyboard layout
        macropad = MacroPad(
            layout_class=KeyboardLayout,
            keycode_class=Keycode,
        )

        # Display text on the OLED to note the regular layout use
        text_lines = macropad.display_text(title="")
        text_lines[1].text = "     USING REGULAR"
        text_lines[2].text = "     AZERTY LAYOUT"
        text_lines.show()

        # Make all LED's white to note the change
        for i in range(4):
            neokey_l.pixels[i] = 0xFFFFFF
            neokey_r.pixels[i] = 0xFFFFFF
        
        while neokey_l[0]: time.sleep(0.005) # Wait until the button is released (sleep 5ms each time)
        
        # Turn all LED's off to note the change
        for i in range(4):
            neokey_l.pixels[i] = 0x000000
            neokey_r.pixels[i] = 0x000000
    else:
        # macropad = MacroPad() # 01/05/2022 BRECHTVE: Commented line and replaced with lines below to use the added custom keyboard layout-support using "adafruit_macropad" v2.1.0 and later
        macropad = MacroPad(
            layout_class=CustomKeyboardLayout,
            keycode_class=Keycode,
        )
else:
    macropad = MacroPad(
        layout_class=KeyboardLayout,
        keycode_class=Keycode,
    )

# 01/05/2022 BRECHTVE: Added lines below to add Neokey1x4 functionality
neokey_layer_index = 0
neokey_last_button_pressed = [0, 0]
neokey_button_pressed_flag = 0
neokey_button_file_index = [[0, 0, 0, 0, 0, 0, 0, 0]]
neokey_lut = [0, 0, 1, 1, 2, 2, 3, 3] # LUT to translate the button-numbers to left/right NeoKey-numbers
for i in range(len(neokey_buttons)): # Add other Neokey-layer entries if there is more than one layer
    neokey_button_file_index.append([0, 0, 0, 0, 0, 0, 0, 0])

macropad.display.auto_refresh = False
macropad.pixels.auto_write = False

# Set up displayio group with all the labels
group = displayio.Group()
for key_index in range(12):
    x = key_index % 3
    y = key_index // 3
    group.append(label.Label(terminalio.FONT, text='', color=0xFFFFFF,
                             anchored_position=((macropad.display.width - 1) * x / 2,
                                                macropad.display.height - 1 -
                                                (3 - y) * 12),
                             anchor_point=(x / 2, 1.0)))
group.append(Rect(0, 0, macropad.display.width, 12, fill=0xFFFFFF))
group.append(label.Label(terminalio.FONT, text='', color=0x000000,
                         anchored_position=(macropad.display.width//2, -2),
                         anchor_point=(0.5, 0.0)))
macropad.display.show(group)

# Load all the macro key setups from .py files in MACRO_FOLDER
apps = []
files = os.listdir(MACRO_FOLDER)
files.sort()
for filename in files:
    if filename.endswith('.py'):
        try:
            module = __import__(MACRO_FOLDER + '/' + filename[:-3])
            apps.append(App(module.app))
        except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                IndexError, TypeError) as err:
            print("ERROR in", filename)
            import traceback
            traceback.print_exception(err, err, err.__traceback__)

if not apps:
    group[13].text = 'NO MACRO FILES FOUND'
    macropad.display.refresh()
    while True:
        pass

last_position = None
last_encoder_switch = macropad.encoder_switch_debounced.pressed
app_index = 0
apps[app_index].switch()

# 28/09/2022 BRECHTVE: Added lines below to add timeout functionality
autoscreen = AutoOffScreen(TIMEOUT_S) # Set up timeout (duration [s], initial duration [s])
display_sleeper = SH1107_Wrapper(macropad.display) # Use a mangled copy of the SH1107 python driver to add sleep ability to display.
autoscreen.handle_on = lights_on
autoscreen.handle_off = lights_off

# 30/09/2022 BRECHTVE: Added line below to add additional NeyKey1x4 functionality
updateNeokeyColors()


# MAIN LOOP ----------------------------

while True:
    autoscreen.poll() # 28/09/2022 BRECHTVE: Added line to add timeout functionality (refresh timing)

    # 01/05/2022 BRECHTVE: Added lines below to add Neokey1x4 functionality
    if neokey_l[0]:
        while neokey_l[0]: time.sleep(0.005) # Wait until the button is released (sleep 5ms each time)
        handleNeokeyButtonPress(0)
    elif neokey_r[0]:
        while neokey_r[0]: time.sleep(0.005) # Wait until the button is released (sleep 5ms each time)
        handleNeokeyButtonPress(1)
    elif neokey_l[1]:
        while neokey_l[1]: time.sleep(0.005) # Wait until the button is released (sleep 5ms each time)
        handleNeokeyButtonPress(2)
    elif neokey_r[1]:
        while neokey_r[1]: time.sleep(0.005) # Wait until the button is released (sleep 5ms each time)
        handleNeokeyButtonPress(3)
    elif neokey_l[2]:
        while neokey_l[2]: time.sleep(0.005) # Wait until the button is released (sleep 5ms each time)
        handleNeokeyButtonPress(4)
    elif neokey_r[2]:
        while neokey_r[2]: time.sleep(0.005) # Wait until the button is released (sleep 5ms each time)
        handleNeokeyButtonPress(5)
    elif neokey_l[3]:
        while neokey_l[3]: time.sleep(0.005) # Wait until the button is released (sleep 5ms each time)
        handleNeokeyButtonPress(6)
    elif neokey_r[3]:
        while neokey_r[3]: time.sleep(0.005) # Wait until the button is released (sleep 5ms each time)
        handleNeokeyButtonPress(7)
    if neokey_button_pressed_flag == 1:
        updateNeokeyColors()
        app_index = neokey_buttons[neokey_layer_index][neokey_last_button_pressed[neokey_layer_index]][1][neokey_button_file_index[neokey_layer_index][neokey_last_button_pressed[neokey_layer_index]]] # Update the app-index with the new page-number using the configuration-lists
        apps[app_index].switch() # Switch the app-page
        neokey_button_pressed_flag = 0
    
    # Read encoder position. If it's changed, switch apps.
    position = macropad.encoder
    if position != last_position:
        autoscreen.update_active() # 28/09/2022 BRECHTVE: Added line to add timeout functionality (wakeup/stay woken up)

        if (len(neokey_buttons) > 1): # 29/04/2022 BRECHTVE: Added line to make sure we only use the Neokey-layer-switching logic if there is more than one layer
            # app_index = position % len(apps) # 27/04/2022 BRECHTVE: Commented line because rotary encoder will now switch Neokey-layers
            neokey_layer_index = position % len(neokey_buttons) # 01/05/2022 BRECHTVE: Added line to add Neokey layer-switching functionality
            app_index = neokey_buttons[neokey_layer_index][neokey_last_button_pressed[neokey_layer_index]][1][neokey_button_file_index[neokey_layer_index][neokey_last_button_pressed[neokey_layer_index]]] # 01/05/2022 BRECHTVE: Added line to add Neokey layer-switching functionality
            updateNeokeyColors() # 29/04/2022 BRECHTVE: Added line to add Neokey layer-switching functionality
            apps[app_index].switch()

        last_position = position

    # Handle encoder button. If state has changed, and if there's a
    # corresponding macro, set up variables to act on this just like
    # the keypad keys, as if it were a 13th key/macro.
    macropad.encoder_switch_debounced.update()
    encoder_switch = macropad.encoder_switch_debounced.pressed
    if encoder_switch != last_encoder_switch:
        autoscreen.update_active() # 28/09/2022 BRECHTVE: Added line to add timeout functionality (wakeup/stay woken up)

        last_encoder_switch = encoder_switch
        if len(apps[app_index].macros) < 13:
            continue    # No 13th macro, just resume main loop
        key_number = 12 # else process below as 13th macro
        pressed = encoder_switch
    else:
        event = macropad.keys.events.get()

        # 28/09/2022 BRECHTVE: Added lines below to add timeout functionality
        if event:
            autoscreen.update_active()

        if not event or event.key_number >= len(apps[app_index].macros):
            continue # No key events, or no corresponding macro, resume loop
        key_number = event.key_number
        pressed = event.pressed

    # If code reaches here, a key or the encoder button WAS pressed/released
    # and there IS a corresponding macro available for it...other situations
    # are avoided by 'continue' statements above which resume the loop.

    sequence = apps[app_index].macros[key_number][2]
    if pressed:
        # 'sequence' is an arbitrary-length list, each item is one of:
        # Positive integer (e.g. Keycode.KEYPAD_MINUS): key pressed
        # Negative integer: (absolute value) key released
        # Float (e.g. 0.25): delay in seconds
        # String (e.g. "Foo"): corresponding keys pressed & released
        # List []: one or more Consumer Control codes (can also do float delay)
        # Dict {}: mouse buttons/motion (might extend in future)
        if key_number < 12: # No pixel for encoder button
            macropad.pixels[key_number] = 0xFFFFFF
            macropad.pixels.show()
        for item in sequence:
            if isinstance(item, int):
                if item >= 0:
                    macropad.keyboard.press(item)
                else:
                    macropad.keyboard.release(-item)
            elif isinstance(item, float):
                time.sleep(item)
            elif isinstance(item, str):
                macropad.keyboard_layout.write(item)
            elif isinstance(item, list):
                for code in item:
                    if isinstance(code, int):
                        macropad.consumer_control.release()
                        macropad.consumer_control.press(code)
                    if isinstance(code, float):
                        time.sleep(code)
            elif isinstance(item, dict):
                if 'buttons' in item:
                    if item['buttons'] >= 0:
                        macropad.mouse.press(item['buttons'])
                    else:
                        macropad.mouse.release(-item['buttons'])
                macropad.mouse.move(item['x'] if 'x' in item else 0,
                                    item['y'] if 'y' in item else 0,
                                    item['wheel'] if 'wheel' in item else 0)
                if 'tone' in item:
                    if item['tone'] > 0:
                        macropad.stop_tone()
                        macropad.start_tone(item['tone'])
                    else:
                        macropad.stop_tone()
                elif 'play' in item:
                    macropad.play_file(item['play'])
    else:
        # Release any still-pressed keys, consumer codes, mouse buttons
        # Keys and mouse buttons are individually released this way (rather
        # than release_all()) because pad supports multi-key rollover, e.g.
        # could have a meta key or right-mouse held down by one macro and
        # press/release keys/buttons with others. Navigate popups, etc.
        for item in sequence:
            if isinstance(item, int):
                if item >= 0:
                    macropad.keyboard.release(item)
            elif isinstance(item, dict):
                if 'buttons' in item:
                    if item['buttons'] >= 0:
                        macropad.mouse.release(item['buttons'])
                elif 'tone' in item:
                    macropad.stop_tone()
        macropad.consumer_control.release()
        if key_number < 12: # No pixel for encoder button
            macropad.pixels[key_number] = apps[app_index].macros[key_number][0]
            macropad.pixels.show()
