#!/usr/bin/python3
import scapy.all as scapy

# sudo venv/bin/python network-scanner.py

def scan(ip):
    # 1. Creamos un paquete arp
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request.summary())
    # Esto te devuelve una lista de las propiedades de un objeto ARP
    #scapy.ls(scapy.ARP())


scan("192.168.1.254")
