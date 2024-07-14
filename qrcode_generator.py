import qrcode

# add your anyone data here eg.text,url etc.....
data = "https://www.instagram.com/meett.vaghela?igsh=MXd5eWJteDhyamhuOQ=="

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image 
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img.save("qrcode.png")

print("QR code saved as qrcode.png")
