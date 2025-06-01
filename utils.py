# utils.py
import os
from Crypto.Cipher import AES
from Crypto.Util import Counter

def pad(s):
    pad_len = AES.block_size - len(s) % AES.block_size
    return s.encode() + bytes([pad_len] * pad_len)

def unpad(s):
    return s[:-s[-1]].decode()

def encrypt_ecb(text):
    key = os.urandom(16)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(text))
    
    # cipher decrypt harus dipisah
    cipher_dec = AES.new(key, AES.MODE_ECB)
    decrypted = unpad(cipher_dec.decrypt(ciphertext))
    
    return ciphertext.hex(), decrypted

def encrypt_cbc(text):
    key = os.urandom(16)
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(text))
    
    cipher_dec = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher_dec.decrypt(ciphertext))
    
    return ciphertext.hex(), decrypted

def encrypt_ctr(text):
    key = os.urandom(16)
    iv = os.urandom(16)
    
    # Enkripsi
    ctr = Counter.new(128, initial_value=int.from_bytes(iv, byteorder='big'))
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    ciphertext = cipher.encrypt(text.encode())
    
    # Dekripsi pakai counter baru
    ctr_dec = Counter.new(128, initial_value=int.from_bytes(iv, byteorder='big'))
    cipher_dec = AES.new(key, AES.MODE_CTR, counter=ctr_dec)
    decrypted = cipher_dec.decrypt(ciphertext).decode()
    
    return ciphertext.hex(), decrypted
