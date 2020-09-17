import io
from base64 import b64encode
import pyqrcode
import eel

# initial and Start project
eel.init('web')

@eel.expose
def generateQRCode(data):
    img = pyqrcode.create(data)
    buffers = io.BytesIO()
    img.png(buffers, scale=8, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
    encoded = b64encode(buffers.getvalue()).decode("ascii")
    print("QR Code Generation Successfull")
    return "data:image/png;base64, " + encoded

eel.start('main.html', mode='firefox')

