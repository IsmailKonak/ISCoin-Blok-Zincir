# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 11:29:51 2022

@author: ismail
"""

import pickle
from os.path import exists
import hashlib
import time

class Wallet:
    
    def __init__(self):
        self.dt = self.database()
        
    def database(self):
        if exists("database.pkl") == True:
            database = pickle.load(open("database.pkl","rb"))
            return database
        else:
            database = open("database.pkl","wb")
            miners = []
            pickle.dump(miners,database)
            database.close()
            database = pickle.load(open("database.pkl","rb"))
            return database
        
    def add_miner(self,miner):
        miner_hash = hashlib.sha256(str(miner).encode()).hexdigest()
        add = True
        for miner in self.dt:
            if miner["miner_id"] == miner_hash:
                print("Bu kullanıcı zaten veri tabanında kayıtlı.")
                add = None
        if add == True:
            miner_profile = {"miner_name":miner, "miner_id":miner_hash, "last_activity": time.ctime(), "quantity": 0}
            self.dt.append(miner_profile)
            dat = open("database.pkl","wb")
            pickle.dump(self.dt,dat)
            dat.close()
            self.dt = self.database()
            return miner_hash
        else: 
            pass
        
    def remove_miner(self,miner_id):
        pos = -1
        for miner in self.dt:
            pos += 1
            if miner["miner_id"] == miner_id:
                self.dt.pop(pos)
                print(" Kazıcı veri tabanından kaldırılmıştır")
                dat = open("database.pkl","wb")
                pickle.dump(self.dt,dat)
                dat.close()
                self.dt = self.database()
                break
    
    def miners(self):
        for miner in self.dt:
            print(" "+str(miner)+"\n")
            
    def miner_info(self,miner_id):
        for miner in self.dt:
            if miner["miner_id"] == miner_id:
                print("Kazıcı kullanıcı adı: "+miner["miner_name"])
                print(" Kazıcı kimlik numarası: "+ miner["miner_id"])
                print(" En son aktivite tarihi: "+miner["last_activity"])
                print(" Miktar (ISCoin): "+str(miner["quantity"]))
     
    def earn_coin(self, miner_id,quantity):
        for miner in self.dt:
            if miner["miner_id"] == miner_id:
                miner["quantity"] = miner["quantity"] + quantity
        dat = open("database.pkl","wb")
        pickle.dump(self.dt,dat)
        dat.close()
        self.dt = self.database()
        