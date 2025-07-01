fizik = int(input("Fizik ders notu: "))
kimya = int(input("Kimya ders notu: "))
biyoloji = int(input("Biyoloji ders notu: "))

ortalama = (fizik + kimya + biyoloji) / 3
ortalama = round(ortalama, 2)

print(ortalama)

if ortalama < 50:
    print("Sınıfta kaldın.")
elif ortalama == 50:
    print("Ortalamanız 50, hediye kazandınız.")
else:
    print(f"Sınıfı geçtin.")