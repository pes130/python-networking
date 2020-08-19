#!/usr/bin/python3
import scapy.all as scapy

# sudo venv/bin/python network-scanner.py

def scan(ip):
    scapy.arping(ip)


scan("192.168.1.0/24")
