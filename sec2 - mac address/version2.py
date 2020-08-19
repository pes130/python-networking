#!/usr/bin/python3
import subprocess

# shell true, interpreta primero el comando y resuelve variables de entorno

subprocess.run("ip link set dev enp1s0 down", shell=True)
subprocess.run("ip link set dev enp1s0 address 00:11:22:33:44:66", shell=True)
subprocess.run("ip link set dev enp1s0 up", shell=True)
print("Mac de la interfaz enp1s0 cambiada con éxito")
subprocess.run("ip a show enp1s0", shell=True)
