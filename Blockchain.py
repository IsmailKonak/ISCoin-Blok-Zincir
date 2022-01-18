import hashlib
import time
from ast import literal_eval as todict

class Block():

    def __init__(self, block_num, data, prev_hash, time, miner, nonce):
        self.block_num = block_num
        self.data = data
        self.prev_hash = prev_hash
        self.time = time or time.time()
        self.miner = miner
        self.nonce = nonce

    def info(self):
        return {"block_num": self.block_num, "data":self.data, "prev_hash": self.prev_hash,
                "time": self.time, "miner": self.miner, "nonce": self.nonce}


class Blockchain_of_IScoin():

    def __init__(self):
        self.chain = []
        self.construct_genesis()    

    def construct_genesis(self):
        block = Block(block_num=len(self.chain),data=None, prev_hash="0"*64,                                                                               
                      time=time.ctime(), miner= "IRONISM", nonce=0).info()
        
        self.chain.append(str(block))

    def mining(self,data, miner_id):
        difficulty = 5
        maxnonce = 100000000000
        prev_hash = self.last_hash()
        for nonce in range(maxnonce):
            
            block = Block(block_num=len(self.chain), data=data, prev_hash=prev_hash, time=time.ctime(),
                          miner= miner_id, nonce=nonce).info()
            
            hash_of_block = hashlib.sha256(str(block).encode("ascii")).hexdigest()
            
            if hash_of_block.startswith("0"*difficulty):
                print(f" Deneme sayısı: {nonce}")
                print(f"Kazım başarılı !!! Kazılan bloğun hash'i': '{hash_of_block}'")
                self.chain.append(block)
                break

    def info(self):
        print(f"Blok zincir yüksekliği: {len(self.chain)}")
        print("Geliştirici: Ismail Konak")

    def chain(self):
        return self.chain

    def last_block(self):
        last_block = self.chain[-1]
        if type(last_block) == dict:
            return last_block
        
        elif type(last_block) != dict:    
            last_block = todict(last_block)
            return last_block
        
    def chsd_block(self,block_num):
        last_block = self.chain[block_num]
        if type(last_block) == dict:
            return last_block
        
        elif type(last_block) != dict:    
            last_block = todict(last_block)
            return last_block

    def last_hash(self):
        last_block = self.chain[-1]
        hash_block = hashlib.sha256(str(last_block).encode("ascii")).hexdigest()
        return hash_block

    def last_transaction(self):
        last_block = self.chain[-1]
        if type(last_block) == dict:
            trans_dict = last_block["data"]
            return f"{trans_dict['sender']} sent {trans_dict['quantity']} ISCoin to {trans_dict['receiver']}."
        
        elif type(last_block) != dict:    
            last_block = todict(last_block)
            trans_dict = last_block["data"]
            return f"{trans_dict['sender']} sent {trans_dict['quantity']} ISCoin to {trans_dict['receiver']}."
        

    def last_sender(self):
        last_block = self.chain[-1]
        if type(last_block) == dict:
            trans_dict = last_block["data"]
            return trans_dict['sender']
        
        elif type(last_block) != dict:    
            last_block = todict(last_block)
            trans_dict = last_block["data"]
            return trans_dict['sender']

    def last_quantity(self):
       last_block = self.chain[-1]
       if type(last_block) == dict:
           trans_dict = last_block["data"]
           return trans_dict['quantity']
        
       elif type(last_block) != dict:    
           last_block = todict(last_block)
           trans_dict = last_block["data"]
           return trans_dict['quantity']

    def last_receiver(self):
       last_block = self.chain[-1]
       if type(last_block) == dict:
           trans_dict = last_block["data"]
           return trans_dict['receiver']
        
       elif type(last_block) != dict:    
           last_block = todict(last_block)
           trans_dict = last_block["data"]
           return trans_dict['receiver']

