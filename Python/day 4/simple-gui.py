import PySimpleGUI as sg

layout = [[sg.Button('Klik saya')]]

window = sg.Window('Contoh Program PySimpleGUI', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Klik saya':
        print('Tombol Diklik')

window.close()
