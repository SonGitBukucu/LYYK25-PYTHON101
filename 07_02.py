fizik = int(input("Fizik ders notu: "))
kimya = int(input("Kimya ders notu: "))
biyoloji = int(input("Biyoloji ders notu: "))

ortalama = (fizik + kimya + biyoloji) / 3
ortalama = round(ortalama, 4)

print(f"ortalama: {ortalama}")

if fizik < 0 or fizik > 100 or kimya < 0 or kimya > 100 or biyoloji < 0 or biyoloji > 100:
    print("Girilen notlarda hata var. Notları tekrar giriniz.")
else:
    print("Notlar geçerli.")
    if ortalama < 50:
        print("Sınıfta kaldınız.")
    elif ortalama == 50:
        print("Hediye kazandınız.")
    else:
        print("Sınıfı geçtiniz.")   

