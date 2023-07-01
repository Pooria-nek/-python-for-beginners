import cv2
from pyzbar.pyzbar import decode
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

class QRCodeScanner:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title('QR Code Scanner')
        self.root.geometry("400x400")
        # Make the window resizable false
        # self.root.resizable(False,False)

        self.qrextract = tk.StringVar()
        self.qrextract.set("Scan a QR code")

        # Create the canvas to display the camera frame
        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack(pady=5, padx=5)

        # Create the entry to display the result
        self.qr_text = tk.Entry(self.root, textvariable=self.qrextract, font=("Helvetica", 16))
        self.qr_text.pack(pady=5, padx=5)

        # Create the button to start scanning
        self.scan_button = tk.Button(self.root, text='Copy', font=("Helvetica", 16), command=self.copy)
        self.scan_button.pack(pady=5, padx=5)

        # Open the camera
        self.cap = cv2.VideoCapture(0)

        # Start the scan loop
        self.scan()

    def scan(self):
        # Read a frame from the camera
        ret, frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Decode the QR code if it is present in the frame
        decoded_objects = decode(gray)
        for obj in decoded_objects:
            pts = np.array([obj.polygon], np.int32,)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frame, [pts], True, (0, 0, 255), 2)
            self.qrextract.set(str(obj.data)[2:-1])

        # cv2.imshow("QR", frame)

        frame = cv2.resize(frame, None, fx = 0.50, fy = 0.50)
        # Display the frame on the canvas
        img = Image.fromarray(frame, mode="RGB")
        imgtk = ImageTk.PhotoImage(image=img)
        self.canvas.imgtk = imgtk
        self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)

        # Schedule the next scan
        self.root.after(10, self.scan)

    def copy(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.qrextract.get())

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    scanner = QRCodeScanner()
    scanner.run()
