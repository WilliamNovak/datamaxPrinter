import win32print
from PIL import Image

printer_name = win32print.GetDefaultPrinter()

image = Image.open('LOGO_EMP.jpg')
image.save('LOGO_EMP200.jpg',dpi=(200,200))

img = Image.open('LOGO_EMP200.jpg')
pcxImage = img.convert('1')

# Defina o tamanho da escala em polegadas
escala_polegadas = 0.01

# Converta a escala de polegadas para pixels
dpi = 200  # Define a resolução em pontos por polegada (dpi)
escala_pixels = escala_polegadas * dpi

# Calcule o novo tamanho da imagem
largura_atual, altura_atual = pcxImage.size
nova_largura = int(largura_atual * escala_pixels)
nova_altura = int(altura_atual * escala_pixels)

# Redimensione a imagem
pcxImage = pcxImage.resize((nova_largura, nova_altura))
pcxImage.save('LOGO_EMP200.pcx','PCX')

with open('LOGO_EMP200.pcx', 'rb') as file:
    pcx_data = file.read()

# dpl_code  = "\x02IBPLOGO_EMP\n" + pcx_data.decode('latin-1') + "\n"
# dpl_code += "\x02O0220\n"
# dpl_code += "\x02M3000\n"
# dpl_code += "\x02c0000\n"
# dpl_code += "\x02f322\n"
# dpl_code += "\x02e\n"
# dpl_code += "\x02LC0000\n"
# dpl_code += "H08\n"
# dpl_code += "D11\n"
# dpl_code += "SG\n"
# dpl_code += "PI\n"
# dpl_code += "R0003\n"
# dpl_code += "z\n"
# dpl_code += "W\n"
# dpl_code += "^012Y1100000170192LOGO_EMP\n"
# dpl_code += "1Y1100001300140LOGO_EMP\n"
# dpl_code += "1W1D44000001000102\n" # qrCode
# dpl_code += "1D000000015010001234567890\n" # barCode
# dpl_code += "221100200730177169.001\n"
# dpl_code += "221100200640167V: 1\n"
# dpl_code += "Q0001\n"
# dpl_code += "E"

dpl_code  = "\x02O0220\x0D\n"
dpl_code += "\x02f220\x0D\n"
dpl_code += "\x02e\x0D\n"
dpl_code += "\x02xBGPB0\x0D\n"
dpl_code += "\x02IBPPB0\x0D"
dpl_code += pcx_data.decode('latin-1') + "\x02L\x0D\n"
dpl_code += "H10\x0D\n"
dpl_code += "PC\x0D\n"
dpl_code += "A2\x0D\n"
dpl_code += "D11\x0D\n"
dpl_code += "1Y1100001300140PB0\x0D\n"
dpl_code += "^01\x0D\n"
dpl_code += "Q0001\x0D\n"
dpl_code += "E"

dpl_code_bytes = str(dpl_code).encode(encoding='latin-1')
# print(dpl_code_bytes)

with open('arquivo.prn', 'wb') as file:
    file.write(dpl_code_bytes)

# printer = win32print.OpenPrinter(printer_name)
# job = win32print.StartDocPrinter(printer, 1, ("Label", None, "RAW"))
# win32print.WritePrinter(printer, dpl_code_bytes)
# win32print.EndDocPrinter(printer)
# win32print.ClosePrinter(printer)