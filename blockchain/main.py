import creationBlockchain

blo = creationBlockchain.Block("test")
chainblo = creationBlockchain.Blockchain(blo)
block = creationBlockchain.Block( "test2")
chainblo.addBlock(block)
chainblo.showBlockchain()
print(chainblo.getBlocks()[0].index)