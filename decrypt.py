from cryptography.fernet import Fernet
key = b'DqbtoOEMKXpTsYjm9FFRJOwOXEfUPn5vmUvlOnsx2MY='

fernet = Fernet(key)
  
# opening the encrypted file
with open('info.txt', 'rb') as enc_file:
    encrypted = enc_file.read()
  
# decrypting the file
decrypted = fernet.decrypt(encrypted)
  
# opening the file in write mode and
# writing the decrypted data
with open('info2.txt', 'wb') as dec_file:
    dec_file.write(decrypted)