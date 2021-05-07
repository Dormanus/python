
from datetime import datetime

class Block:
    def __init__(self,  film, producer, release_year, hash = None, nonce=0, id = 0, previous_hash = None, timestamp =datetime.now()):
        self.id = id
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.film = film
        self.producer = producer
        self.release_year = release_year
        self.hash = hash
        self.nonce = nonce


        
    
    def blockToString(self):
        return str(self.id) + str(self.previous_hash) + str(self.timestamp) + str(self.film) + str(self.producer) + str(self.release_year) +  str(self.nonce)

        