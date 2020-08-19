#!/usr/bin/python3
import subprocess
import argparse
import re

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', required=True, help="Network interface to change. Use 'ip link show' to list")
    parser.add_argument('-m', '--mac', required=True, help="New MAC address to set")
    args = parser.parse_args()
    argsdict = vars(args)
    return argsdict

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for ",interface, "to",new_mac)
    # Poner el shell = True puede ser un problema de seguridad, ya que puedo ejecutar comandos con ;
    subprocess.run(["ip","link","set","dev",interface,"down"])
    completed = subprocess.run(["ip","link","set","dev",interface,"address",new_mac])
    subprocess.run(["ip","link","set","dev",interface,"up"])
    return completed.returncode

def extract_mac_address(interface):
    ip_result = subprocess.run(["ip","link","show",interface], stdout=subprocess.PIPE)
    mac_search = re.search(r"[\dA-Fa-f]{2}:[\dA-Za-z]{2}:[\dA-Fa-f]{2}:[\dA-Fa-f]{2}:[\dA-Fa-f]{2}:[\dA-Fa-f]{2}", ip_result.stdout.decode('utf-8'))
    if mac_search:
        return mac_search.group(0)
    else:
        return None

parametersDict = get_arguments()

interface = parametersDict["interface"]
new_mac = parametersDict["mac"]

current_mac = extract_mac_address(interface)
print("Current MAC is", current_mac)
status = change_mac(interface, new_mac)

 
current_mac = extract_mac_address(interface)
if status == 0 and current_mac == new_mac:
    print("[+] Interface "+interface+" MAC changed sucessfuly")
else:
    print("[+] Problems changing interface MAC")

