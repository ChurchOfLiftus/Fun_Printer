from escpos.printer import Usb
# from escpos.capabilities import *
# Custom printer profile for centering things
from printer_profile_custom import my_printer_profile

IDVENDOR = 0x0fe6
IDPRODUCT= 0x811e

printer=Usb(IDVENDOR,IDPRODUCT)
print(printer.is_usable())
printer.open()
printer.image("7-11.png",impl="graphics",center=True)
printer.text("\n")
printer.text("Thanks for choosing 7-11 on Halloween!\n")
printer.text("\n")
printer.close()
