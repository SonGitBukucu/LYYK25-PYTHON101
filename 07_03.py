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
        print("Başarıyla giriş yapıldı.")
"""

""" 5 girince geri sayma (döngülü mü emin olamadım ama döngülü yaptım yine de)
while int(input("Bir sayı girin: ")) != 5:
    print("Başka bir sayı girin (5 deneyin bence): ")
else:
    for i in range(0, 6):
        print(5 - i)
"""