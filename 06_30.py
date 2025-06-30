isim = input("adınız: ")
soyad = input("soyadınız: ")
yas = int(input("yaşınız: "))
urun = input("ne içmek istersiniz: ")
tutar = 70

#print("merhaba " + isim + " " + soyad + ". Yaşınız: " + str(yas) + ". İçecek tercihiniz: " + urun + ".")
#print(f"Merhaba {isim} {soyad}, yaşınız {yas}. İçecek tercihiniz: {urun}. Toplam tutarınız: {tutar}TL")

yasKontrol = yas < 18

print(type(yasKontrol))