#!/usr/bin/python3
import scapy.all as scapy

# Parseamos la respuesta
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="FF:FF:FF:FF:FF:FF")
    arp_request_broadcast = broadcast/arp_request
    # devuelve 2 listas: una con paquetes contestados y otra con no contestados
    # Poniendo el 0 me devuelve sólo la lista 1
    answered_list = scapy.srp(arp_request_broadcast, timeout=2)[0]
    
    # print(answered_list.summary())

    for element in answered_list:
        print("----------------------------------------------------------------------------")
        response = element[1]
        print(response.psrc)
        print(response.hwsrc)
    


    

    


scan("192.168.1.0/24")
