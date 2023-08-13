from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

def encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(ciphertext).decode()

# Example usage
key = input("Enter 16-byte Key: ").encode('utf-8')
plaintext = input("Enter plaintext: ")

encrypted_text = encrypt(key, plaintext)
print("Encrypted Text:", encrypted_text)
