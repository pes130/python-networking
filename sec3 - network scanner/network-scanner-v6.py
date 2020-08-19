#!/usr/bin/python3
import scapy.all as scapy

# FOrmateamos un poco la salida
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="FF:FF:FF:FF:FF:FF")
    arp_request_broadcast = broadcast/arp_request

    answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    
    print("IP\t\t\tMAC Address\n--------------------------------------------")
    for element in answered_list:      
        response = element[1]
        print(response.psrc+"\t\t"+response.hwsrc)
        
    


    

    


scan("192.168.1.0/24")
