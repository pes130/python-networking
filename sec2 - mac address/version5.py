#!/usr/bin/python3
import subprocess
import argparse

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


parametersDict = get_arguments()

interface = parametersDict["interface"]
new_mac = parametersDict["mac"]

status = change_mac(interface, new_mac)
if status == 0:
    print("[+] Interface "+interface+" MAC changed sucessfuly")
else:
    print("[+] Problems changing interface MAC")
