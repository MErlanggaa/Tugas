import PySimpleGUI as sg

# Tambahkan layout untuk jendela
layout = [
    [sg.Text("Harga Barang"), sg.InputText(key="-HARGA-")],
    [sg.Text("Kuantitas"), sg.InputText(key="-KUANTITAS-")],
    [sg.Button("Hitung Total")],
    [sg.Text("Total Pembayaran:", size=(15, 1)), sg.Text("", size=(10, 1), key="-TOTAL-")],
]

# Buat jendela dari layout
window = sg.Window("Kasir Sederhana", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Hitung Total":
        try:
            harga = float(values["-HARGA-"])
            kuantitas = int(values["-KUANTITAS-"])
            total = harga * kuantitas
            window["-TOTAL-"].update(f"Rp.{total:.2f}")
        except ValueError:
            sg.popup_error("Harga dan Kuantitas harus berupa angka!")

window.close()
