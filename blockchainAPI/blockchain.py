from datetime import datetime
import block as b
import function
import sqlite3





def addBlock(block, last_id, last_hash):
    if(last_hash):
        size = last_id +1
        block.id = size
        block.previous_hash = last_hash
        block = function.compute_hash(block)
        return block
    

def isBlockchainValid():
    co = sqlite3.connect('tables/tables.db')
    cur = co.cursor()
    r = cur.execute('select * from films').fetchall()    
    if(r[0][1] != None and r[0][1] != "None"):
        return False
    else:
        for b in r[1:]:
            if (b[1] != r[b[0] - 1][6]):
                return False
    return True

