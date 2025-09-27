from escpos.capabilities import *

#TODO: By including this profile it overides the default usb profile. I dont know why but it works.
my_printer_profile=get_profile_class('default')
my_printer_profile.profile_data['media']['width']['mm']=80
my_printer_profile.profile_data['media']['width']['pixels']=576
my_printer_profile.profile_data['media']['width']['dpi']=203
