#!/bin/python3

import socket
import argparse
from pwn import log
import ipaddress
from termcolor import colored
import signal
import sys

def ip_validator(ip_addr):
    print(f"The IP address {ip_addr} is not valid")

def parse_args():
    parser = argparse.ArgumentParser(description="Enumeration Port.")
    parser.add_argument("-i", "--ipaddr", dest="ip", required=True, help="IP to scan")
    args = parser.parse_args()
    return args

def scan_ports(ip_scan):
    t_IP = socket.gethostbyname(ip_scan)  # Obtener la dirección IP correspondiente al nombre del host
    print(f"\t[+] Host: {t_IP}")
    p = log.progress("Scanning")  # Mostrar el progreso

    try:
        for i in range(1, 65536):
            p.status(f"\nDiscovering port {i}")  # Actualizar el estado de progreso
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IPv4, SOCK_STREAM = protocolo TCP
            result = sock.connect_ex((t_IP, i))

            if result == 0:
                print(colored(f"\t[+] Port {i} : OPEN", "green"))
            sock.close()
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        sys.exit(0)

def signal_handler(sig, frame):
    print("\nScan interrupted by user.")
    sys.exit(0)

if __name__ == "__main__":
    ip_address = parse_args()
    ip_scan = ip_address.ip
    ip_validator(ip_scan)
    signal.signal(signal.SIGINT, signal_handler)  # Configurar el manejador de señales para Ctrl+C
    scan_ports(ip_scan)
