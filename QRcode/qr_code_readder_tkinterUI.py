import cv2
from pyzbar.pyzbar import decode
import tkinter as tk

class QRCodeScanner:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title('QR Code Scanner')

        # Create the label to display the result
        self.result_label = tk.Label(self.root, text='Scan a QR code')
        self.result_label.pack()

        # Create the button to start scanning
        self.scan_button = tk.Button(self.root, text='Scan', command=self.scan)
        self.scan_button.pack()

    def scan(self):
        # Open the camera
        cap = cv2.VideoCapture(0)

        while True:
            # Read a frame from the camera
            ret, frame = cap.read()

            # Decode the QR code if it is present in the frame
            decoded_objects = decode(frame)
            for obj in decoded_objects:
                self.result_label.config(text=obj.data.decode())

            # Display the frame
            cv2.imshow('frame', frame)

            # Exit if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the camera and close all windows
        cap.release()
        cv2.destroyAllWindows()

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    scanner = QRCodeScanner()
    scanner.run()
