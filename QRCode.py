import pyqrcode
import png
from pyqrcode import QRCode

# Adicionando Link 
QRString = input("Digite o link para o QRCode: ")

# Montando QRCode
url = pyqrcode.create(QRString)

# Salvando a imagem do QRCode
url.png(r'qr.png', scale=8)