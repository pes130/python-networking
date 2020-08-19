#!/usr/bin/python3
import scapy.all as scapy

# sudo venv/bin/python network-scanner.py

def scan(ip):
    # 1. Creamos un paquete arp
    #   IP de destino
    #   Dirección física de broadcast
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request.show())
    # Creamos un paquete Ethernet
    broadcast = scapy.Ether(dst="FF:FF:FF:FF:FF:FF")
    print(broadcast.show())
    # scapy te permite combinarlos así.
    arp_request_broadcast = broadcast/arp_request
    print(arp_request_broadcast.summary())
    # Lo siguiente te muestra muchos más detalles
    arp_request_broadcast.show()

    

    


scan("192.168.1.254")
