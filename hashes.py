import hashlib
hash_object=hashlib.sha224(b'hello world')
hash_object=hashlib.sha256(b'hello world')
hash_object=hashlib.sha384(b'hello world')
hex_dig=hash_object.hexdigest()
print(hex_dig)