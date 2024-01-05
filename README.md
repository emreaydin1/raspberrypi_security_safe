Bilgisayar Donanımı dersi kapsamında yapılan Raspberry Pi Projesi.

Bu proje değerli eşyalarını güvende tutmak isteyen kişiler için tasarlanmış bir güvenlik sistemdir. 
Projenin ismi, Raspberry Pi Security Safe’ dir. Bu güvenlik sisteminde Raspberry Pi Model 3B kullanılmıştır.
Projeye dışarıdan bakıldığında kapağının üzerinde üç adet farklı renklerde led ve RFID-RC522 modülü bulunan bir dolap görülmektedir.
Bu dolabın içinde eşyaların konulacağı bir kasa bulunmaktadır.Kasanın güvenlik sistemi devredeyken dolap kapağının üzerinde bulunan sarı renkli led yanıp söner. 
RFID modülüne kasa sahibi tanımlanmış kartını okuttuğunda güvenlik sistemi devre dışı kalır ve yeşil renkli led yanar. 
RFID modülüne tanımlanan kart okutulmadan kasanın bulunduğu dolabın kapağı açılırsa pır sensörü hareketi algılar, buzzer ses çıkartır ve kırmızı renkli led yanar. 
Ayrıca kasa sahibinin e-mail adresine: “17.12.2022 tarihinde, 12:40:50 saatinde kasanıza izinsiz giriş tespit edilmiştir.” şeklinde bir uyarı mesajı yollanır. 
Tüm bu sistemin işleyişi Python programlama diliyle yazılan kodlarla Raspberry Pi tarafından yürütülmektedir.
