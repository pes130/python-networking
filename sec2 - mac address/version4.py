#!/usr/bin/python3
import subprocess

subprocess.run("clear")

print ("#############################################")
print ("#              MAC CHANGER                  #")
print ("#############################################")


interface = input("interface > ")
new_mac = input("new MAC > ")

print("[+] Changing MAC address for ",interface, "to",new_mac)

# Poner el shell = True puede ser un problema de seguridad, ya que puedo ejecutar comandos con ;
subprocess.run(["ip","link","set","dev",interface,"down"])
completed = subprocess.run(["ip","link","set","dev",interface,"address",new_mac])
subprocess.run(["ip","link","set","dev",interface,"up"])
if completed.returncode == 0:
    print("[+] Interface "+interface+" MAC changed sucessfuly")
else:
    print("[+] Problems changing interface MAC")
