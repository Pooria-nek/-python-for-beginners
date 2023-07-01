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

        # Create the label to display the result
        self.result_label = tk.Label(self.root, text='Scan a QR code')
        self.result_label.pack()

        # Create the canvas to display the camera frame
        self.canvas = tk.Canvas(self.root, width=640, height=480)
        self.canvas.pack()

        # Create the button to start scanning
        self.scan_button = tk.Button(self.root, text='Scan')
        self.scan_button.pack()

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

            print("Data: ", obj.data)
            pts = np.array([obj.polygon], np.int32,)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frame, [pts], True, (0, 0, 255), 2)

            self.result_label.config(text=obj.data)

        # cv2.imshow("QR", frame)

        # Display the frame on the canvas
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        self.canvas.imgtk = imgtk
        self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)

        # Schedule the next scan
        self.root.after(10, self.scan)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    scanner = QRCodeScanner()
    scanner.run()
