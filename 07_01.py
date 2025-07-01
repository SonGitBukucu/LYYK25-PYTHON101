#dogumYili = int(input("Doğum yılınız: "))
#simdikiYil = 2025

#print(f"{simdikiYil} yılı itibariyle {simdikiYil - dogumYili} yaşındasınız.")

#x = 1
#while x < 501 :
#    print(f"{x}. Merhabalar!")
#    x += 1

#aci1 = int(input("Üçgenin birinci açısı: "))
#aci2 = int(input("Üçgenin ikinci açısı: "))
#aci3 = 180 - (aci1 + aci2)

#if aci3 < 0:
#    print(f"Hatalı açı girdiniz. Üçüncü açı değeri: {aci3} derece")
#else :
#    print(f"üçgende birinci açı {aci1} derece, ikinci açı {aci2} derece ise üçüncü açı {aci3} derecedir.")

kisiSayisi = int(input("etkinlikte kaç kişi var? : "))
erkekSayisi = int(input("etkinlikte kaç erkek var? : "))
kadinSayisi = kisiSayisi - erkekSayisi
print(f"Etkinlikte {kadinSayisi} tane kadın var.")

print(f"etkinlikteki erkeklerin yüzde oranı: {erkekSayisi/kisiSayisi*100}, kadınların yüzde oranı: {kadinSayisi/kisiSayisi*100} ")