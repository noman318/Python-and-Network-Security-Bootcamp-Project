import hashlib

str = hashlib.sha384(b'Sahikh Noman')

str_hex = str.hexdigest()

print(str_hex)
