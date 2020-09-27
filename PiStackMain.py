import PySimpleGUI as sg
from telnet import FlightGear

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

fg = FlightGear('localhost', 5401)

fg_com1 = fg['/instrumentation/comm/frequencies/selected-mhz']
fg_stby_com1 = fg['/instrumentation/comm/frequencies/standby-mhz']

fg_com2 = fg['/instrumentation/comm[1]/frequencies/selected-mhz']
fg_stby_com2 = fg['/instrumentation/comm[1]/frequencies/standby-mhz']

fg_nav1 = fg['/instrumentation/nav/frequencies/selected-mhz']
fg_stby_nav1 = fg['/instrumentation/nav/frequencies/standby-mhz']

fg_nav2 = fg['/instrumentation/nav[1]/frequencies/selected-mhz']
fg_stby_nav2 = fg['/instrumentation/nav[1]/frequencies/standby-mhz']

sg.theme('DarkBlack1')

layout = [
    [sg.Text('                    COM1                                           NAV1')], 
    [sg.Input((fg_com1), size=(7,1), key='-use_com1-', readonly=True, border_width=(4), text_color='red',
        background_color='white'), sg.Button('<==>', key='-SWITCH_COM1-'), sg.Input((fg_stby_com1), size=(7, 1),
        text_color='red', border_width=(4), key='-stby_com1-'),
            sg.Input((fg_nav1), size=(7,1), key='-use_nav1-', readonly=True, border_width=(4), text_color='red',
            background_color='white'), sg.Button('<==>', key='-SWITCH_NAV1-'), sg.Input((fg_stby_nav1), size=(7, 1),
            text_color='red', border_width=(4), key='-stby_nav1-')],
    [sg.Text('                    COM2                                           NAV2')], 
    [sg.Input((fg_com2), size=(7,1), key='-use_com2-', readonly=True, border_width=(4), text_color='red',
        background_color='white'), sg.Button('<==>', key='-SWITCH_COM2-'), sg.Input((fg_stby_com2), size=(7, 1),
        text_color='red', border_width=(4), key='-stby_com2-'),
            sg.Input((fg_nav2), size=(7,1), key='-use_nav2-', readonly=True, border_width=(4), text_color='red',
            background_color='white'), sg.Button('<==>', key='-SWITCH_NAV2-'), sg.Input((fg_stby_nav2), size=(7, 1),
            text_color='red', border_width=(4), key='-stby_nav2-')],
    [sg.Button('Exit')]
]

window = sg.Window('PiStack', layout, location=(100, 100), size=(800, 480)) 
  
while True: 
    event, values = window.read(1000)
    # Un-comment the below to print values to the Python Terminal
    # print(event, values)
    

    if event in  (None, 'Exit'): 
        break
      
    if event == '-SWITCH_COM1-': 
        # Swap COM1 frequency
        window['-use_com1-'].update(values['-stby_com1-']),
        window['-stby_com1-'].update(values['-use_com1-'])
        fg['/instrumentation/comm/frequencies/selected-mhz'] = values['-stby_com1-']
        fg['/instrumentation/comm/frequencies/standby-mhz'] = values['-use_com1-']

    if event == '-SWITCH_NAV1-': 
        # Swap NAV1 frequncy
        window['-use_nav1-'].update(values['-stby_nav1-']),
        window['-stby_nav1-'].update(values['-use_nav1-'])
        fg['/instrumentation/nav/frequencies/selected-mhz'] = values['-stby_nav1-']
        fg['/instrumentation/nav/frequencies/standby-mhz'] = values['-use_nav1-']
        
    if event == '-SWITCH_COM2-': 
        # Swap COM2 frequncy
        window['-use_com2-'].update(values['-stby_com2-']),
        window['-stby_com2-'].update(values['-use_com2-'])
        fg['/instrumentation/comm[1]/frequencies/selected-mhz'] = values['-stby_com2-']
        fg['/instrumentation/comm[1]/frequencies/standby-mhz'] = values['-use_com2-']
        
    if event == '-SWITCH_NAV2-': 
        # Swap NAV2 frequncy
        window['-use_nav2-'].update(values['-stby_nav2-']),
        window['-stby_nav2-'].update(values['-use_nav2-'])
        fg['/instrumentation/nav[1]/frequencies/selected-mhz'] = values['-stby_nav2-']
        fg['/instrumentation/nav[1]/frequencies/standby-mhz'] = values['-use_nav2-']
        
window.close(); del window
