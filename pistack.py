import PySimpleGUI as sg
from telnet import FlightGear
import sys

# PiStack, a remote radio stack for FlightGear
# Copyright (C) 2020 Jeffrey Davis <jeff@puffergas.com>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation; either version 2 of the License,
# or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330,
# Boston, MA 02111-1307 USA

try:
    fg = FlightGear('localhost', 5401)
    # fg = FlightGear('192.168.##.#', 5401)
except ConnectionRefusedError:
    sg.popup_error('Opps', 'Looks like you started PiStack before FlightGear'
    ' or did not configure FlightGear - PiStack will exit.', font=(any, 14))
    sys.exit()

# Value, (double)
fg_com1 = fg['/instrumentation/comm/frequencies/selected-mhz']
fg_stby_com1 = fg['/instrumentation/comm/frequencies/standby-mhz']
fg_com2 = fg['/instrumentation/comm[1]/frequencies/selected-mhz']
fg_stby_com2 = fg['/instrumentation/comm[1]/frequencies/standby-mhz']
fg_nav1 = fg['/instrumentation/nav/frequencies/selected-mhz']
fg_stby_nav1 = fg['/instrumentation/nav/frequencies/standby-mhz']
fg_nav2 = fg['/instrumentation/nav[1]/frequencies/selected-mhz']
fg_stby_nav2 = fg['/instrumentation/nav[1]/frequencies/standby-mhz']
fg_vol_com1 = fg['/instrumentation/comm/volume']
fg_vol_com2 = fg['/instrumentation/comm[1]/volume']
fg_nav1_deg = fg['/instrumentation/nav/radials/selected-deg']
fg_nav2_deg = fg['/instrumentation/nav[1]/radials/selected-deg']

# Boolean 0 or 1
fg_com1_power_btn = fg['/instrumentation/comm/power-btn']
fg_com2_power_btn = fg['/instrumentation/comm[1]/power-btn']
fg_nav1_power_btn = fg['/instrumentation/nav/power-btn']
fg_nav2_power_btn = fg['/instrumentation/nav[1]/power-btn']

sg.theme('DarkBlack1')

frame_layout1 = [
    # -----     COM1     -----
    # Active frequency
    [sg.Input((fg_com1), size=(7,1), key='-use_com1-', readonly=True, border_width=(4),
    font=('any', 16, 'bold'), text_color='red' if bool(fg_com1_power_btn) else 'Gray',
    background_color='white'),
    # Exchange frequncies, button
    sg.Button('<==>', key='-SWITCH_COM1-', font=('any', 14)),
    # Standy frequency
    sg.Input((fg_stby_com1), size=(7, 1), font=('any', 16, 'bold'), text_color='red' if bool(fg_com1_power_btn) else 'Gray',
    border_width=(4), key='-stby_com1-'),
    ],

    # On Off, button 
    [sg.Button('On' if bool(fg_com1_power_btn) else 'Off',
    button_color='white on green' if bool(fg_com1_power_btn) else 'white on red',
    size=(3, 1), key='-COM1_ON_OFF-', font='Any 14',pad=((6,0),(20,4))),
    # Volume
    sg.Slider(range=(0.0, 1.0), resolution=0.1, key='-VOL_COM1-', default_value=fg_vol_com1, pad=((50,10),(20,4)),
    size=(10, 34), orientation='horizontal', disable_number_display=True, enable_events=True, font=('any', 12)),
    sg.Text('Volume', font=('any', 14), pad=((4,4),(20,4))),
    ],
]

frame_layout2 = [
    # -----     NAV1 -----
    # Active frequency
    [sg.Input((fg_nav1), size=(7,1), key='-use_nav1-', readonly=True, border_width=(4), font=('any', 16, 'bold'),
    text_color='red' if bool(fg_nav1_power_btn) else 'Gray', background_color='white'),
    # Exchange frequncy, button
    sg.Button('<==>', key='-SWITCH_NAV1-', font='Any 14'),
    # Standby frequency
    sg.Input((fg_stby_nav1), size=(7, 1),
    font=('any', 16, 'bold'), text_color='red' if bool(fg_nav1_power_btn) else 'Gray', border_width=(4), key='-stby_nav1-'),
    ],
    
    # On Off, button
    [sg.Button('On' if bool(fg_nav1_power_btn) else 'Off',
    button_color='white on green' if bool(fg_nav1_power_btn) else 'white on red',
    size=(3, 1), key='-NAV1_ON_OFF-', font='Any 14', pad=((6,0),(20,4))),
    # Nav1 degrees
    sg.Input(int(fg_nav1_deg), size=(7,1), key='-nav1_deg-', border_width=(4), font=('any', 16, 'bold'),
    text_color='red' if bool(fg_nav1_power_btn) else 'Gray', background_color='white', pad=((20,0),(20,4))),
    sg.Text('Deg', font=('any', 14), pad=((4,4),(20,4))),
    ],
]

