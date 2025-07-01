pasta = int(input("Kaç kişi pasta yedi? : "))
ekler = int(input("Kaç kişi ekler yedi? : "))
baklava = int(input("Kaç kişi baklava yedi? : "))
tatli =  pasta + ekler + baklava

kandil = int(input("kaç kişi kandil simidi yedi? : "))
sarma = int(input("kaç kişi sarma yedi? : "))
kisir = int(input("kaç kişi kısır yedi? : "))
tuzlu = kandil + sarma + kisir

toplamYiyecek = tatli + tuzlu
tatliYuzde = tatli / toplamYiyecek * 100
tuzluYuzde = tuzlu / toplamYiyecek * 100
baklavaYuzde = baklava / tatli * 100
sarmaYuzde = sarma / tuzlu * 100

print(f"tatlı-tuzlu yüzde oranları: {tatliYuzde} tatlı / {tuzluYuzde} tuzlu ({tatli} tatlı / {tuzlu} tuzlu)")
print(f"tatlılar arasında baklavanın oranı yüzde {baklavaYuzde}")
print(f"tuzlular arasında sarmanın yüzde oranı yüzde {sarmaYuzde}")