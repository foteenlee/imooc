from Crypto.PublicKey import RSA

key = RSA.generate(2048)
print(key.export_key().decode())