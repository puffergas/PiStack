import PySimpleGUI as sg 
   
      
sg.theme('DarkBlack1') 
   
layout = [
    [sg.Text('                     COM1                                            NAV1')], 
    [sg.Input(size=(7,1), key='-USE_COM1-', readonly=True, border_width=(4), text_color='red',
        background_color='white'), sg.Button('Switch', key='-SWITCH_COM1-'), sg.Input(size=(7, 1),
        text_color='red', border_width=(4), key='-STBY_COM1-'),
            sg.Input(size=(7,1), key='-USE_NAV1-', readonly=True, border_width=(4), text_color='red',
            background_color='white'), sg.Button('Switch', key='-SWITCH_NAV1-'), sg.Input(size=(7, 1),
            text_color='red', border_width=(4), key='-STBY_NAV1-')],
    [sg.Text('                     COM2                                            NAV2')], 
    [sg.Input(size=(7,1), key='-USE_COM2-', readonly=True, border_width=(4), text_color='red',
        background_color='white'), sg.Button('Switch', key='-SWITCH_COM2-'), sg.Input(size=(7, 1),
        text_color='red', border_width=(4), key='-STBY_COM2-'),
            sg.Input(size=(7,1), key='-USE_NAV2-', readonly=True, border_width=(4), text_color='red',
            background_color='white'), sg.Button('Switch', key='-SWITCH_NAV2-'), sg.Input(size=(7, 1),
            text_color='red', border_width=(4), key='-STBY_NAV2-')],
    [sg.Button('Exit')]
] 
  
window = sg.Window('PiStack', layout, location=(100, 100), size=(800, 480)) 
  
while True: 
    event, values = window.read(1000) 
    print(event, values) 
      
    if event in  (None, 'Exit'): 
        break
      
    if event == '-SWITCH_COM1-': 
        # Update the "output" text element 
        # to be the value of "input" element 
        window['-USE_COM1-'].update(values['-STBY_COM1-']),
        window['-STBY_COM1-'].update(values['-USE_COM1-'])

    if event == '-SWITCH_NAV1-': 
        # Update the "output" text element 
        # to be the value of "input" element 
        window['-USE_NAV1-'].update(values['-STBY_NAV1-']),
        window['-STBY_NAV1-'].update(values['-USE_NAV1-'])

    if event == '-SWITCH_COM2-': 
        # Update the "output" text element 
        # to be the value of "input" element 
        window['-USE_COM2-'].update(values['-STBY_COM2-']),
        window['-STBY_COM2-'].update(values['-USE_COM2-'])

    if event == '-SWITCH_NAV2-': 
        # Update the "output" text element 
        # to be the value of "input" element 
        window['-USE_NAV2-'].update(values['-STBY_NAV2-']),
        window['-STBY_NAV2-'].update(values['-USE_NAV2-'])
  
window.close() 
