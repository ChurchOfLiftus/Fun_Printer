from escpos.printer import Usb
from escpos.capabilities import *

# Custom printer profile for centering things
from printer_profile_custom import my_printer_profile

# Constants
HALLOWEENIE_PRICE:float = 3.75
CANNED_BREAD     :float = 5.00
CHEETOS          :float = 1.00

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
	printer.block_text("Want to see how you can be a 7-11 residential owner on halloween? Scan here! \n",columns=48)
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
	# If there is change due. Open register.
	if(total!=0):
		printer.cashdraw(2)
	printer.close()
	#--}}}

def main():
	hot_cheetos_sold =0;
	canned_bread_sold=0;
	halloweenies_sold=0;
	total_price      =0;
	cash_given       =0;
	while(1):
		# We need to figure out what the user wants.
		print("dogs_sold: "+str(halloweenies_sold)+" canned bread: "+str(canned_bread_sold)+" cheetos: "+str(hot_cheetos_sold))
		first_input = input("1 for halloween sale, 2 for Items, 3 end sale (fast checkout 1 weenie): Press x to clock out:")

		# First case we are done with the night.
		if first_input == "x":
			break

		elif first_input == "1":
			halloweenies_sold = input("How Many Halloweenies sold?:")

		elif first_input == "2":
			hot_cheetos_sold  = input("Hot cheetos?:")
			canned_bread_sold = input("canned_bread_sold?:")

		# End sale.
		elif first_input == "3":
			if(halloweenies_sold==0 and hot_cheetos_sold==0 and canned_bread_sold==0):
				halloweenies_sold = 1
			elif(halloweenies_sold!=0 and hot_cheetos_sold==0 and canned_bread_sold==0):
				print()
			else:
				cheeto_total = float(hot_cheetos_sold)*CHEETOS
				bread_total  = float(canned_bread_sold)*CANNED_BREAD
				total_price = cheeto_total+bread_total
				# f=open('bee_script.txt','r')
				# content = f.read()
				print("Total Price: "+str(total_price))
				cash_given = float(input("cash_given?:"))
				print("Chane Due: "+str(float(total_price)-float(cash_given))+"\n")

			printer=Usb(IDVENDOR,IDPRODUCT)
			print_start(printer)

			if(halloweenies_sold!=0):
				printer.text("Halloweenies"+" x                         "+str(halloweenies_sold)+" = "+str(0.00)+"\n")
			if(hot_cheetos_sold!=0):
				printer.text("Hot Cheetos"+"  x                         "+str(hot_cheetos_sold)+" = "+"{:0.2f}".format(cheeto_total)+"\n")
			if(canned_bread_sold!=0):
				printer.text("Canned Bread"+" x                         "+str(canned_bread_sold)+" = " +"{:0.2f}".format(bread_total)+"\n")

			if cash_given == "0" and (hot_cheetos_sold!=0 or canned_bread_sold!=0) :
				printer.text("Wizard hacks promotion -"+"{:0.2f}".format(total_price)+"\n")
				# printer.block_text(content,columns=48)
			else:
				printer.text("\n")
				printer.text("Total                                    "+"{:0.2f}".format(float(total_price))+"\n")
				printer.text("\n")
				printer.text("Cash given                               "+"{:0.2f}".format(cash_given)+"\n")
				printer.text("Chane Due                                "+"{:0.2f}".format(float(total_price)-float(cash_given))+"\n")

			print_end(printer,total_price)
			hot_cheetos_sold =0;
			canned_bread_sold=0;
			halloweenies_sold=0;
			total_price      =0;
			cash_given       =0;
			# f.close()
		else:
			print("INVALID OPTION TRY AGAIN")


if __name__== "__main__":
	main ()
	print("Thanks for the hard work at 7/11!")
