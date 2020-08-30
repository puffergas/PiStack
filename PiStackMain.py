import PySimpleGUI as sg 
   
      
sg.theme('DarkBlack1') 
   
layout = [
    [sg.Text('COM1              NAV1')], 
    [sg.Text(size=(7,1), key='-USE-', text_color='#6D9F85', background_color='white'), sg.Button('Switch'),
        sg.Input(size=(7, 1), key='-STBYcomm1-')], 
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
        window['-USE-'].update(values['-STBYcomm1-']) 
  
window.close() 
