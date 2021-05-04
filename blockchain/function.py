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


def listdirectory(): 
    cwd = os.getcwd()
    fichier=[] 
    idfichier=[]
    l = glob.glob(cwd + '/save/*') 
    for i in l: 
        if os.path.isfile(i): 
            elem = i.split("/")
            elem = elem[len(elem)-1]
            fichier.append(elem)
            elem = elem.split(".")[0]
            elem = [int(s) for s in elem.split("_") if s.isdigit()]
            idfichier.append(elem[0])  

    return [idfichier,fichier]