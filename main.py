import qrcode as qrc
#from tkinter import *
#from tkinter import ttk
import PySimpleGUI as ui

def generate_qr(link_to_generate):
    result = qrc.make(link_to_generate)
    type(result)
    result.save("qr.png")

## Tkinter
#root =Tk()

""""
## Personalization
root.title("QR Code Generator")
root.geometry("400x400")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)



"""
layout = [ 
            [ui.Text("Insert link to generate QR code")],
            [ui.InputText(key="link")],
            [ui.Button("Generar código QR")],
            [ui.Image(key="qr_image")],
            [ui.Button("Close")]]


window = ui.Window("QR Code Generator", layout)

def update_window():
    window["qr_image"].update("qr.png")

while True:
    event, values = window.read()
    if event == "Close" or event == ui.WIN_CLOSED:
        break
    if event == "Generar código QR":
        generate_qr(values["link"])
        update_window()

#root.mainloop()
        

window.close()