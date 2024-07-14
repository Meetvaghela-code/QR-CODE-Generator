import qrcode

img = qrcode.make("hello my name is meet")
img.save("qrcode.jpg")