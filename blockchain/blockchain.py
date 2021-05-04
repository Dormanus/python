from datetime import datetime
import os.path
from os import path
cwd = os.getcwd()
import block as b
import function


class Blockchain:

    def saveBlockchainFirst(self, b):
        f = open("save/Blockchain_" + str(self.__id) + ".csv", "a")
        f.write(str(self.isBlockchainValid()) + ";")
        f.write(str(self.__id) + ";")
        f.write(str(b.index) + ";") 
        f.write(str(b.previous_hash)+ ";")
        f.write(str(b.timestamp) + ";")
        f.write(str(b.data) + ";")
        f.write(str(b.hash) + ";")
        f.write(str(b.nonce) + "\n")
        f.close()

    def saveBlockchain(self, b):
        f = open("save/Blockchain_" + str(self.__id) + ".csv", "a")
        f.write(str(self.isBlockchainValid()) + ";")
        f.write(str(self.__id) + ";")
        f.write(str(b.index) + ";") 
        f.write(str(b.previous_hash)+ ";")
        f.write(str(b.timestamp) + ";")
        f.write(str(b.data) + ";")
        f.write(str(b.hash) + ";")
        f.write(str(b.nonce) + "\n")
        f.close()

    def __init__(self, block):
        if(isinstance(block, list)):
            self.__blocks = []
            for bls in block:
                self.__id = int(bls[1][0])
                self.__blocks.append(b.Block(bls))
        else:
            self.__blocks = [function.compute_hash(block)]
            i = 1
            while(path.exists(cwd+"/save/Blockchain_" + str(i) + ".csv")):
                i = i + 1
            self.__id = i
            self.saveBlockchainFirst(block)

    def getId(self):
        return self.__id
    

    def addBlock(self, block):
        size = len(self.__blocks)
        newBlock = b.Block(block.data)
        newBlock.index = size
        newBlock.previous_hash = self.__blocks[size-1].hash
        self.__blocks.append(function.compute_hash(newBlock))
        self.saveBlockchain(newBlock)



    

    def isBlockchainValid(self):
        try:
            if(self.__blocks[0].previous_hash != None and self.__blocks[0].previous_hash != "None"):
                print("1 :"+  str(self.__blocks[0].previous_hash))
                return False
            else:
                for b in self.__blocks[1:]:
                    if (b.previous_hash != self.__blocks[b.index - 1].hash):
                        print("2")
                        return False
            return True
        except:
            print("3")
            return False 


    def showBlockchain(self):
        print("Blockchain validity: " + str(self.isBlockchainValid()))
        if(self.isBlockchainValid() or True):
            for b in self.__blocks:
                b.showBlock()

    def getBlocks(self):
        return self.__blocks 




