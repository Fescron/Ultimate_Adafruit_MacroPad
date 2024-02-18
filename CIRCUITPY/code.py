"""
[08/02/2024 BRECHTVE]

A macro/hotkey program for the Adafruit MACROPAD, modified from the original Adafruit example
(see also https://learn.adafruit.com/macropad-hotkeys?view=all).

Macro setups are stored in the "/macros" folder, configurable below ("MACRO_FOLDER").
Plug the MACROPAD into the computer's USB port, use the extra NeoKey buttons
to select an application macro set (also configurable below, "NEOKEY_BUTTONS"),
and press the main MACROPAD keys to send key sequences and other USB protocols.
Use the dial to scroll through additional NeoKey layers.

The used keyboard-layout can also be configured ("KEYBOARD_LAYOUT")
(see also https://github.com/Neradoc/Circuitpython_Keyboard_Layouts).

The OLED displays and button LEDs will dim after a specified amount of time
("TIMEOUT_S"). When dimmed and pressed, the keys still send the same key-sequences
when they are not dimmed. Any press will wake up the MACROPAD lights again
(see also https://github.com/M-Eldin/Adafruit-MacroPad-RP2040-Sleep).

Connected I2C devices:
- NeoKey 1x4 (left,  0x31 = A0 jumper closed)
- NeoKey 1x4 (right, 0x30)
- 1.3" 128x64 OLED display (0x3d)

Make sure to have flashed CircuitPython firmware (.uf2) which supports two displays!
"""

# pylint: disable=import-error, unused-import, too-few-public-methods


# TODO Make sure to not light-up the Neokey1x4 LED's if the board can't get a USB-connection, ...


# 04/02/2023 BRECHTVE: Added line to select the used keyboard-layout
#  - 0 = US QWERTY
#  - 1 = Belgian AZERTY (switch to the modified layout by holding the lower-left neokey-button down on boot)
#  - 2 = Modified Belgian AZERTY (numbers and characters on number-row swapped) (switch to the regular layout by holding the lower-left neokey-button down on boot)
KEYBOARD_LAYOUT = 1


import os
import time
import displayio
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad

# 01/05/2022 BRECHTVE: Added lines below for the added (custom) keyboard layout support using "adafruit_macropad" v2.1.0 and later
if ((KEYBOARD_LAYOUT == 2) or (KEYBOARD_LAYOUT == 1)):
    from keyboard_layout_win_be_custom import KeyboardLayout as CustomKeyboardLayout
    from keyboard_layout_win_be import KeyboardLayout as KeyboardLayout
    from keycode_win_be import Keycode
elif (KEYBOARD_LAYOUT == 0):
    from adafruit_hid.keyboard_layout_us import KeyboardLayout
    from adafruit_hid.keycode import Keycode

# 27/04/2022 BRECHTVE: Added lines below to add Neokey1x4 functionality
import board
# import busio
from adafruit_neokey.neokey1x4 import NeoKey1x4

# 28/09/2022 BRECHTVE: Added lines below to add timeout functionality
from autoscreen import AutoOffScreen

# 09/12/2023 BRECHTVE: Added lines below to add functionality to work with an extra OLED display
import adafruit_displayio_ssd1306
import adafruit_displayio_sh1106


# CONFIGURABLES ------------------------

MACRO_FOLDER = '/macros'

# 01/05/2022 BRECHTVE: Added lines below to configure which macropad-pages can be accessed using the NeoKey1x4 buttons
NEOKEY_BUTTONS_START_LAYER  = 0
NEOKEY_BUTTONS_START_BUTTON = 6

