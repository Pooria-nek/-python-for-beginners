import pyqrcode
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

def generate_qr():
    qr_data = qr_text.get()
    qr = pyqrcode.create(qr_data)
    qr.png('qr.png', scale=8)

    img = Image.open('qr.png')
    img = img.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel.configure(image=img)
    panel.image = img

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x400")

frame = Frame(root)
frame.pack()

generate_button = tk.Button(frame, text="Generate QR Code", command=generate_qr)
generate_button.pack(side=LEFT, pady=10, padx=10)

qr_text = tk.Entry(frame, font=("Helvetica", 16))
qr_text.pack(side=LEFT, pady=10, padx=10)

panel = tk.Label(root)
panel.pack(pady=10)

root.mainloop()