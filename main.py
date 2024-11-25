import qrcode as qrc
import PySimpleGUI as ui


layout = [ 
            [ui.Text("Insert link to generate QR code")],
            [ui.InputText(key="link")],
            [ui.Button("Generar código QR")]    ]

window = ui.Window("QR Code Generator", layout)

def generate_qr(link_to_generate):
    result = qrc.make(link_to_generate)
    type(result)
    result.save("qr.png")
    ui.popup("QR code generated successfully")



while True:
    event, values = window.read()
    if event == ui.WIN_CLOSED:
        break
    if event == "Generar código QR":
        link = values["link"]
        generate_qr(link)
        

window.close()