NEOKEY_BUTTONS = [
    [
        # Layer title
        "Base [1/3] AltiumSch",
        # Button definitions
        [
            # First row
            (0x004000, "AltCode1,2", [0, 1]),   # Alt-codes 1 & 2
            (0x404000, "Base,Queri", [3, 24]),  # Altium Schematic 1 & Validation Queries
            # Second row
            (0x000040, "Word1,4",    [2, 16]),  # Word 1 & 4
            (0x404000, "Hierarch",   [4]),      # Altium Schematic 2
            # Third row
            (0x000040, "Word2,3",    [20, 23]), # Word 2 & 3
            (0x404000, "Varia,Algn", [5, 22]),  # Altium Schematic 3 & Alignment
            # Fourth row
            (0x004040, "Outl,Excl",  [18, 26]), # Outlook & Excel
            (0x404000, "Col,NetCol", [15, 11])  # Altium Colors & Net-colors
        ]
    ],
    [
        # Layer title
        "Base [2/3] AltiumLay",
        # Button definitions
        [
            # First row
            (0x004000, "AltCode1,2", [0, 1]),   # Alt-codes 1 & 2
            (0x400000, "Base,Queri", [7, 25]),  # Altium Layout 1 & Validation Queries
            # Second row
            (0x000040, "Word1,4",    [2, 16]),  # Word 1 & 4
            (0x400000, "Varia",      [8]),      # Altium Layout 2
            # Third row
            (0x000040, "Word2,3",    [20, 23]), # Word 2 & 3
            (0x000000, "",           [0]),
            # Fourth row
            (0x004040, "Outl,Excl",  [18, 26]), # Outlook & Excel
            (0x400000, "View",       [6])       # Altium Layout View
        ]
    ],
    [
        # Layer title
        "Base [3/3] Code/Zukn",
        # Button definitions
        [
            # First row
            (0x004000, "AltCode1,2", [0, 1]),   # Alt-codes 1 & 2
            (0x400040, "VSdbg,MCUX", [21, 9]),  # VScode debug & MCUXpresso IDE
            # Second row
            (0x000040, "Word1,4",    [2, 16]),  # Word 1 & 4
            (0x400040, "Clip,EmbC",  [19, 10]), # "Clipboard" & Embedded C 
            # Third row
            (0x000040, "Word2,3",    [20, 23]), # Word 2 & 3
            (0x404000, "Algn,BrdVw", [14, 17]), # CR-8000 Alignment & Board View
            # Fourth row
            (0x004040, "Outl,Excl",  [18, 26]), # Outlook & Excel
            (0x404000, "Base,Varia", [12, 13])  # CR-8000 1 & 2
        ]
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
        global neokey_led_update_flag
        for i in range(12):
            if i < len(self.macros): # Key in use, set label + LED color
                macropad.pixels[i] = self.macros[i][0]
            else:  # Key not in use, no label or LED
                macropad.pixels[i] = 0
        macropad.pixels.show()
        neokey_led_update_flag = True
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
    global neokey_led_update_flag
    if neokey_led_update_flag:
        # Loop through each button
        for i in range(len(NEOKEY_BUTTONS[0][1])): # TODO Only update colors which necessitate an update?
            # Set the configured button-color if it was not pressed
            if ((i % 2) == 0): # Left NeoKey button
                if neokey_last_button_pressed[neokey_layer_index] != i:
                    neokey_l.pixels[neokey_lut[i]] = NEOKEY_BUTTONS[neokey_layer_index][1][i][0]
            else: # Right NeoKey button
                if neokey_last_button_pressed[neokey_layer_index] != i:
                    neokey_r.pixels[neokey_lut[i]] = NEOKEY_BUTTONS[neokey_layer_index][1][i][0]
        # Make the last-pressed button white
        if ((neokey_last_button_pressed[neokey_layer_index] % 2) == 0): # Left NeoKey button
            neokey_l.pixels[neokey_lut[neokey_last_button_pressed[neokey_layer_index]]] = 0xFFFFFF
        else:
            neokey_r.pixels[neokey_lut[neokey_last_button_pressed[neokey_layer_index]]] = 0xFFFFFF
        neokey_l.pixels.show()
        neokey_r.pixels.show()
        neokey_led_update_flag = False
def handleNeokeyButtonPress(button):
    global neokey_last_button_pressed, neokey_button_pressed_flag, neokey_led_update_flag # Make sure we address the correct variables
    if (neokey_last_button_pressed[neokey_layer_index] == button): # Change the "sub-page" if the same button was pressed before
        neokey_button_file_index[neokey_layer_index][button] = (neokey_button_file_index[neokey_layer_index][button] + 1) % len(NEOKEY_BUTTONS[neokey_layer_index][1][button][2])
    else: # If the same button was not pressed before, indicate that this button was pressed
        neokey_last_button_pressed[neokey_layer_index] = button
        neokey_led_update_flag = True
    neokey_button_pressed_flag = True
    autoscreen.update_active() # 28/09/2022 BRECHTVE: Added line to add timeout functionality (wakeup/stay woken up)
# 30/09/2022 BRECHTVE: Added lines below to add additional NeyKey1x4 functionality
def setAllNeoKeyColors(color):
    # Turn off Neokey1x4 LED's
    for i in range(4):
        neokey_l.pixels[i] = color
        neokey_r.pixels[i] = color
    neokey_l.pixels.show()
    neokey_r.pixels.show()

# 28/09/2022 BRECHTVE: Added lines below to add timeout functionality
def lights_on():
    macropad.display.brightness = 0.45 # Un-dim OLED display
    macropad.pixels.brightness = 1
    apps[app_index].set_pixels()
    extra_display.brightness = 1 # Un-dim extra OLED display (08/12/2023)
def lights_off():
    macropad.display.brightness = 0 # Dim OLED display
    macropad.pixels.brightness = 0
    setAllNeoKeyColors(0x000000)
    # Make the last-pressed button (dim) white
    if ((neokey_last_button_pressed[neokey_layer_index] % 2) == 0): # Left NeoKey button
        neokey_l.pixels[neokey_lut[neokey_last_button_pressed[neokey_layer_index]]] = 0x303030
        neokey_l.pixels.show()
    else:
        neokey_r.pixels[neokey_lut[neokey_last_button_pressed[neokey_layer_index]]] = 0x303030
        neokey_r.pixels.show()
    macropad.pixels.show()
    extra_display.brightness = 0 # Dim extra OLED display (08/12/2023)

# 07/12/2023 BRECHTVE: Added lines below to update the text on the extra OLED display
def updateExtraDisplay():
    refreshDisplay = False
    if extra_group[9].text != NEOKEY_BUTTONS[neokey_layer_index][0]:
        extra_group[9].text = NEOKEY_BUTTONS[neokey_layer_index][0]
        refreshDisplay = True
    for i in range(8):
        if extra_group[i].text != NEOKEY_BUTTONS[neokey_layer_index][1][i][1]:
            extra_group[i].text = NEOKEY_BUTTONS[neokey_layer_index][1][i][1]
            refreshDisplay = True
        if (i != neokey_last_button_pressed[neokey_layer_index]) and (extra_group[i].color != 0xFFFFFF):
            extra_group[i].color = 0xFFFFFF
            extra_group[i].background_color=0x000000
            refreshDisplay = True
        if i == neokey_last_button_pressed[neokey_layer_index]:
            if extra_group[i].color != 0x000000:
                extra_group[i].color = 0x000000
                extra_group[i].background_color=0xFFFFFF
                refreshDisplay = True
    if refreshDisplay:
        extra_display.refresh()

# 09/12/2023 BRECHTVE: Added lines below to add functionality to work with an extra OLED display
def setupMainDisplay():
    displayio.release_displays() 
    display_bus = displayio.FourWire(
        board.SPI(),
        command=board.OLED_DC,
        chip_select=board.OLED_CS,
        reset=board.OLED_RESET,
        baudrate=1000000,
        polarity=0, phase=0
    )
    display = adafruit_displayio_sh1106.SH1106(display_bus, width=128, height=64, colstart=2)
    macropad.display = display


# INITIALIZATION -----------------------

# 01/05/2022 BRECHTVE: Added lines below to add Neokey1x4 functionality
i2c_bus = board.I2C() # Use default I2C bus
# i2c_bus = busio.I2C(scl=board.SCL, sda=board.SDA, frequency=400000) # 09/12/2023 BRECHTVE: Increased bus-frequency BUT this gives errors when using autoreload (and doesn't seem to increase the speed much anyway?)
neokey_l = NeoKey1x4(i2c_bus, addr=0x31) # Create a NeoKey object (A0 jumper closed)
neokey_r = NeoKey1x4(i2c_bus, addr=0x30) # Create a NeoKey object
neokey_l.pixels.auto_write = False
neokey_r.pixels.auto_write = False

# 30/09/2022 BRECHTVE: Added line below to add additional NeyKey1x4 functionality
# setAllNeoKeyColors(0x000000)

# 13/07/2022 BRECHTVE: Added lines below to change to the "regular" (or modified, depending on definition at the top of the file) AZERTY keyboard-layout upon a startup-button-press
if (KEYBOARD_LAYOUT == 1):
    if neokey_l[3]:
        # Use the custom AZERTY keyboard layout
        macropad = MacroPad(
            layout_class=CustomKeyboardLayout,
            keycode_class=Keycode,
        )
        setupMainDisplay() # 09/12/2023 BRECHTVE: Added line to add functionality to work with an extra OLED display

        # Display text on the OLED to note the regular layout use
        text_lines = macropad.display_text(title="")
        text_lines[1].text = "     USING CUSTOM"
        text_lines[2].text = "     AZERTY LAYOUT"
        text_lines.show()

        # Make all LED's white to note the change
        setAllNeoKeyColors(0xFFFFFF)

        while neokey_l[3]: time.sleep(0.005) # Wait until the button is released (sleep 5ms each time)

        # Turn all LED's off to note the change
        setAllNeoKeyColors(0x000000)
    else:
        # macropad = MacroPad() # 01/05/2022 BRECHTVE: Commented line and replaced with lines below to use the added custom keyboard layout-support using "adafruit_macropad" v2.1.0 and later
        macropad = MacroPad(
            layout_class=KeyboardLayout,
            keycode_class=Keycode,
        )
        setupMainDisplay() # 09/12/2023 BRECHTVE: Added line to add functionality to work with an extra OLED display
elif (KEYBOARD_LAYOUT == 2):
    if neokey_l[3]:
        # Use the "regular" AZERTY keyboard layout
        macropad = MacroPad(
            layout_class=KeyboardLayout,
            keycode_class=Keycode,
        )
        setupMainDisplay() # 09/12/2023 BRECHTVE: Added line to add functionality to work with an extra OLED display

        # Display text on the OLED to note the regular layout use
        text_lines = macropad.display_text(title="")
        text_lines[1].text = "     USING REGULAR"
        text_lines[2].text = "     AZERTY LAYOUT"
        text_lines.show()

        # Make all LED's white to note the change
        setAllNeoKeyColors(0xFFFFFF)

        while neokey_l[3]: time.sleep(0.005) # Wait until the button is released (sleep 5ms each time)
        
        # Turn all LED's off to note the change
        setAllNeoKeyColors(0x000000)
    else:
        # macropad = MacroPad() # 01/05/2022 BRECHTVE: Commented line and replaced with lines below to use the added custom keyboard layout-support using "adafruit_macropad" v2.1.0 and later
        macropad = MacroPad(
            layout_class=CustomKeyboardLayout,
            keycode_class=Keycode,
        )
        setupMainDisplay() # 09/12/2023 BRECHTVE: Added line to add functionality to work with an extra OLED display
else:
    macropad = MacroPad(
        layout_class=KeyboardLayout,
        keycode_class=Keycode,
    )
    setupMainDisplay() # 09/12/2023 BRECHTVE: Added line to add functionality to work with an extra OLED display

# 01/05/2022 BRECHTVE: Added lines below to add Neokey1x4 functionality
neokey_layer_index = NEOKEY_BUTTONS_START_LAYER
neokey_last_button_pressed = [0]
neokey_button_pressed_flag = False
neokey_led_update_flag = False
neokey_button_file_index = [[0, 0, 0, 0, 0, 0, 0, 0]]
neokey_lut = [0, 0, 1, 1, 2, 2, 3, 3] # LUT to translate the button-numbers to left/right NeoKey-numbers
for i in range(len(NEOKEY_BUTTONS)): # Add other Neokey-layer entries if there is more than one layer
    neokey_last_button_pressed.append(0)
    neokey_button_file_index.append([0, 0, 0, 0, 0, 0, 0, 0])
neokey_last_button_pressed[neokey_layer_index] = NEOKEY_BUTTONS_START_BUTTON

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
                         anchored_position=(macropad.display.width//2, 0), # 07/12/2023 BRECHTVE: Changed "-2" to "0" to fix the vertical title-offset
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
# apps[app_index].switch() # 09/12/2023 BRECHTVE: Not necessary to call this here, will get refreshed by the encoder logic...

# 28/09/2022 BRECHTVE: Added lines below to add timeout functionality
autoscreen = AutoOffScreen(TIMEOUT_S) # Set up timeout (duration [s], initial duration [s])
autoscreen.poll()
autoscreen.handle_on = lights_on
autoscreen.handle_off = lights_off

# 30/09/2022 BRECHTVE: Added line below to add additional NeyKey1x4 functionality
# updateNeokeyColors() # 09/12/2023 BRECHTVE: Not necessary to call this here, will get refreshed by the encoder logic...

# 07/12/2023 BRECHTVE: Added lines below to add functionality to work with an extra OLED display
macropad.display.brightness = 0.45 # Set the brightness of the OLED display to be about the same of the extra one
extra_display_bus = displayio.I2CDisplay(i2c_bus, device_address=0x3d)
extra_display = adafruit_displayio_ssd1306.SSD1306(extra_display_bus, width=128, height=64)
extra_display.auto_refresh = False
# Set up displayio group with all the labels
extra_group = displayio.Group()
for key_index in range(8):
    x = key_index % 2
    y = key_index // 2
    extra_group.append(label.Label(terminalio.FONT, text='', color=0xFFFFFF,
                             anchored_position=((128 - 1) * x,
                                                64 - 1 -
                                                (3 - y) * 12),
                             anchor_point=(x, 1.0)))
extra_group.append(Rect(0, 0, 128, 12, fill=0xFFFFFF))
extra_group.append(label.Label(terminalio.FONT, text='', color=0x000000,
                         anchored_position=(128//2, 0),
                         anchor_point=(0.5, 0.0)))
extra_display.root_group = extra_group
updateExtraDisplay()


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
    if neokey_button_pressed_flag:
        updateNeokeyColors()
        app_index = NEOKEY_BUTTONS[neokey_layer_index][1][neokey_last_button_pressed[neokey_layer_index]][2][neokey_button_file_index[neokey_layer_index][neokey_last_button_pressed[neokey_layer_index]]] # Update the app-index with the new page-number using the configuration-lists
        apps[app_index].switch() # Switch the app-page
        updateExtraDisplay() # 09/12/2023 BRECHTVE: Added functionality to work with an extra OLED display
        neokey_button_pressed_flag = False

    # Read encoder position. If it's changed, switch apps.
    position = macropad.encoder
    if position != last_position:
        autoscreen.update_active() # 28/09/2022 BRECHTVE: Added line to add timeout functionality (wakeup/stay woken up)

        if (len(NEOKEY_BUTTONS) > 1): # 29/04/2022 BRECHTVE: Added line to make sure we only use the Neokey-layer-switching logic if there is more than one layer
            # app_index = position % len(apps) # 27/04/2022 BRECHTVE: Commented line because rotary encoder will now switch Neokey-layers
            neokey_layer_index = position % len(NEOKEY_BUTTONS) # 01/05/2022 BRECHTVE: Added line to add Neokey layer-switching functionality
            app_index = NEOKEY_BUTTONS[neokey_layer_index][1][neokey_last_button_pressed[neokey_layer_index]][2][neokey_button_file_index[neokey_layer_index][neokey_last_button_pressed[neokey_layer_index]]] # 01/05/2022 BRECHTVE: Added line to add Neokey layer-switching functionality
            neokey_led_update_flag = True
            updateNeokeyColors() # 29/04/2022 BRECHTVE: Added line to add Neokey layer-switching functionality
            apps[app_index].switch()
            updateExtraDisplay() # 07/12/2023 BRECHTVE: Added functionality to work with an extra OLED display

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
