# Networking Basics

## 1. TCP/IP (Transmission Control Protocol/Internet Protocol)

- **TCP/IP** is a suite of protocols that enable communication over the internet.
- **IP** handles addressing and routing, while **TCP** ensures reliable data delivery.
- **Layers**:
  - Application (HTTP, FTP)
  - Transport (TCP, UDP)
  - Internet (IP)
  - Network Interface (Ethernet)

## 2. DNS (Domain Name System)

- **DNS** translates domain names (e.g., `www.example.com`) into IP addresses (e.g., `192.0.2.1`).
- It acts like the "phonebook" of the internet, allowing users to access websites by name.

## 3. HTTP (Hypertext Transfer Protocol)

- **HTTP** is used for transferring web pages and data over the internet.
- **Methods**: 
  - `GET`: Retrieve data
  - `POST`: Send data
  - `PUT`: Update data
  - `DELETE`: Remove data
- **HTTPS** is the secure version, using encryption (SSL/TLS).

## 4. Other Common Protocols

- **FTP**: Transfers files between systems.
- **SMTP**: Sends email.
- **IMAP/POP3**: Retrieve email.
- **DHCP**: Automatically assigns IP addresses to devices on a network.

# Network Layers

This guide provides an overview of the **OSI** and **TCP/IP** models and their respective layers.

## OSI Model (7 Layers)

1. **Application Layer**
   - Interface for end-user applications.
   - Protocols: HTTP, FTP, SMTP.

2. **Presentation Layer**
   - Translates data formats for the application layer.
   - Handles encryption, compression, and translation.

3. **Session Layer**
   - Manages communication sessions between applications.
   - Ensures proper session establishment and termination.

4. **Transport Layer**
   - Manages end-to-end communication and data flow.
   - Protocols: TCP, UDP.

5. **Network Layer**
   - Routes data between devices on different networks.
   - Protocols: IP, ICMP.

6. **Data Link Layer**
   - Ensures error-free data transfer between devices on the same network.
   - Protocols: Ethernet, PPP.

7. **Physical Layer**
   - Transmits raw data bits over physical media.
   - Deals with hardware like cables, switches, and network interfaces.

## TCP/IP Model (4 Layers)

1. **Application Layer**
   - Combines OSI's Application, Presentation, and Session layers.
   - Protocols: HTTP, FTP, DNS, SMTP.

2. **Transport Layer**
   - Manages end-to-end communication.
   - Protocols: TCP, UDP.

3. **Internet Layer**
   - Handles routing and addressing of data packets.
   - Protocols: IP, ICMP.

4. **Network Access Layer**
   - Corresponds to OSI’s Data Link and Physical layers.
   - Handles hardware and physical transmission protocols (e.g., Ethernet)
     
# Common Protocols and Ports
- **HTTP**: Port 80
- **HTTPS**: Port 443
- **FTP**: Port 21 (Control), 20 (Data)
- **SFTP**: Port 22
- **SSH**: Port 22
- **SMTP**: Port 25
- **IMAP**: Port 143
- **POP3**: Port 110
- **DNS**: Port 53
- **Telnet**: Port 23
- **DHCP**: Port 67 (Server), 68 (Client)
- **RDP**: Port 3389
- **LDAP**: Port 389
- **SMB**: Port 445
- **SNMP**: Port 161 (Request), 162 (Trap)
- **NTP**: Port 123
- **ICMP**: N/A (Uses IP)
- **MSSQL**: Port 1433
- **MySQL**: Port 3306
- **PostgreSQL**: Port 5432

