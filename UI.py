# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 20:00:00 2022

@author: ismail
"""

from Blockchain import Block, Blockchain_of_IScoin
from Wallet import Wallet
import time

print(
"""
*******************************************************************************
*                                                                             *  
*                                                                             * 
*                                                                             *
*                       BLOK ZİNCİRE HOŞ GELDİNİZ                             *
*                                                                             *
*                                                                             *
*                                                                             *
*                                                 Bu blok zincir Ismail Konak *
*                                                  tarafından hazırlanmıştır  *
*******************************************************************************                    
      """)
blockchain = Blockchain_of_IScoin()
wallet = Wallet()
Run = True
while Run:
    operation_mode= int(input("""
                 
    1) Kazım yapmak
    2) Cüzdan işlemleri
    3) Blok zincir işlemleri                                             
    0) Çık                                                                
    --- Hangi işlemi gerçekleştirmek istiyorsunuz?                            
            
                --> """))
    
    if operation_mode == 1:
        miner_id = input(" Kazıcı kimlik numaranız: ")
        print("\n")
        print(" Blok verisi")
        sender = input("   i) Gönderen:")
        receiver = input("   ii) Alan:")
        quantity = int(input("   iii) Miktar:"))
        print("\n")
        print("**************** Kazım işlemi başladı ********************* \n \n")
        data = {"sender":sender,"receiver":receiver,"quantity":quantity}
        print(str(data)+"\n")
        b_time = time.time()
        blockchain.mining(data,miner_id)
        e_time = time.time()
        
        wallet.earn_coin(miner_id,3.14)
        print("\n")
        blockchain.info() 
        print("\n")
        print("3.14 ISCoin kazanıldı")
        print("Kazım süresi: "+str(e_time-b_time)+" sn")
        print("**************** Kazım işlemi sonlandı *********************")
        
        
    elif operation_mode == 2:
        while True:
            print(" Cüzdan işlemleri")
            op = int(input("""
                     
        1) Kazıcı ekle
        2) Kazıcı çıkar
        3) Kazıcı hakkında bilgi 
        4) Veri tabanındaki kazıcılar
        0) Ana menü                                                                
        --- Hangi işlemi gerçekleştirmek istiyorsunuz?                            
                
                    --> """))
            if op == 1:
                miner = input("Kullanıcı adınızı seçiniz: ")
                miner_id = wallet.add_miner(miner)
                print("Kazıcı kullanıcı adınız: "+miner)
                print("Kazıcı kimlik numaranız: "+miner_id )
                print("Bu kazıcı kimlik numarası, ISCoin kazımı ve cüzdan işlemleri için gerekecek, kaybetmeyiniz.")
            elif op == 2:
                miner_id = input("Kazıcı kimlik numarası: ")
                wallet.remove_miner(miner_id)
            elif op == 3:
                miner_id = input("Kazıcı kimlik numarası: ")
                wallet.miner_info(miner_id)
            elif op == 4:
                wallet.miners()
            elif op == 0:
                break
    
            
    elif operation_mode == 3:
        while True:
            print(" Blok zincir işlemleri")
            op = int(input("""
                         
            1) Blok zincir hakkında bilgi
            2) Son blok hakkında bilgi
            3) Blok bilgisi
            0) Ana menü                                                                
            --- Hangi işlemi gerçekleştirmek istiyorsunuz?                            
                    
                        --> """))
            if op == 1:
                blockchain.info()
            
            elif op == 2 :
                last_block = blockchain.last_block()
                
                sender = last_block["data"]["sender"]
                receiver = last_block["data"]["receiver"]
                quantity = last_block["data"]["quantity"]
                date = last_block["time"]
                nonce = last_block["nonce"]
                miner = last_block["miner"]
                block_num = last_block["block_num"]
                prev_hash = last_block["prev_hash"]
                
                print(" Blok numarası: "+str(block_num))
                print(" Gönderen: "+sender)
                print(" Alan: "+receiver)
                print(" Miktar: "+str(quantity))
                print(" Kazılma tarihi: "+ str(date))
                print(" Nonce: "+ str(nonce))
                print(" Önceki hash: "+ prev_hash)
            
            elif op == 3:
                block_num = int(input("Blok numarası: "))
                last_block = blockchain.chsd_block(block_num)
                if last_block == None:
                    print("Seçili blok henüz kazılmamış.")
                else:
                    sender = last_block["data"]["sender"]
                    receiver = last_block["data"]["receiver"]
                    quantity = last_block["data"]["quantity"]
                    date = last_block["time"]
                    nonce = last_block["nonce"]
                    miner = last_block["miner"]
                    block_num = last_block["block_num"]
                    prev_hash = last_block["prev_hash"]
                    
                    print(" Blok numarası: "+str(block_num))
                    print(" Gönderen: "+sender)
                    print(" Alan: "+receiver)
                    print(" Miktar: "+str(quantity))
                    print(" Kazılma tarihi: "+ str(date))
                    print(" Nonce: "+ str(nonce))
                    print(" Önceki hash: "+ prev_hash)
            elif op == 0:
                break
            
    elif operation_mode == 0:
        break


