
from datetime import datetime

class Block:
    def __init__(self,  values, hash = None, nonce=0, index = 0, previous_hash = None, timestamp =datetime.now()):
        if(isinstance(values, list)):
            self.index = int(values[2])
            self.previous_hash = values[3]
            self.timestamp = values[4]
            self.data = values[5]
            self.hash = values[6]
            self.nonce = int(values[7])
        else : 
            self.index = index
            self.previous_hash = previous_hash
            self.timestamp = timestamp
            self.data = values
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

        