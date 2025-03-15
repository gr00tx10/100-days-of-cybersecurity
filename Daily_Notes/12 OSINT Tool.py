#!/bin/python3

import requests
from bs4 import BeautifulSoup
import socket

testingwebpage = "http://testphp.vulnweb.com/"

response = requests.get(testingwebpage)
print("\n[+] HTTP Headers:")
for key, value in response.headers.items():
    print(f"{key}: {value}")

# Get IP Address
ip_address = socket.gethostbyname("testphp.vulnweb.com")
print(f"\n[+] Resolved IP Address: {ip_address}")

# Extract links from the webpage
soup = BeautifulSoup(response.text, "html.parser")
links = [a["href"] for a in soup.find_all("a", href=True)]

print("\n[+] Extracted Links:")
for link in links:
    print(link)
