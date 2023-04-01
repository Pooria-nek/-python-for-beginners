# Importing library
import qrcode

print("its qrcode genarator")
data = input("tell me the text: ")
qr_ver = int(input("choose the version of qrcode(1, 2 or 3):"))
if qr_ver > 3 or qr_ver < 1:
    print("version " + str(qr_ver) + " not allowed ill chang it to 1")
    qr_ver = 1

file_name = input("what name should i save it? ")

# Creating an instance of QRCode class
qr = qrcode.QRCode(version = qr_ver,
                   box_size = 10,
                   border = 1)
 
# Adding data to the instance 'qr'
qr.add_data(data)
 
qr.make(fit = True)
img = qr.make_image()
img.save(file_name + '.png')


