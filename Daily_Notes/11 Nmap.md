# Nmap  

## Skipping Host Discovery (Ping)  
nmap -Pn 

<ip/dns/ip-file/dns-file>

## All ports
nmap -p- <target>

## Specific Ports 
nmap -p 20,21,80 <target>
nmap -p 100-500 <target>

## TCP 
nmap -pT <target>

## Service Detection 
nmap -sV <target>

## Timing Speed, Accuracy 
nmap -T3 <target>

## Packet Fragmentation  (Firewall)
nmap -f <target>

## Aggressive 
nmap -A <target>

## Verbose
nmap -vv <target>

## Output Normal 
nmap <target> -oN <file.txt> 

## Output XML
nmap <target> -oX <file> 

