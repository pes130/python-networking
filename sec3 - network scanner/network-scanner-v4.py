#!/usr/bin/python3
import scapy.all as scapy

# Aquí vamos a enviar la request y parsear la respuesta

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="FF:FF:FF:FF:FF:FF")
    arp_request_broadcast = broadcast/arp_request
    # función para enviar
    # devuelve 2 listas: una con paquetes contestados y otra con no contestados
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=2)
    print(answered.summary())
    # print(unanswered.summary())

    

    


scan("192.168.1.0/24")
