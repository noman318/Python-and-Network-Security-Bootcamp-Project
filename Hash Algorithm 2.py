import hashlib

str = hashlib.shake_128(b'Sahikh Noman')

str_hex = str.hexdigest(50)

print(str_hex)
