import win32print
from PIL import Image

dpl_code  = "\x02O0220\n"
dpl_code += "\x02M3000\n"
dpl_code += "\x02c0000\n"
dpl_code += "\x02f322\n"
dpl_code += "\x02e\n"
dpl_code += "\x02LC0000\n"
dpl_code += "H08\n"
dpl_code += "D11\n"
dpl_code += "SG\n"
dpl_code += "PI\n"
dpl_code += "R0003\n"
dpl_code += "z\n"
dpl_code += "W\n"
# dpl_code += "^012Y1100000170192LOGO_EMP\n"
dpl_code += "221100200730177169.001\n"
dpl_code += "221100200640167V: 1\n"
dpl_code += "Q0001\n"
dpl_code += "E"

dpl_code_bytes = str(dpl_code).encode(encoding='cp437')
# print(dpl_code)

# printer_name = win32print.GetDefaultPrinter()
# printer = win32print.OpenPrinter(printer_name)
# job = win32print.StartDocPrinter(printer, 1, ("Label", None, "RAW"))
# win32print.StartPagePrinter(printer)
# win32print.WritePrinter(printer, dpl_code_bytes)
# win32print.EndPagePrinter(printer)
# win32print.EndDocPrinter(printer)
# win32print.ClosePrinter(printer)