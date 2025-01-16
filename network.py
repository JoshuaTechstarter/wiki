import socket
import os
import platform
import ipaddress


hostname = "example.com"
ip_address = socket.gethostbyname(hostname)
print(f"Die IP-Adresse von {hostname} ist {ip_address}")


def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = f"ping {param} 4 {host}"
    return os.system(command)


host = "google.com"
ping(host)


network = ipaddress.ip_network("192.168.10.0/24")
print(f"Netzwerk: {network}")
print(f"Erste IP: {network[0]}")
print(f"Letzte IP: {network[-1]}")
print(f"Anzahl nutzbarer Hosts: {network.num_addresses - 2}")
