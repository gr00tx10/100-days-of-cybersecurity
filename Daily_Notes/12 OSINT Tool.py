import requests
from bs4 import BeautifulSoup
import socket
import re
from urllib.parse import urljoin

def get_page_content(url):
    """Fetch the page content from a given URL."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_emails(text):
    """Extract all email addresses from the given text."""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return set(re.findall(email_pattern, text))

def extract_links(soup, base_url):
    """Extract all links from the given BeautifulSoup object."""
    return {urljoin(base_url, a['href']) for a in soup.find_all('a', href=True)}

def scrape_website(url):
    """Scrape a website for emails, links, headers, and IP."""
    response = get_page_content(url)
    if not response:
        return
    
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    emails = extract_emails(html_content)
    links = extract_links(soup, url)
    
    print("\n[+] HTTP Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
    
    try:
        domain = url.split("//")[-1].split("/")[0]
        ip_address = socket.gethostbyname(domain)
        print(f"\n[+] Resolved IP Address: {ip_address}")
    except socket.gaierror:
        print("\n[-] Could not resolve IP address")
    
    print("\n[+] Extracted Emails:")
    for email in emails:
        print(email)
    
    print("\n[+] Extracted Links:")
    for link in links:
        print(link)

if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    scrape_website(target_url)
