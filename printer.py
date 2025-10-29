from escpos.printer import Usb
from escpos.capabilities import *

# Custom printer profile for centering things
from printer_profile_custom import my_printer_profile

# Constants
HALLOWEENIE_PRICE:float = 3.75
CANNED_BREAD     :float = 5.00

IDVENDOR = 0x0fe6
IDPRODUCT= 0x811e

# Open connection and print the logo.
def print_start(printer): #--{{{
	# print(printer.is_usable())
	printer.open()
	printer.image("7-11.png",impl="graphics",center=True)
	printer.text("\n")
	printer.text("Thanks for choosing 7-11 on Halloween!\n")
	printer.text("\n")
	#--}}}

def print_end(printer,total=0): #--{{{
	# Print last QR section
	printer.text("\n")
	printer.text("\n")
	printer.block_text("Liked your experience? Take our survey! \n",columns=48)
	printer.text("\n")
	printer.qr("https://www.youtube.com/watch?v=dQw4w9WgXcQ",size=6,center=True) #Trap QR code.
	printer.text("\n")
	printer.text("\n")
	printer.text("\n")
	printer.text("\n")
	printer.text("\n")
	printer.text("\n")
	printer.text("\n")
	printer.cut()
	printer.text("\n")
	printer.buzzer(times=2,duration=4)
	if(total<=0):
		printer.cashdraw(2)
	printer.close()
	#--}}}

def main():
	customer_number :int = 1;
	halloweenies_sold=0;
	meal_combo       =0;
	cash_given       =0;
	misc_item        =0;
	misc_item_price  =0;
	total_price      =0;
	while(1):
		# We need to figure out what the user wants.
		print("dogs_sold: "+str(halloweenies_sold)+" meal_combo: "+str(meal_combo))
		first_input = input("1 for halloween sale, 2 misc, 3 end sale, Press + to clock out:")

		# First case we are done with the night.
		if first_input == "+":
			break

		elif first_input == "1":
			halloweenies_sold = input("How Many Halloweenies sold?:")
			meal_combo= input("meal_combo?:")

		elif first_input == "2":
			misc_item       = int(input("Misc Item's: "))
			misc_item_price = float(input("Misc Item price: "))
			total_price = misc_item*misc_item_price

		elif first_input == "3":
			if(total_price!=0):
				print("Total Price: "+str(total_price))
				cash_given = float(input("cash_given?:"))
				print("Chane Due: "+str(float(total_price)-float(cash_given))+"\n")
			else:
				cash_given=0

			printer=Usb(IDVENDOR,IDPRODUCT)
			print_start(printer)

			printer.text("         Customer# "+str(customer_number)+"\n")
			printer.text("\n")
			if(halloweenies_sold!=0):
				printer.text("Halloweenies"+" x                         "+str(halloweenies_sold)+" = "+str(0.00)+"\n")
			if(meal_combo!=0):
				printer.text("  Meal Combo"+" x                         "+str(meal_combo)       +" = "+str(0.00)+"\n")
			if(misc_item!=0):
				printer.text("Misc Items  "+" x                         "+str(misc_item)        +" = "+str(misc_item*misc_item_price)+"\n")
			printer.text("\n")
			printer.text("Total                                    "+"{:0.2f}".format(float(total_price))+"\n")
			printer.text("\n")
			printer.text("Cash given                               "+"{:0.2f}".format(cash_given)+"\n")
			finish_price=float(total_price)-float(cash_given)
			if(finish_price<=0):
				printer.text("Change Due                               "+"{:0.2f}".format(abs(finish_price))+"\n")
			else:
				printer.text("Cash stil Due                            "+"{:0.2f}".format(abs(finish_price))+"\n")

			print_end(printer,finish_price)

			halloweenies_sold=0;
			meal_combo       =0;
			cash_given       =0;
			misc_item        =0;
			misc_item_price  =0;
			total_price      =0;
			customer_number=customer_number+1
		else:
			print("INVALID OPTION TRY AGAIN")


if __name__== "__main__":
	main ()
	print("Thanks for the hard work at 7/11!")
