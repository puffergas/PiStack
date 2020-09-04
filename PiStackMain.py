import PySimpleGUI as sg 
   
      
sg.theme('DarkBlack1') 
   
layout = [
    [sg.Text('COM1')], 
    [sg.Input(size=(7,1), key='-USEcom1-', readonly=True, border_width=(4), text_color='red',
        background_color='white'), sg.Button('Switch'), sg.Input(size=(7, 1),
        text_color='red', border_width=(4), key='-STBYcom1-'),
            sg.Input(size=(7,1), key='-USEnav1-', readonly=True, border_width=(4), text_color='red',
            background_color='white'), sg.Button('Switch'), sg.Input(size=(7, 1),
            text_color='red', border_width=(4), key='-STBYnav1-')], 
    [sg.Button('Exit')]
] 
  
window = sg.Window('PiStack', layout, location=(100, 100), size=(800, 480)) 
  
while True: 
    event, values = window.read(1000) 
    print(event, values) 
      
    if event in  (None, 'Exit'): 
        break
      
    if event == 'Switch': 
        # Update the "output" text element 
        # to be the value of "input" element 
        window['-USEcom1-'].update(values['-STBYcom1-']),
        window['-STBYcom1-'].update(values['-USEcom1-'])
  
window.close() 
