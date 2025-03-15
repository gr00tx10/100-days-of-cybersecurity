## What is Hashing?

**Hashing** is the process of converting data into a fixed-length string of characters (the hash). This process is used to verify the integrity of data or store passwords securely. Common hashing algorithms include:

- **MD5**: A widely used hash function but considered insecure.
- **SHA-1**: A stronger hash function than MD5, but still vulnerable to attacks.
- **SHA-256**: A more secure version of SHA-1, widely used in security applications.

Hashes are **one-way** functions, meaning you can create a hash from the original data, but you can't easily revert the hash back to the original data.

---

## What is Salt?

**Salt** is random data added to a password or input before hashing to ensure that even if two identical inputs are hashed, their outputs are different. Salt prevents attackers from using precomputed hash databases (rainbow tables) to easily crack passwords.

- **Salted hashes** make it much harder to crack the hashes by adding randomness.
- Salt is typically stored in the database along with the hash but is never kept secret.

---

## Useful Hash Cracking Tools & Resources

### 1. **CyberChef**
[CyberChef](https://gchq.github.io/CyberChef/) is a web-based tool that provides a variety of cryptographic functions. It can be used to **hash** and **decrypt** data, and also includes a **hash cracking** feature for known hash algorithms.

### 2. **CrackStation**
[CrackStation](https://crackstation.net) is an online hash cracking tool that uses precomputed hash databases (rainbow tables) to crack hashed passwords.

### 3. **Hashcat**
[Hashcat](https://hashcat.net/hashcat/) is a powerful password cracking tool that can crack various hash types using **brute force** and **dictionary attacks**.

### 4. **John the Ripper**
[John the Ripper](https://www.openwall.com/john/) is a popular password cracking tool that supports many different hashing algorithms. It is commonly used for testing password security.

---

## Common Hash Types

- **MD5**
- **SHA-1**
- **SHA-256**
- **bcrypt**
- **base64**

## Important Dirs

  | **OS**        | **File**            | **Key Points**                                            |
|---------------|---------------------|-----------------------------------------------------------|
| **Linux**     | `/etc/passwd`        | User info (no password hashes)                            |
|               | `/etc/shadow`        | Password hashes and security data, root access only       |
| **Windows**   | **SAM**              | Password hashes (NTLM), only accessible by SYSTEM         |
|               | **SECURITY**         | Security policies, group memberships                      |
|               | **SYSTEM**           | System settings and configuration    


