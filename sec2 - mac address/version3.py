#!/usr/bin/python3
import subprocess

interface = 'enp1s0'
new_mac = '00:11:22:33:44:66'

print("[+] Changing MAC address for ",interface, "to",new_mac)

subprocess.run("ip link set dev "+interface+" down", shell=True)
completed = subprocess.run("ip link set dev "+interface+" address "+ new_mac, shell=True)
subprocess.run("ip link set dev "+interface+" up", shell=True)
if completed.returncode == 0:
    print("[+] Mac de la interfaz "+interface+" cambiada con éxito")
else:
    print("[+] Problems changing interface MAC")
#subprocess.run("ip a show "+interface, shell=True)
