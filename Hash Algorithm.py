import hashlib
# showhash librarys all the algo avilable in the system
# print(hashlib.algorithms_available)

# print(hashlib.algorithms_guaranteed)
# showhash librarys all the algo avilable in Hash Lib Library

hashed_String = hashlib.sha224(b"Hello Shaikh Noman")

hex_digest = hashed_String.hexdigest()
print(hashed_String)
print(hex_digest)
