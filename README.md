# Crypto App, SDEV245 Midterm

## How to Run
1. Install dependency: `pip3 install cryptography`
2. Run: `python3 crypto_app.py`
3. Enter any message when prompted

## How It Upholds the CIA Triad

**Confidentiality:** The message is encrypted using AES symmetric encryption via the Fernet library. Without the key, the encrypted output is unreadable.

**Integrity:** The message is hashed with SHA-256 before encryption and again after decryption. If the hashes match, the message was not altered. If they differ, tampering is detected.
**Availability:** The script runs locally with no external dependencies beyond the cryptography library, keeping it simple and accessible.

## Entropy and Key Generation
A fresh AES key is generated every time the script runs using `Fernet.generate_key()`, which pulls from the operating system's cryptographically secure random number generator. High entropy in key generation is critical, a predictable or low entropy key can be brute forced. By using the OS level random source, the key is statistically unique and unpredictable each run.