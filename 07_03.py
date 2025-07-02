""" sıfır girilene kadar girilen değerleri toplayıp yazdır
x = int(input("bir sayı girin: "))

a = x

while x != 0:
    x = int(input("bir sayı girin: "))
    a += x
if x == 0:
    print(a)
"""

""" giriş sistemi
isim = "admin"
sifre = "123"

while input("Kullanıcı adı giriniz: ") != isim:
    print("Kullanıcı adı bulunmamaktadır.")
else:
    while input("Şifre giriniz: ") != sifre:
        print("Şifre yanlış.")
    else:
        print("Başarıylas giriş yapıldı.")
"""