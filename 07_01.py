cayFiyat = 20
kahveFiyat = 50

caySayi = int(input("Kaç bardak çay istersiniz: "))
kahveSayi = int(input("Kaç bardak kahve istersiniz: "))

cayToplam = cayFiyat * caySayi
kahveToplam = kahveFiyat * kahveSayi
total = cayToplam + kahveToplam

print(f"{caySayi} bardak çay toplam {cayFiyat}*{caySayi} = {cayToplam}TL")
print(f"{kahveSayi} bardak kahve toplam {kahveFiyat}*{kahveSayi} = {kahveToplam}TL")
print(f"Toplam tutar: {cayToplam} + {kahveToplam} = {total}TL ")
