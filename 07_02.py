fizik = int(input("Fizik ders notu: "))
if fizik < 0:
    print("Notlar 0'dan küçük olamaz")
elif fizik > 100:
    print("Notlar 100'den büyük olamaz")
else:
    kimya = int(input("Kimya ders notu: "))
    if kimya < 0:
        print("Notlar 0'dan küçük olamaz")
    elif kimya > 100:
        print("Notlar 100'den büyük olamaz")
    else:
        biyoloji = int(input("Biyoloji ders notu: "))
        if biyoloji < 0:
            print("Notlar 0'dan küçük olamaz")
        elif biyoloji > 100:
            print("Notlar 100'den büyük olamaz")
        else:
            ortalama = (fizik + kimya + biyoloji) / 3
            print("Notlar geçerli.")
            if ortalama < 50:
                print("Sınıfta kaldınız.")
            elif ortalama == 50:
                print("Hediye kazandınız.")
            else:
                print("Sınıfı geçtiniz.") 
