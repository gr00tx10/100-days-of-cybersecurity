# Operating System Fundamentals: Linux and Windows for Cybersecurity

## Common Security Tasks:
- User management (`useradd`, `passwd`)
- File permissions (`chmod`, `chown`)
  
## Read(r)= 4 | Write(w)= 2 | Execute(x)= 1
- chmod 777 -Full
- chmod 421 -Owner(4), Group(2), Others(1)
---
- Firewall (`iptables`, `ufw`)
- Log monitoring (`syslog`)

## File Systems:
- **Ext4**: Most common Linux file system.
- **XFS**: High-performance file system used in enterprise environments.
- **Btrfs**: Modern file system supporting snapshots and volume management.
- 
## 2. **Windows for Cybersecurity**
### File Systems:
- **NTFS (New Technology File System)**: Default file system for modern Windows systems, supporting file permissions and encryption.
- **FAT32**: Older file system, limited to 4GB file sizes.
- **exFAT**: Used for larger file sizes and external drives.


## 1. **Linux File Systems and Key Directories**

### File Systems:
- **Ext4**: The default file system for most Linux distributions, known for stability and performance.
- **XFS**: A high-performance file system often used in enterprise environments.
- **Btrfs**: A newer file system with features like snapshots and volume management.

### Key Directories in Linux:
- **/root**: The home directory for the **root** (superuser) account. It has full privileges over the system.
- **/var**: Contains variable data, such as logs, spools, caches, and temporary files. Includes important directories like:
  - **/var/log**: Logs (important for security auditing).
  - **/var/www**: Web server files.
- **/home**: Contains user-specific data and configurations (e.g., `/home/user`).
- **/etc**: System configuration files (e.g., `/etc/passwd` for user data, `/etc/ssh/sshd_config` for SSH config).
- **/bin**: Contains essential command binaries (e.g., `ls`, `cp`, `mv`).
- **/lib**: Holds shared libraries essential for system functions.
- **/tmp**: Temporary files used by applications, usually deleted on reboot.
- **/dev**: Device files (e.g., `/dev/sda` for disk drives).
- **/mnt**: Temporary mount points for file systems.

## 2. **Windows File Systems and Key Directories**

### File Systems:
- **NTFS (New Technology File System)**: The default file system for Windows, supporting file permissions and encryption.
- **FAT32**: Older file system, supports drives up to 2TB and individual files up to 4GB.
- **exFAT**: A more modern alternative to FAT32, used for larger external drives.

### Key Directories in Windows:
- **C:\**: The main system drive, typically where Windows is installed.
- **C:\Windows**: Contains system files, executables, and operating system files. Important subdirectories:
  - **C:\Windows\System32**: System files, libraries, and executables.
  - **C:\Windows\Temp**: Temporary files created by the system and applications.
  - **C:\Program Files**: Installed software programs (e.g., `C:\Program Files\Microsoft Office`).
  - **C:\Users**: Contains user profiles and directories, e.g., `C:\Users\JohnDoe`.
- **C:\ProgramData**: Stores application data that is not user-specific, like settings for installed programs.
- **C:\Documents and Settings** (Older versions of Windows): A legacy directory used to store user profiles.
- **C:\Recycled (Recycle Bin)**: Stores deleted files until they are permanently removed.

### Key Files:
- **/etc/passwd**: Contains user account information including the username, user ID (UID), group ID (GID), home directory, and the login shell. **(No longer stores passwords by default)**.
- **/etc/shadow**: Stores hashed user passwords. This file is readable only by the root user, making it more secure. The password field in **/etc/shadow** contains the hashed password or a placeholder like `*` or `!!` if no password is set.
  - **Example**:
  **C:\Windows\System32\config\SAM**: The primary file where Windows stores the password hashes. This file is not accessible while the system is running (it's locked).
  - **Note**: The file is protected by a lock during regular operation to prevent tampering.



