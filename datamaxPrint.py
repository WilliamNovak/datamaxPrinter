import win32print
from PIL import Image

printer_name = win32print.GetDefaultPrinter()

image = Image.open('LOGO_EMP.jpg')
pcxImage = image.convert('1')
pcxImage.resize((256,256))

pcxImage.save('LOGO.pcx','PCX')

with open('LOGO.pcx', 'rb') as file:
    pcx_data = file.read()

dpl_code  = "\x02O0220\x0D\n"
dpl_code += "\x02M3000\x0D\n"
dpl_code += "\x02c0000\x0D\n"
dpl_code += "\x02f322\x0D\n"
dpl_code += "\x02e\x0D\n"
dpl_code += "\x02xBGLOGO\x0D\n"
dpl_code += "\x02IBPLOGO\x0D"
dpl_code += pcx_data.decode('latin-1') + "\x02L\x0D\n"
dpl_code += "\x02LC0000\x0D\n"
dpl_code += "H08\x0D\n"
dpl_code += "D11\x0D\n"
dpl_code += "SG\x0D\n"
dpl_code += "PI\x0D\n"
dpl_code += "R0003\x0D\n"
dpl_code += "z\x0D\n"
dpl_code += "W\x0D\n"
dpl_code += "^012Y1100000170192LOGO\x0D\n"
# dpl_code += "1W1D44000001000102\x0D\n" # qrCode
# dpl_code += "1D000000015010001234567890\x0D\n" # barCode
dpl_code += "221100200730177169.001\x0D\n"
dpl_code += "221100200640167V: 1\x0D\n"
dpl_code += "Q0001\x0D\n"
dpl_code += "E"

dpl_code_bytes = str(dpl_code).encode(encoding='latin-1')
# print(dpl_code_bytes)

# with open('arquivo.prn', 'wb') as file:
#     file.write(dpl_code_bytes)

printer = win32print.OpenPrinter(printer_name)
job = win32print.StartDocPrinter(printer, 1, ("Label", None, "RAW"))
win32print.WritePrinter(printer, dpl_code_bytes)
win32print.EndDocPrinter(printer)
win32print.ClosePrinter(printer)