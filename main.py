import qrcode as qrc
import PySimpleGUI as ui


layout = [ 
            [ui.Text("Insert link to generate QR code")],
            [ui.InputText(key="link")],
            [ui.Button("Generar código QR")],
            [ui.Image(key="qr_image")],
            [ui.Button("Close")]]

window = ui.Window("QR Code Generator", layout)

def generate_qr(link_to_generate):
    result = qrc.make(link_to_generate)
    type(result)
    result.save("qr.png")

def update_window():
    window["qr_image"].update("qr.png")

while True:
    event, values = window.read()
    if event == ui.WIN_CLOSED or event == "Close":
        break
    if event == "Generar código QR":
        link = values["link"]
        generate_qr(link)
        update_window()
        

window.close()