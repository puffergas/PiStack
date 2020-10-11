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

fg_com1 = fg['/instrumentation/comm/frequencies/selected-mhz']
fg_stby_com1 = fg['/instrumentation/comm/frequencies/standby-mhz']

fg_com2 = fg['/instrumentation/comm[1]/frequencies/selected-mhz']
fg_stby_com2 = fg['/instrumentation/comm[1]/frequencies/standby-mhz']

fg_nav1 = fg['/instrumentation/nav/frequencies/selected-mhz']
fg_stby_nav1 = fg['/instrumentation/nav/frequencies/standby-mhz']

fg_nav2 = fg['/instrumentation/nav[1]/frequencies/selected-mhz']
fg_stby_nav2 = fg['/instrumentation/nav[1]/frequencies/standby-mhz']

sg.theme('DarkBlack1')

frame_layout1 = [
    # COM1
    [sg.Input((fg_com1), size=(7,1), key='-use_com1-', readonly=True, border_width=(4), font='Any 14', text_color='red',
    background_color='white'), sg.Button('<==>', key='-SWITCH_COM1-', font='Any 14'), sg.Input((fg_stby_com1), size=(7, 1),
    font='Any 14', text_color='red', border_width=(4), key='-stby_com1-')],
    ]

frame_layout2 = [
    # NAV1 
    [sg.Input((fg_nav1), size=(7,1), key='-use_nav1-', readonly=True, border_width=(4), font='Any 14', text_color='red',    
    background_color='white'), sg.Button('<==>', key='-SWITCH_NAV1-', font='Any 14'), sg.Input((fg_stby_nav1), size=(7, 1),
    font='Any 14', text_color='red', border_width=(4), key='-stby_nav1-')],
    ]

frame_layout3 = [
    # COM1
    [sg.Input((fg_com2), size=(7,1), key='-use_com2-', readonly=True, border_width=(4), font='Any 14', text_color='red',
    background_color='white'), sg.Button('<==>', key='-SWITCH_COM2-', font='Any 14'), sg.Input((fg_stby_com2), size=(7, 1),
    font='Any 14', text_color='red', border_width=(4), key='-stby_com2-')],
    ]

frame_layout4 = [
    # NAV1 
    [sg.Input((fg_nav2), size=(7,1), key='-use_nav2-', readonly=True, border_width=(4), font='Any 14', text_color='red',    
    background_color='white'), sg.Button('<==>', key='-SWITCH_NAV2-', font='Any 14'), sg.Input((fg_stby_nav2), size=(7, 1),
    font='Any 14', text_color='red', border_width=(4), key='-stby_nav2-')],
    ]

layout1 = [
          [sg.Frame('Com1', frame_layout1, font='Any 14', title_color='white'),
          sg.Frame('Nav1', frame_layout2, font='Any 14', title_color='white')],
          [sg.Frame('Com2', frame_layout3, font='Any 14', title_color='white'),
          sg.Frame('Nav2', frame_layout4, font='Any 14', title_color='white')],
          # Optionsa
          [sg.Button('Keypad', key='-KEYPAD-'), sg.Button('Exit')]
         ]


window1 = sg.Window('PiStack', layout1, location=(100, 100), size=(800, 480))
window2_active = False
  
while True: 
    event1, values1 = window1.read(1000)
    # Un-comment the below to print values to the Python Terminal
    # print(event, values)
    

    if event1 in  (None, 'Exit'):
        window1.close()    # ; del window
        break
    
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
        
    if event1 == '-KEYPAD-' and not window2_active:
        window2_active = True
        window1.Hide()
        layout2 = [
            # Radio type
            [sg.Radio('COM1', 'stack', key='-COM1-', default=True, font='Any 12', size=(6, 1)),
            sg.Radio('COM2', 'stack', key='-COM2-', font='Any 12', size=(6, 1))],

            # Radio type
            [sg.Radio('NAV1', 'stack', key='-NAV1-', font='Any 12', size=(6, 1)),
            sg.Radio('NAV2', 'stack', key='-NAV2-', font='Any 12', size=(6, 1))],

            # Lable
            [sg.Text('FREQUENCY')],
            
            # Frequncy to send to FlightGear
            [sg.Input(size=(7, 1), justification='right', border_width=(4), font=('Helvetica', 20),
            text_color='red', key='input'), sg.Button('Clear')],
            
            # Digit
            [sg.Button('1'), sg.Button('2'), sg.Button('3')],
            
            # Digit
            [sg.Button('4'), sg.Button('5'), sg.Button('6')],
            
            # Digit
            [sg.Button('7'), sg.Button('8'), sg.Button('9')],
            
            # Digits and Enter
            [sg.Button('Enter'), sg.Button('0'), sg.Button('.'), sg.Cancel()],
            ]

        # Make window visiable
        window2 = sg.Window('Keypad', layout2, default_button_element_size=(5,2), auto_size_buttons=False)

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
        
                window2.close()
                window2_active = False
                window1.UnHide()
#                print(freq)
                break