frame_layout3 = [
    # ----- COM2 -----
    # Active frequncy
    [sg.Input((fg_com2), size=(7,1), key='-use_com2-', readonly=True, border_width=(4), font=('any', 16, 'bold'),
    text_color='red' if bool(fg_com2_power_btn) else 'Gray', background_color='white'),
    # Exchange frequency, button
    sg.Button('<==>', key='-SWITCH_COM2-', font='Any 14'),
    # Standby frequency
    sg.Input((fg_stby_com2), size=(7, 1),
    font=('any', 16, 'bold'), text_color='red' if bool(fg_com2_power_btn) else 'Gray', border_width=(4), key='-stby_com2-'),
    ],

    # On Off, button
    [sg.Button('On' if bool(fg_com2_power_btn) else 'Off',
    button_color='white on green' if bool(fg_com2_power_btn) else 'white on red',
    size=(3, 1), key='-COM2_ON_OFF-', font='Any 14', pad=((6,0),(20,4))),
    # Volume
    sg.Slider(range=(0.0, 1.0), resolution=0.1, key='-VOL_COM2-', default_value=fg_vol_com2, pad=((50,10),(20,4)),
    size=(10, 34), orientation='horizontal', disable_number_display=True, enable_events=True, font=('any', 12)),
    sg.Text('Volume', font=('any', 14), pad=((4,4),(20,4))),
    ],
]

frame_layout4 = [
    # ----- NAV2 -----
    # Active frequency
    [sg.Input((fg_nav2), size=(7,1), key='-use_nav2-', readonly=True, border_width=(4), font=('any', 16, 'bold'),
    text_color='red' if bool(fg_nav2_power_btn) else 'Gray', background_color='white'),
    # Exchange frequency, button
    sg.Button('<==>', key='-SWITCH_NAV2-', font='Any 14'),
    # Standby frequency
    sg.Input((fg_stby_nav2), size=(7, 1),
    font=('any', 16, 'bold'), text_color='red' if bool(fg_nav2_power_btn) else 'Gray', border_width=(4), key='-stby_nav2-'),
    ],

    # On Off, button
    [sg.Button('On' if bool(fg_nav2_power_btn) else 'Off',
    button_color='white on green' if bool(fg_nav2_power_btn) else 'white on red',
    size=(3, 1), key='-NAV2_ON_OFF-', font='Any 14', pad=((6,0),(20,4))),
    # Nav2 degrees
    sg.Input(int(fg_nav2_deg), size=(7,1), key='-nav2_deg-', border_width=(4), font=('any', 16, 'bold'),
    text_color='red' if bool(fg_nav2_power_btn) else 'Gray', background_color='white', pad=((20,0),(20,4))),
    sg.Text('Deg', font=('any', 14), pad=((4,4),(20,4))),
    ],
]

layout1 = [
    [sg.Frame('Com1', frame_layout1, border_width=(10), font='Any 14', title_color='white'),
    sg.Frame('Nav1', frame_layout2, border_width=(10), font='Any 14', title_color='white')],
    [sg.Frame('Com2', frame_layout3, border_width=(10), font='Any 14', title_color='white'),
    sg.Frame('Nav2', frame_layout4, border_width=(10), font='Any 14', title_color='white')],
    # Options
    [sg.Button('Keypad', key='-KEYPAD-', font='Any 14'), sg.Button('Exit', font='Any 14')]
]


window1 = sg.Window('PiStack', layout1, location=(0, 0), size=(800, 480))
window2_active = False

