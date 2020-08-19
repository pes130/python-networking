#!/usr/bin/python3
import scapy.all as scapy
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('network', 
                    help="Network to scan")
    parser.add_argument('-t', '--timeout', 
                    type=int, 
                    required=False, 
                    help="Max timeout to wait for a response. In seconds", 
                    default=1)
    args = parser.parse_args()
    argsdict = vars(args)
    return argsdict

def scan(ip, timeout_secs):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="FF:FF:FF:FF:FF:FF")
    arp_request_broadcast = broadcast/arp_request   
    answered_list = scapy.srp(arp_request_broadcast, timeout=timeout_secs, verbose=False)[0]
    clients_lists = []

    for element in answered_list:      
        response = element[1]
        client_dict = {"ip":response.psrc, "mac":response.hwsrc}
        clients_lists.append(client_dict)

    return clients_lists 
    

def print_results(list_of_clients):
    print("IP\t\t\tMAC Address\n--------------------------------------------")
    for client in list_of_clients:
        print(client["ip"]+"\t\t"+client["mac"])
    
arguments_dict = get_arguments()
network = arguments_dict["network"]
timeout = arguments_dict["timeout"]
clients = scan(network, timeout)
print_results(clients)
