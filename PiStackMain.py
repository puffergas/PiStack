import PySimpleGUI as sg 
   
      
sg.theme('DarkBlack1') 
   
layout = [
    [sg.Text('COM1')], 
    [sg.Input(size=(7,1), key='-USE-', readonly=True, border_width=(4), text_color='red',
        background_color='white'), sg.Button('Switch'), sg.Input(size=(7, 1),
        text_color='red', border_width=(4), key='-STBYcomm1-')], 
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
        window['-USE-'].update(values['-STBYcomm1-']),
        window['-STBYcomm1-'].update(values['-USE-'])
  
window.close() 
