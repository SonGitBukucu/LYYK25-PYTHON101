fizik = int(input("Fizik ders notu: "))
kimya = int(input("Kimya ders notu: "))
biyoloji = int(input("Biyoloji ders notu: "))

ortalama = (fizik + kimya + biyoloji) / 3
ortalama = round(ortalama, 2)

print(ortalama)

if ortalama < 0:
    print("Girilen notlar negatif olamaz.")
elif ortalama > 100:
    print("Girilen notlar 100'den büyük olamaz.")
else:
    print("Notlar geçerli.")

    if ortalama < 50:
        print("Sınıfta kaldın.")
    elif ortalama == 50:
        print("Hediye kazandınız.")
    else:
        print("Sınıfı geçtin.")

#gün bitti