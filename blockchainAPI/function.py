from hashlib import sha256
import glob 
import os.path 

def compute_hash(block):
    n = 0  

    searchHash = sha256(block.blockToString().encode('utf-8')).hexdigest()
    while str(searchHash).find("0000") != 0:
        n += 1
        block.nonce = n
        searchHash = sha256(block.blockToString().encode('utf-8')).hexdigest()

    block.hash = searchHash
    return block

