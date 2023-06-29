import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()

frame = tk.Frame(root, bg="#456732")

Label_pic_path = tk.Label(frame, text="img path:", padx=25, pady=20, font=("verdana", 16), bg="#456732")
Label_pic_show = tk.Label(frame, bg="#456732")
Entr_pic_path = tk.Entry(frame, font=("verdana", 16))
Button_browse = tk.Button(frame, text="select image", bg="grey", fg="#ffffff", font=("verdana", 16))

def select_pic():
    global img
    filename = filedialog.askopenfilename(initialdir="/image", title="select image", filetypes=(("png image", "*.png"), ("jpg image", "*.jpg")))
    img = Image.open(filename)
    img = img.resize((100, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    Label_pic_show['image'] = img
    Entr_pic_path.insert(0, filename)

Button_browse['command'] = select_pic

frame.pack()

Label_pic_path.grid(row=0, column=0)
Entr_pic_path.grid(row=0, column=1, padx=(0, 20))
Label_pic_show.grid(row=1, column=0, columnspan="2")
Button_browse.grid(row=2, column=0, columnspan="2", padx=10, pady=10)

root.mainloop()