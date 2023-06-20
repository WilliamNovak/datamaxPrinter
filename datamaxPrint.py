import win32print
from PIL import Image

printer_name = win32print.GetDefaultPrinter() # Get Default Printer Name

def resize_image(image_path, new_width):
    
    image = Image.open(image_path) # Open the image file
    original_width, original_height = image.size # Get the original width and height
    
    aspect_ratio = original_width / original_height # Calculate the aspect ratio
    
    calculated_height = int(new_width / aspect_ratio) # Calculate the new height based on the aspect ratio and the new width
    
    resized_image = image.resize((new_width, calculated_height)) # Resize the image using the new width and calculated height

    pcxImage = resized_image.convert('1') # Convert image to B&W format
    pcxImage.save('LOGO.pcx', 'PCX') # Save the resized image

resize_image('logo_klin.bmp', 128) # Call function to resize image

with open('LOGO.pcx', 'rb') as file:
    pcx_data = file.read() # Get image content in bytes

dpl_img  = "\x02xBGLOGO\x0D\n" # Command to delete "LOGO" image from printer memory
dpl_img += "\x02IBPLOGO\x0D" # Command to add a new "LOGO" image in printer memory
dpl_img += pcx_data.decode('latin-1') # Data of the image to be saved

dpl_img_bytes = str(dpl_img).encode(encoding='latin-1') # Encode image data in bytes

# Execute commands to save image
printer = win32print.OpenPrinter(printer_name)
job = win32print.StartDocPrinter(printer, 1, ("Label", None, "RAW"))
win32print.WritePrinter(printer, dpl_img_bytes)
win32print.EndDocPrinter(printer)
win32print.ClosePrinter(printer)

dpl_code  = "\x02O0220\x0D\n"
dpl_code += "\x02M3000\x0D\n"
dpl_code += "\x02c0000\x0D\n"
dpl_code += "\x02f322\x0D\n"
dpl_code += "\x02e\x0D\n"
dpl_code += "\x02LC0000\x0D\n"
dpl_code += "H08\x0D\n"
dpl_code += "D11\x0D\n"
dpl_code += "SG\x0D\n"
dpl_code += "PI\x0D\n"
dpl_code += "R0003\x0D\n"
dpl_code += "z\x0D\n"
dpl_code += "W\x0D\n"
dpl_code += "^012Y1100000170192LOGO\x0D\n" # Command to print image
# dpl_code += "1W1D44000001000102\x0D\n" # qrCode
# dpl_code += "1D000000015010001234567890\x0D\n" # barCode
dpl_code += "221100200730177169.001\x0D\n"
dpl_code += "221100200640167V: 1\x0D\n"
dpl_code += "Q0001\x0D\n"
dpl_code += "E"

dpl_code_bytes = str(dpl_code).encode(encoding='latin-1') # Encode commands in bytes

# Print all
printer = win32print.OpenPrinter(printer_name)
job = win32print.StartDocPrinter(printer, 1, ("Label", None, "RAW"))
win32print.WritePrinter(printer, dpl_code_bytes)
win32print.EndDocPrinter(printer)
win32print.ClosePrinter(printer)