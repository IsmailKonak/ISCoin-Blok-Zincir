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

    1) Kazım yapmak
    2) Cüzdan işlemleri
    3) Blok zincir işlemleri                                             
    0) Çık                                                                
    --- Hangi işlemi gerçekleştirmek istiyorsunuz?                            
            
                --> 2
```

Yeni kazıcı kaydı için 1. seçeneği seçiyoruz<br /><br />

```bash
 Cüzdan işlemleri

        1) Kazıcı ekle
        2) Kazıcı çıkar
        3) Kazıcı hakkında bilgi 
        4) Veri tabanındaki kazıcılar
        0) Ana menü                                                                
        --- Hangi işlemi gerçekleştirmek istiyorsunuz?                            
                
                    --> 1 
```

Kazıcı kullanıcı adımızı giriyoruz, sistemin bize verdiği şifrelenmiş kimliği kaydediyoruz, bu kazıcı kimliğini kazım yaparken kullanacağız.

```bash
Kullanıcı adınızı seçiniz: IRONISM

Kazıcı kullanıcı adınız: IRONISM
Kazıcı kimlik numaranız: a932734233079fd6faacb85f6b40f409924537be31897d8d264b942cdddf6ba1
Bu kazıcı kimlik numarası, ISCoin kazımı ve cüzdan işlemleri için gerekecek, kaybetmeyiniz.
```
Buradan sonra ana menüye gidiyoruz ve Mining işlemi için bu sefer 1 seçeneği seçiyoruz

```bash

    1) Kazım yapmak
    2) Cüzdan işlemleri
    3) Blok zincir işlemleri                                             
    0) Çık                                                                
    --- Hangi işlemi gerçekleştirmek istiyorsunuz?                            
            
                --> 1
```

Bu aşamada kazacağımız bloğun bilgilerini giriyoruz:
> Kazıcı kimliğiniz: (Az önce aldığınız kazıcı kimliğini giriniz)

> i) Sender: (İstediğiniz bir isim)

> ii) Receiver: (İstediğiniz bir isim)

> iii) Quantity: (İstediğiniz bir rakam)

```bash
Kazıcı kullanıcı adınız: a932734233079fd6faacb85f6b40f409924537be31897d8d264b942cdddf6ba1


 Blok verisi

   i) Gönderen: Blockchain

   ii) Alan: Ismail

   iii) Miktar: 6
```
Bı kısmı çalıştırdığınızda kazım işlemi başlayacaktır ve yaklaşık 30 saniye sonra bloğunuz blok zincire eklenecektir.

```bash
**************** Kazım işlemi başladı ********************* 
 

{'sender': 'il', 'receiver': 'il', 'quantity': 6}

Deneme sayısı: 586068
Kazım başarılı !!! Kazılan bloğun hash'i: '00000267a6d4242d94860bbe306b8f70451fbf6d8e31ab6462280c60bd2f818f'


Blok zincir yüksekliği: 2
Geliştirici: Ismail Konak


3.14 ISCoin kazanıldı
Kazım süresi: 24.823636293411255 sn
**************** Kazım işlemi sonlandı *********************
```

Bu kazım işlemi sonucunda cüzdanınıza sistem tarafından 5 ISCoin eklendi. Kazım işlemi 24 saniye sürdü, blok zincirimizin kazım sonrası uzunluğu 2 bloka çıktı.

Kazım işlemi sona erdi. <br /><br />

### **Cüzdan işlemleri**

Cüzdan işlemleri için arayüz üzerinden cüzdan işlemleri seçeneğini seçiyoruz

```bash

    1) Kazım yapmak
    2) Cüzdan işlemleri
    3) Blok zincir işlemleri                                             
    0) Çık                                                                
    --- Hangi işlemi gerçekleştirmek istiyorsunuz?                            
            
                --> 2
```

Bu bölümde:
> {1} Yeni kazıcı kaydı yapıpı kazıcı kimliği almak için seçiniz

> {2} Sistemde kayıtlı bir kazıcıyı silmek için seçiniz

> {3} Kazıcı cüzdanına ulaşmak için seçiniz (Yaptığınız kazımlar sonucunda kazandığınız token miktarını burada görebilirsiniz) 

> {4} Sistemde kayıtlı tüm kazıcıları görmek için tıklayınız

```bash
 Cüzdan işlemleri

        1) Kazıcı ekle
        2) Kazıcı çıkar
        3) Kazıcı hakkında bilgi 
        4) Veri tabanındaki kazıcılar
        0) Ana menü                                                                
        --- Hangi işlemi gerçekleştirmek istiyorsunuz?                            
                
                    -->
```
<br />
<br />

### **Blok Zincir sorgulaması**

Blok zincir sorgulaması için arayüz üzerinden "Blok zincir işlemleri" seçeneğini seçiyoruz

```bash

    1) Kazım yapmak
    2) Cüzdan işlemleri
    3) Blok zincir işlemleri                                             
    0) Çık                                                                
    --- Hangi işlemi gerçekleştirmek istiyorsunuz?                            
            
                --> 3
```
Bu bölümde:
> {1} Yeni kazıcı kaydı yapıpı kazıcı kimliği almak için seçiniz

> {2} Sistemde kayıtlı bir kazıcıyı silmek için seçiniz

> {3} Kazıcı cüzdanına ulaşmak için seçiniz (Yaptığınız kazımlar sonucunda kazandığınız token miktarını burada görebilirsiniz) 


```bash
Blok zincir işlemleri


            
            1) Blok zincir hakkında bilgi
            2) Son blok hakkında bilgi
            3) Blok bilgisi
            0) Ana menü                                                                
            --- Hangi işlemi gerçekleştirmek istiyorsunuz?                            
                    
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
