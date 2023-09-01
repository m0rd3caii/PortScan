#!/bin/python3

import socket
from pwn import log
import ipaddress
from termcolor import colored

def ip_validator(ip_addr):
     ip_valid = False
  
     try:
         ip_object = ipaddress.ip_address(ip_addr)
         ip_valid = True
     except ValueError:
         print(f"The IP address {ip_addr} is not valid")
 
 def parse_args():
     parser = argparse.ArgumentParser(description="Enumeration Port.")
     parser.add_argument("-i", "--ipaddr", dest="ip", required=True, help="IP to scan")
     args = parser.parse_args()
   
     return args

def scan_ports(ip_scan):
     t_IP = socket.gethostbyname(ip_scan)
     print(f"\t[+] Host: {t_IP}")
     p = log.progress("Scanning")
 
     for i in range(1, 65536):
         p.status(f"\nDiscovering port {i}")
         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         result = sock.connect_ex((t_IP, i))
         
         if result == 0:
             print(colored(f"\t[+] Port {i} : OPEN", "green"))
         sock.close()

if __name__ == "__main__":
     ip_address = parse_args()
     ip_scan = ip_address.ip
     ip_validator(ip_scan)
     scan_ports(ip_scan)
