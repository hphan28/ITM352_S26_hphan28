from cryptography.fernet import Fernet


key = Fernet.generate_key()
print(f"Encryption Key: {key}\n")


cipher_suite = Fernet(key)


user_message = input("Enter a message to encrypt: ")
print()

encoded_message = user_message.encode()
print(f"Step 1 - String encoded to bytes: {encoded_message}")

encrypted_text = cipher_suite.encrypt(encoded_message)
print(f"Step 2 - Encrypted (unreadable): {encrypted_text}")
print()

decrypted_bytes = cipher_suite.decrypt(encrypted_text)
print(f"Step 3 - Decrypted (still bytes): {decrypted_bytes}")

decrypted_message = decrypted_bytes.decode()
print(f"Step 4 - Decoded to string: {decrypted_message}")



