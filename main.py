import qrcode

data = "Don't forget to subscribe"

# Simple QR Code
img = qrcode.make(data)
img.save('D:/python/Assignment_6/qrcode.png')

# Customized QR Code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color='red', back_color='white')
img.save('D:/python/Assignment_6/qrcode1.png')
