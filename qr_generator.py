# pip install pyqrcode
# instala la librería necesaria

import pyqrcode

url = pyqrcode.create('https://www.python.org/doc/')
url.svg('QR_generado.svg', scale=5)

# se pueden editar los valores como escala, color, background
# los colores se pueden indicar con su nombre o valor hexadecimal
# url.svg('QR_generado.svg', scale=5, module_color='#007FAB', background='red')