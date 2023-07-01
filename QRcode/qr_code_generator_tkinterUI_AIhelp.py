from tkinter import *
import qrcode
from PIL import ImageTk

def create_qrcode(text):
    qr = qrcode.QRCode()
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="black")
    return img

def demo():
    def on_click(e):
        input_text = txt.get("0.0", "end-1c")
        print(input_text)
        img = create_qrcode(input_text).resize((250, 250))
        imgTk = ImageTk.PhotoImage(img)
        qr.configure(image=imgTk)
        qr.image = imgTk

    gui = Tk()
    gui.title("QR code generator")
    gui.option_add("*Font", "consolas 20")
    Label(gui, text="Write anything").grid(row=0, column=0)
    txt = Text(gui, height=4, width=30, fg="green")
    txt.insert(END, "")
    txt.grid(row=1, column=0)
    btn = Button(gui, text="create QR Code", bg="gold")
    btn.grid(row=2, column=0)
    btn.bind("<Button-1>", on_click)
    qr = Label(gui)
    qr.grid(row=0, column=1, rowspan=3)
    gui.mainloop()

if __name__ == '__main__':
    demo()
