import subprocess
import optparse
import time
import re

print("###################################")
print("     |M|A|C|  |C|H|A|N|G|E|R|!|    ")
print("####################################\n")




time.sleep(1)
def user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="Interface to change Mac address!")
    parse_object.add_option("-m","--mac_address",dest="mac_address",help="new Mac address!")

    (options,arguments) = parse_object.parse_args()

    return options

def change_mac_address(user_interface,user_mac):
    print("MacChanger started!")
    time.sleep(1)
    print("Changing..")
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac])
    subprocess.call(["ifconfig",user_interface,"up"])

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if new_mac_address:
        return new_mac_address.group(0)
    else:
        print("Mac address could not read.")

options = user_input()
change_mac_address(options.interface,options.mac_address)
last_mac = control_new_mac(str(options.interface))

if last_mac == options.mac_address:
    print("Mac address was changed to : " + last_mac)
else:
    print("Mac address did not get changed!")