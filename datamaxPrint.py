import win32print

dpl_code  = "\x02O0220"
dpl_code += "\x02M3000"
dpl_code += "\x02c0000"
dpl_code += "\x02f322"
dpl_code += "\x02e"
dpl_code += "\x02LC0000"
dpl_code += "H08"
dpl_code += "D11"
dpl_code += "SG"
dpl_code += "PI"
dpl_code += "R0003"
dpl_code += "z"
dpl_code += "W"
dpl_code += "^012Y1100000170192LOGO_EMP"
dpl_code += "221100200730177169.001"
dpl_code += "221100200640167V: 1"
dpl_code += "Q0002"
dpl_code += "E"

dpl_code_bytes = dpl_code.encode('utf-8')

# print(dpl_code_bytes)

printer_name = win32print.GetDefaultPrinter()
printer = win32print.OpenPrinter(printer_name)
win32print.StartDocPrinter(printer, 1, ("raw_data", None, "RAW"))
win32print.WritePrinter(printer, dpl_code_bytes)
win32print.EndDocPrinter(printer)
win32print.ClosePrinter(printer)