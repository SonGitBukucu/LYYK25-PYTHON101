#girilen 3 ders notu, ortalama bul, 50 < ise sınıfta kal, büyükse geç

fizik = int(input("Fizik ders notu: "))
kimya = int(input("Kimya ders notu: "))
biyoloji = int(input("biyoloji ders notu: "))

ortalama = (fizik + kimya + biyoloji) / 3

if ortalama < 50:
    print(f"Ortalaman {ortalama}, sınıfta kaldın.")
else:
    print(f"Sınıfı geçtin. Ortalaman {ortalama}.")