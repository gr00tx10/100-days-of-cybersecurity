#Reconnaissance

##Dork-
eg- site:(temp.com) filetype:pdf confidential


## 🛠 Common DNS Tools for Advanced Information Gathering
| Tool          | Usage                         | Description                                                |
|---------------|-------------------------------|------------------------------------------------------------|
| **Amass**     | `amass enum -d example.com`   | Powerful DNS enumeration and network mapping tool, supporting passive and active techniques. |
| **Sublist3r** | `sublist3r -d example.com`    | Quickly enumerates subdomains using search engines and brute-forcing. |
| **dnsenum**   | `dnsenum example.com`         | Gathers DNS info, including subdomains and DNS records, and attempts zone transfers. |
| **dnsrecon**  | `dnsrecon -d example.com`     | DNS reconnaissance with standard record enumeration and brute-force subdomain discovery. |
| **Fierce**    | `fierce --domain example.com` | Scans for non-contiguous IP space and gathers hostnames from DNS. |
| **dig**       | `dig example.com ANY`         | Versatile tool for querying DNS records.                   |
| **Nslookup**  | `nslookup example.com`        | Simple tool for DNS lookups and querying records.          |
| **TheHarvester** | `theharvester -d example.com -b google` | Gathers emails and subdomains from public sources, including DNS information. |
| **dnstracer** | `dnstracer example.com`       | Traces the path of DNS queries to their authoritative servers. |
| **whois**     | `whois example.com`           | Provides domain registration details, DNS servers, and contact information. |
|**Ghunt**|`ghunt --domain example.com`|A tool designed for gathering intelligence on Google accounts, including DNS information and subdomains. |
|**Maltego**|`maltego -h`|A powerful tool for visualizing relationships between entities (domains, emails, subdomains, etc.) in a graph.|
|**Shodan**| `www.shodan.io` |A search engine for discovering internet-connected devices and services, including DNS-related information.|
|**Dirb Gobuster**|`gobuster dir -u http://example.com -w wordlist.txt`|A tool for directory and subdomain brute-forcing with support for various DNS-related attacks.|
