import pyqrcode
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

class QRCodeGenerator:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title('QR Code Generator')
        self.root.geometry("400x400")
        #Make the window resizable false
        # self.root.resizable(False,False)

        self.panel = tk.Label(self.root)
        self.panel.pack(pady=5, padx=5)

        self.qr_text = tk.Entry(self.root, font=("Helvetica", 16))
        self.qr_text.pack(pady=5, padx=5)

        self.generate_button = tk.Button(self.root, text="Generate QR-Code", command=self.generate_qr)
        self.generate_button.pack(pady=5, padx=5)

    def generate_qr(self):
        qr_data = self.qr_text.get()
        qr = pyqrcode.create(qr_data)
        qr.png('qr.png', scale=8)

        img = Image.open('qr.png')
        img = img.resize((300, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.panel.configure(image=img)
        self.panel.image = img

    def run(self):
        self.root.mainloop()

# root = tk.Tk()
# root.title("QR Code Generator")
# root.geometry("400x400")

if __name__ == '__main__':
    generator = QRCodeGenerator()
    generator.run()