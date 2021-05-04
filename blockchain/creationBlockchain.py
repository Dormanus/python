from hashlib import sha256
from datetime import datetime

class Block:
    def __init__(self,  data, hash = None, nonce=0, index = 0, previous_hash = None, timestamp =datetime.now()):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.nonce = nonce
    
    def blockToString(self):
        return str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.data) +  str(self.nonce)

    def showBlock(self):
        print("Block #" + str(self.index) + " [")
        print("     index: " + str(self.index))
        print("     previous hash: " + str(self.previous_hash))
        print("     timestamp: " + str(self.timestamp))
        print("     data: " + str(self.data))
        print("     hash: " + str(self.hash))
        print("     nonce: " + str(self.nonce))
        print("] \n")

        

class Blockchain:
    def __init__(self, block):
        self.__blocks = [compute_hash(block)]
        
        fichier = open("data.txt", "a")
        fichier.write(self.__blocks)
        fichier.close()
    

    def addBlock(self, block):
        size = len(self.__blocks)
        newBlock = Block(block.data)
        newBlock.index = size
        newBlock.previous_hash = self.__blocks[size-1].hash
        self.__blocks.append(compute_hash(newBlock))
    

    def isBlockchainValid(self):
        try:
            if(self.__blocks[0].previous_hash != None):
                return False
            else:
                for b in self.__blocks[1:]:
                    if (b.previous_hash != self.__blocks[b.index - 1].hash):
                        return False
            return True
        except:
            return False 


    def showBlockchain(self):
        print("Blockchain validity: " + str(self.isBlockchainValid()))
        if(self.isBlockchainValid()):
            for b in self.__blocks:
                b.showBlock()

    def getBlocks(self):
        return self.__blocks 


def compute_hash(block):
    n = 0  

    searchHash = sha256(block.blockToString().encode('utf-8')).hexdigest()
    while str(searchHash).find("0000") != 0:
        n += 1
        block.nonce = n
        searchHash = sha256(block.blockToString().encode('utf-8')).hexdigest()

    block.hash = searchHash
    return block


