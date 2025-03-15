

## 1. **Linux Commands**

- **`pwd`**: Print the current working directory.
- **`ls`**: List files and directories.
- **`cd [directory]`**: Change to a specific directory.
- **`mkdir [directory]`**: Create a new directory.
- **`cp [source] [destination]`**: Copy files or directories.
- **`mv [source] [destination]`**: Move or rename files or directories.
- **`rm [file]`**: Remove a file.
- **`rmdir [directory]`**: Remove an empty directory.
- **`cat [file]`**: Display the contents of a file.
- **`echo [text]`**: Print text to the terminal.
- **`top`**: Display system resource usage (CPU, memory).
- **`clear`**: Clear the terminal screen.
- **`exit`**: Exit the terminal session.

- **`ps aux`**: List running processes and their details (useful for spotting suspicious processes).
- **`netstat`**: Display network connections and open ports (helps detect unauthorized access).
- **`find / -name [filename]`**: Search for a specific file or folder on the system.
- **`chmod [permissions] [file]`**: Change file permissions (e.g., secure files).
- **`chown [user] [file]`**: Change file ownership (assign correct user/group).
- **`kill [PID]`**: Terminate a running process by its Process ID (PID).
- **`iptables`**: Set up firewall rules (important for blocking malicious traffic).
- **`sudo [command]`**: Run a command with root privileges (use with caution).
- **`dmesg`**: Display system messages, useful for troubleshooting security issues.

---

## 2. **Windows Commands**

- **`dir`**: List files and directories in the current folder.
- **`cd [directory]`**: Change directory.
- **`mkdir [directory]`**: Create a new directory.
- **`copy [source] [destination]`**: Copy files.
- **`move [source] [destination]`**: Move or rename files.
- **`del [file]`**: Delete a file.
- **`cls`**: Clear the command prompt screen.
- **`exit`**: Close the command prompt session.
- **`echo [text]`**: Print text to the command prompt.

---
- **`tasklist`**: Show a list of running processes (helps identify suspicious ones).
- **`taskkill /PID [PID]`**: Terminate a running process by its Process ID.
- **`netstat`**: Show active network connections (useful for detecting unauthorized connections).
- **`ipconfig`**: Display network configuration (verify network settings).
- **`ping [address]`**: Check network connectivity to a remote host.
- **`net user`**: Display all user accounts on the system (helps identify unauthorized users).
- **`chkdsk`**: Check disk integrity (useful for detecting signs of malware or file system issues).
- **`shutdown`**: Shutdown or restart the system (useful during an incident).
- **`wmic`**: Use Windows Management Instrumentation to query system details and running processes.
- **`systeminfo`**: Display detailed system configuration and OS information.

- **`ping`**: Check network connectivity (Linux & Windows).
- **`netstat`**: Display network connections and open ports (Linux & Windows).
- **`tasklist`** (Windows) / **`ps aux`** (Linux): List running processes (useful for incident response).
- **`chmod`** (Linux) / **`icacls`** (Windows): Change file permissions (Linux) or access control lists (Windows) to secure sensitive files.
- **`kill`** (Linux) / **`taskkill`** (Windows): Terminate malicious processes.
- **`sudo`** (Linux) / **Run as Administrator** (Windows): Run commands with elevated privileges (for system maintenance or security checks).
- **`sfc /scannow`** (Windows): Scan system files for integrity issues, useful for detecting malware or file corruption.
- **`netstat -ano`** (Windows): View network connections with the associated Process IDs (useful for identifying malicious traffic).
- **`whois [domain]`** (Linux): Retrieve domain registration information, useful for investigating phishing or malicious domains.
- **`lsof`** (Linux): List open files, can help track down suspicious files or ports in use.
- **`iptables -L`** (Linux): View the current firewall rules.

