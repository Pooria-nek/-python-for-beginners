import pyqrcode
import tkinter as tk
from PIL import ImageTk, Image

def generate_qr():
    qr_data = qr_text.get()
    qr = pyqrcode.create(qr_data)
    qr.png('qr.png', scale=8)
    img = ImageTk.PhotoImage(Image.open('qr.png'))
    panel = tk.Label(root, image=img)
    panel.image = img
    panel.pack()

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("300x300")

qr_text = tk.Entry(root, width=30)
qr_text.pack(pady=10)

generate_button = tk.Button(root, text="Generate", command=generate_qr)
generate_button.pack(pady=10)

root.mainloop()