while True: 
    event1, values1 = window1.read(1000)
    # Un-comment the below to print values to the Python Terminal
    # print(event, values)
    

    if event1 in  (None, 'Exit'):
        window1.close()
        break

    if event1 == '-COM1_ON_OFF-':
        fg_com1_power_btn = not bool(fg_com1_power_btn)
        window1['-COM1_ON_OFF-'].update(text='On' if fg_com1_power_btn else 'Off',
        button_color='white on green' if fg_com1_power_btn else 'white on red')
        fg['/instrumentation/comm/power-btn'] = int(fg_com1_power_btn)
        window1['-use_com1-'].update(text_color='red' if fg_com1_power_btn else 'Gray')
        window1['-stby_com1-'].update(text_color='red' if fg_com1_power_btn else 'Gray')

    if event1 == '-NAV1_ON_OFF-':
        fg_nav1_power_btn = not bool(fg_nav1_power_btn)
        window1['-NAV1_ON_OFF-'].update(text='On' if fg_nav1_power_btn else 'Off',
        button_color='white on green' if fg_nav1_power_btn else 'white on red')
        fg['/instrumentation/nav/power-btn'] = int(fg_nav1_power_btn)
        window1['-use_nav1-'].update(text_color='red' if fg_nav1_power_btn else 'Gray')
        window1['-stby_nav1-'].update(text_color='red' if fg_nav1_power_btn else 'Gray')

    if event1 == '-COM2_ON_OFF-':
        fg_com2_power_btn = not bool(fg_com2_power_btn)
        window1['-COM2_ON_OFF-'].update(text='On' if fg_com2_power_btn else 'Off',
        button_color='white on green' if fg_com2_power_btn else 'white on red')
        fg['/instrumentation/comm[1]/power-btn'] = int(fg_com2_power_btn)
        window1['-use_com2-'].update(text_color='red' if fg_com2_power_btn else 'Gray')
        window1['-stby_com2-'].update(text_color='red' if fg_com2_power_btn else 'Gray')

    if event1 == '-NAV2_ON_OFF-':
        fg_nav2_power_btn = not bool(fg_nav2_power_btn)
        window1['-NAV2_ON_OFF-'].update(text='On' if fg_nav2_power_btn else 'Off',
        button_color='white on green' if fg_nav2_power_btn else 'white on red')
        fg['/instrumentation/nav[1]/power-btn'] = int(fg_nav2_power_btn)
        window1['-use_nav2-'].update(text_color='red' if fg_nav2_power_btn else 'Gray')
        window1['-stby_nav2-'].update(text_color='red' if fg_nav2_power_btn else 'Gray')

    if event1 == '-SWITCH_COM1-': 
        # Swap COM1 frequency
        window1['-use_com1-'].update(values1['-stby_com1-'])
        window1['-stby_com1-'].update(values1['-use_com1-'])
        fg['/instrumentation/comm/frequencies/selected-mhz'] = values1['-stby_com1-']
        fg['/instrumentation/comm/frequencies/standby-mhz'] = values1['-use_com1-']

    if event1 == '-SWITCH_NAV1-': 
        # Swap NAV1 frequncy
        window1['-use_nav1-'].update(values1['-stby_nav1-'])
        window1['-stby_nav1-'].update(values1['-use_nav1-'])
        fg['/instrumentation/nav/frequencies/selected-mhz'] = values1['-stby_nav1-']
        fg['/instrumentation/nav/frequencies/standby-mhz'] = values1['-use_nav1-']

    if event1 == '-SWITCH_COM2-': 
        # Swap COM2 frequncy
        window1['-use_com2-'].update(values1['-stby_com2-'])
        window1['-stby_com2-'].update(values1['-use_com2-'])
        fg['/instrumentation/comm[1]/frequencies/selected-mhz'] = values1['-stby_com2-']
        fg['/instrumentation/comm[1]/frequencies/standby-mhz'] = values1['-use_com2-']

    if event1 == '-SWITCH_NAV2-': 
        # Swap NAV2 frequncy
        window1['-use_nav2-'].update(values1['-stby_nav2-'])
        window1['-stby_nav2-'].update(values1['-use_nav2-'])
        fg['/instrumentation/nav[1]/frequencies/selected-mhz'] = values1['-stby_nav2-']
        fg['/instrumentation/nav[1]/frequencies/standby-mhz'] = values1['-use_nav2-']

    if event1 == '-VOL_COM1-':
        # Adjust volume of COM1, slider
        fg['/instrumentation/comm/volume'] = values1['-VOL_COM1-']

    if event1 == '-VOL_COM2-':
        # Adjust volume of COM2, slider
        fg['/instrumentation/comm[1]/volume'] = values1['-VOL_COM2-']

    if event1 == '-KEYPAD-' and not window2_active:
        window2_active = True
        window1.Hide()
        layout2 = [
            # Lable
            [sg.Text('FREQUENCY')],
            
            # Frequncy to send to FlightGear
            [sg.Input(('1'), size=(7, 1), justification='right', border_width=(4), font=('Helvetica', 28), pad=((6,20),(0,0)),
            text_color='red', key='input'), sg.Button('Clear'),
            ],
            
            # Digit
            [sg.Button(('1'), border_width=(8)), sg.Button(('2'), border_width=(8)), sg.Button(('3'), border_width=(8)),
            # Radio type
            sg.Radio('COM1', 'stack', key='-COM1-', default=True, font='Any 18', size=(8, 1)),
            sg.Radio('NAV1', 'stack', key='-NAV1-', font='Any 18', size=(8, 1)),
            ],
            
            # Digit
            [sg.Button(('4'), border_width=(8)), sg.Button(('5'), border_width=(8)), sg.Button(('6'), border_width=(8)),
            # Radio type
            sg.Radio('COM2', 'stack', key='-COM2-', font='Any 18', size=(8, 1)),
            sg.Radio('NAV2', 'stack', key='-NAV2-', font='Any 18', size=(8, 1)),
            ],
            
            # Digit
            [sg.Button(('7'), border_width=(8)), sg.Button(('8'), border_width=(8)), sg.Button(('9'), border_width=(8)),
            # Radio type
            sg.Radio('NAV1 deg', 'stack', key='-NAV1_deg-', font='Any 18', size=(8, 1), enable_events=True),
            sg.Radio('NAV2 deg', 'stack', key='-NAV2_deg-', font='Any 18', size=(8, 1), enable_events=True),
            ],
            
            # Digits, Cancel and Enter
            [sg.Button(('Enter'), border_width=(8)), sg.Button(('0'), border_width=(8)),
            sg.Button(('.'), border_width=(8)), sg.Cancel()],
            ]

        # Make Keypad window visiable
        window2 = sg.Window('Keypad', layout2, default_button_element_size=(6,2), font=('Helvetica', 16), auto_size_buttons=False)

        keys_entered = ''

        while True:
            event2, values2 = window2.read(1000)

            if event2 in (sg.WIN_CLOSED, 'Quit', 'Cancel'):
                window2.close()
                window2_active = False
                window1.UnHide()
                break
            
            if event2 == 'Clear':
                keys_entered = ''
                window2['input'].update(keys_entered)

            if event2 in '1234567890.':
                keys_entered = values2['input']
                keys_entered += event2
                window2['input'].update(keys_entered)

            if event2 =='-NAV1_deg-':
                keys_entered = ''
                window2['input'].update(keys_entered)

            if event2 =='-NAV2_deg-':
                keys_entered = ''
                window2['input'].update(keys_entered)



            if event2 == 'Enter':

                if values2['-COM1-'] == True:
                    window1['-stby_com1-'].update(keys_entered)
                    fg['/instrumentation/comm/frequencies/standby-mhz'] = keys_entered

                elif values2['-NAV1-'] == True:
                    window1['-stby_nav1-'].update(keys_entered)
                    fg['/instrumentation/nav/frequencies/standby-mhz'] = keys_entered

                elif values2['-COM2-'] == True:
                    window1['-stby_com2-'].update(keys_entered)
                    fg['/instrumentation/comm[1]/frequencies/standby-mhz'] = keys_entered

                elif values2['-NAV2-'] == True:
                    window1['-stby_nav2-'].update(keys_entered)
                    fg['/instrumentation/nav[1]/frequencies/standby-mhz'] = keys_entered

                elif values2['-NAV1_deg-'] == True:
                    window1['-nav1_deg-'].update(keys_entered)
                    fg['/instrumentation/nav/radials/selected-deg'] = keys_entered

                elif values2['-NAV2_deg-'] == True:
                    window1['-nav2_deg-'].update(keys_entered)
                    fg['/instrumentation/nav[1]/radials/selected-deg'] = keys_entered


                window2.close()
                window2_active = False
                window1.UnHide()
#                print(freq)
                break
