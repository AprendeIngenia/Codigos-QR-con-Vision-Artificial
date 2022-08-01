# Importamos las librerias
import pyqrcode
import png
from pyqrcode import QRCode


# CODIGOS QR ID
# Variables
con = 1234

# Generamos los QR
while con <= 1239:

    #id = str('j') +  str(con)
    roster = con
    id = '65' + str(con)
    # Creamos los QR
    qr = pyqrcode.create(65 and id, error= 'L')
    # Guardamos
    qr.png('A' + str(roster) + '.png', scale = 6)
    # Aumentamos con
    con = con + 1

# url = 'https://www.youtube.com/c/AprendeeIngenia/videos'
# url = pyqrcode.create(url, error = 'L')
# url.png('URL' + '.png', scale = 6)

