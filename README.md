# ISCoin / Blok Zincir 
 
 *Bitcoin tabanlı, ticari amaç gütmeyen, blok zincir teknolojisini öğrenim sürecinde eğitim amaçlı geliştirdiğim basit bir kripto para projesi*

 ---

## ISCoin nedir?
<br />

ISCoin, benim blok zincir ve kripto para dünyasını öğrenme sürecimde konuya hakimiyetimi artırmak için geliştirmiş olduğum, bitcoin altyapısını kullanan, basit, güvenliksiz bir kripto para projesidir.

---
## Dosyalar ve İçerikleri
<br />

`Blockchain.py` : Blockchain ve kazım işlemleri ile ilgili fonksiyonları ve classları içerir.

`Wallet.py` : Mining işlemi ve mining sonucunda kazıcının ödüllendirilmesi ile ilgili fonksiyonları ve class'ları içerir.

`UI.py` : Blockchainin kullanılabilmesi ve mining işleminin yapılabilmesi için hazırlanmış bir arayüz.
<br /><br />

---
## Kullanım
<br />
Yapacağımız tüm işlemleri arayüz aracılığı ile yapacağımız için ilk olarak komut satırında `UI.py` adlı dosyayı çalıştırın.

```bash
python UI.py
```
<br />

### **Kazım Yapmak**:

Kazıcı kaydımızı yapıp, bir kazıcı kimliği edinmek için bir defalığa mahsus arayüz üzerinden cüzdan işlemleri bölümünü seçiyoruz.

```bash

    1) Mining ISCoin
    2) Wallet operations
    3) Blockchain operations
    0) Quit
    --- Which operation want you to do ?

                --> 2
```

Yeni kazıcı kaydı için 1. seçeneği seçiyoruz<br /><br />

```bash
 Wallet Operations

        1) Add miner
        2) Remove miner
        3) Get miner information
        4) Miners in database
        0) Main Menu                                                                
        --- Which operation want you to do ?                                      
                    --> 1 
```

Kazıcı kullanıcı adımızı giriyoruz, sistemin bize verdiği şifrelenmiş kimliği kaydediyoruz, bu kazıcı kimliğini kazım yaparken kullanacağız.

```bash
Choose your username: IRONISM

Your miner id is: a932734233079fd6faacb85f6b40f409924537be31897d8d264b942cdddf6ba1
This miner id will allow you to mine ISCoin and make wallet operations, keep it safe.
```
Buradan sonra ana menüye gidiyoruz ve Mining işlemi için bu sefer 1 seçeneği seçiyoruz

    1) Mining ISCoin
    2) Wallet operations
    3) Blockchain operations                                             
    0) Quit                                                                
    --- Which operation want you to do ?                            
                
                --> 1

Bu aşamada kazacağımız bloğun bilgilerini giriyoruz:
> Kazıcı kimliğiniz: (Az önce aldığınız kazıcı kimliğini giriniz)

> i) Sender: (İstediğiniz bir isim)

> ii) Receiver: (İstediğiniz bir isim)

> iii) Quantity: (İstediğiniz bir rakam)

```bash
Your miner ID: a932734233079fd6faacb85f6b40f409924537be31897d8d264b942cdddf6ba1


 Block Data

   i) Sender: Blockchain

   ii) Receiver:Ismail

   iii) Quantity:6
```
Bı kısmı çalıştırdığınızda kazım işlemi başlayacaktır ve yaklaşık 30 saniye sonra bloğunuz blok zincire eklenecektir.

```bash
**************** Mining process starts ********************* 
 

{'sender': 'il', 'receiver': 'il', 'quantity': 6}

Try number: 586068
Mining Succesfull !!! The current hash of the block is '00000267a6d4242d94860bbe306b8f70451fbf6d8e31ab6462280c60bd2f818f'


Blockchain Height: 2
Creater: Ismail Konak


Earned 31 ISCoin
Duration: 24.823636293411255 sec
**************** Mining process ended *********************
```

Bu kazım işlemi sonucunda cüzdanınıza sistem tarafından 5 ISCoin eklendi. Kazım işlemi 24 saniye sürdü, blok zincirimizin kazım sonrası uzunluğu 2 bloka çıktı.

Kazım işlemi sona erdi. <br /><br />

### **Cüzdan işlemleri**

Cüzdan işlemleri için arayüz üzerinden cüzdan işlemleri seçeneğini seçiyoruz

```bash

    1) Mining ISCoin
    2) Wallet operations
    3) Blockchain operations
    0) Quit
    --- Which operation want you to do ?

                --> 2
```

Bu bölümde:
> {1} Yeni kazıcı kaydı yapıpı kazıcı kimliği almak için seçiniz

> {2} Sistemde kayıtlı bir kazıcıyı silmek için seçiniz

> {3} Kazıcı cüzdanına ulaşmak için seçiniz (Yaptığınız kazımlar sonucunda kazandığınız token miktarını burada görebilirsiniz) 

> {4} Sistemde kayıtlı tüm kazıcıları görmek için tıklayınız

```bash
 Wallet Operations

        1) Add miner
        2) Remove miner
        3) Get miner wallet
        4) Miners in database
        0) Main Menu                                                                
        --- Which operation want you to do ?                                      
                    -->
```
<br />
<br />

### **Blok Zincir sorgulaması**

Blok zincir sorgulaması için arayüz üzerinden "Blok zincir işlemleri" seçeneğini seçiyoruz

```bash

    1) Mining ISCoin
    2) Wallet operations
    3) Blockchain operations
    0) Quit
    --- Which operation want you to do ?

                --> 3
```
Bu bölümde:
> {1} Yeni kazıcı kaydı yapıpı kazıcı kimliği almak için seçiniz

> {2} Sistemde kayıtlı bir kazıcıyı silmek için seçiniz

> {3} Kazıcı cüzdanına ulaşmak için seçiniz (Yaptığınız kazımlar sonucunda kazandığınız token miktarını burada görebilirsiniz) 


```bash
Blockchain Operations


            
            1) Blockchain information
            2) Last block information
            3) Block information
            0) Main Menu                                                                
            --- Which operation want you to do ?                            
                        
                        --> 
```

<br >

---

## İletişim için:
<br>
Mail: i_konak@hotmail.com
<br><br> 

Linkdin: [İsmail Konak](https://www.linkedin.com/in/ismail-konak-0b4339208/)
<br><br> 
Instragram: [@ironism314](https://www.instagram.com/ironism314/)
<br>
<br> 
Twitter: [@ironism314](https://twitter.com/ironism314)
