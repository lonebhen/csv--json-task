import hashlib

#this function calculates and returns the sha256 code in hexadecimal of the given json 

def calculate(filename):
    sha256_hash = hashlib.sha256()
    with open(filename,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()