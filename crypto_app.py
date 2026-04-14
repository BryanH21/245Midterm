import hashlib
from cryptography.fernet import Fernet

# Generate a fresh key each run
key = Fernet.generate_key()
cipher = Fernet(key)


def hash_message(message):
    return hashlib.sha256(message.encode()).hexdigest()


def encrypt_message(message):
    return cipher.encrypt(message.encode())


def decrypt_message(encrypted):
    return cipher.decrypt(encrypted).decode()


def main():
    print(" Crypto App ")
    message = input("Enter a message to encrypt: ")

    # Hash original
    original_hash = hash_message(message)
    print(f"\nOriginal SHA-256 Hash: {original_hash}")

    # Encrypt
    encrypted = encrypt_message(message)
    print(f"Encrypted: {encrypted}")

    # Decrypt
    decrypted = decrypt_message(encrypted)
    print(f"Decrypted: {decrypted}")

    # Verify integrity
    decrypted_hash = hash_message(decrypted)
    print(f"\nDecrypted SHA-256 Hash: {decrypted_hash}")

    if original_hash == decrypted_hash:
        print("Integrity verified, hashes match!")
    else:
        print("Integrity check failed, hashes do not match!")


main()
