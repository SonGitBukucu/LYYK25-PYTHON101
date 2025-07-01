isim = input("adınız: ")
soyad = input("soyadınız: ")
yas = int(input("yaşınız: "))
urun = input("ne içmek istersiniz: ")
urunSayi = int(input("kaç tane içecek istiyorsunuz: "))
tutar = 70

#print("merhaba " + isim + " " + soyad + ". Yaşınız: " + str(yas) + ". İçecek tercihiniz: " + urun + ".")
print(f"Merhaba {isim} {soyad}, yaşınız {yas}. İçecek tercihiniz: {urun}. Toplam tutarınız: {urunSayi}*{tutar} = {tutar*urunSayi}TL")

yasKontrol = yas < 18

print(type(yasKontrol))