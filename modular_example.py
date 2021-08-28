from cryptography.fernet import Fernet

key = b'DqbtoOEMKXpTsYjm9FFRJOwOXEfUPn5vmUvlOnsx2MY='

fernet = Fernet(key)
val = b'gAAAAABhKqyKrqOSza4x-xRDUy-0B4qVeZq-153pDn2I6eny4I-2r01OWyp0vcDWREII_cLgWCTGJ1do-nP-kPYyQZKk7w3vBO19DjNZWgzJ2Fvan1c1fqQ='
decrypted = fernet.decrypt(val).decode()
print(decrypted)