import qrcode

# Link for website
input_data = "https://www.youtube.com/watch?v=8NKOfVXAfgs&t=1s"
#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=8)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode0004.png')