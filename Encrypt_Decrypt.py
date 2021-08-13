"""Code by IAS/Sénégal"""
from cryptography.fernet import Fernet
def encrypt_decrypt(message):
    # we will be encryting the below string.
    message = message
    # generate a key for encryptio and decryption
    # You can use fernet to generate 
    # the key or use random key generator
    # here I'm using fernet to generate key
    
    key = Fernet.generate_key()
    with open("k.key", "wb") as key_file:
        key_file.write(key)
    def load_key():
        """
        Loads the key from the current directory named `key.key`
        """
        return open("k.key", "rb").read()
    # Instance the Fernet class with the key
    # Instance the Fernet class with the key
    
    fernet = Fernet(load_key())
    
    # then use the Fernet class instance 
    # to encrypt the string string must must 
    # be encoded to byte string before encryption
    encMessage = fernet.encrypt(message.encode())
    
    print("original string: ", message)
    print("encrypted string: ", encMessage)
    
    # decrypt the encrypted string with the 
    # Fernet instance of the key,
    # that was used for encrypting the string
    # encoded byte string is returned by decrypt method,
    # so decode it to string with decode methos
    decMessage = fernet.decrypt(encMessage).decode()
    
    return decMessage