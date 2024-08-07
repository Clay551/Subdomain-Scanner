import socket
import pyfiglet
from colorama import Fore
import colorama
import os

os.system('cls' if os.name == 'nt' else 'clear')

def check_subdomain(subdomain, domain):
    try:
        subdomain_domain = subdomain.strip() + "." + domain
        ip = socket.gethostbyname(subdomain_domain)
        print(colorama.Fore.GREEN)
        print(f"Subdomain found: {subdomain_domain} - IP: {ip}")
        with open("subdomains_found.txt", "a") as file:
            file.write(f"Subdomain found: {subdomain_domain} - IP: {ip}\n")
        print(colorama.Fore.RESET)
    except socket.gaierror:
        print(colorama.Fore.RED)
        print(f"Subdomain not found: {subdomain_domain}")
        print(colorama.Fore.RESET)

print(colorama.Fore.RED)
pyfiglet.print_figlet("Asylum")
print(colorama.Fore.RESET)
print("e.g: example.com")
print('')
domain = input("Enter Domain==> ")

with open("subdomains.txt", 'r') as f:
    for subdomain in f:
        check_subdomain(subdomain, domain)
