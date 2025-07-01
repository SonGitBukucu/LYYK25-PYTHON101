pasta = int(input("Kaç kişi pasta istiyor? : "))
ekler = int(input("Kaç kişi ekler istiyor? : "))
baklava = int(input("Kaç kişi baklava istiyor? : "))
tatli =  pasta + ekler + baklava

kandil = int(input("kaç kişi kandil simidi istiyor? : "))
sarma = int(input("kaç kişi sarma istiyor? : "))
kisir = int(input("kaç kişi kısır istiyor? : "))
tuzlu = kandil + sarma + kisir

toplamYiyecek = tatli + tuzlu
tatliYuzde = tatli / toplamYiyecek * 100
tuzluYuzde = tuzlu / toplamYiyecek * 100
baklavaYuzde = baklava / tatli * 100
sarmaYuzde = sarma / tuzlu * 100

print(f"tatlı-tuzlu yüzde oranları: {tatliYuzde} tatlı / {tuzluYuzde} tuzlu")
print(f"tatlılar arasında baklavanın oranı yüzde {baklavaYuzde}")
print(f"tuzlular arasında sarmanın yüzde oranı yüzde {sarmaYuzde}")