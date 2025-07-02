dersNot = int(input("not giriniz : "))
devamsizlik = int(input("kaç gün devamsızlığınız var? : "))

if devamsizlik < 10:
    if dersNot >= 85 and dersNot <= 100:
        print("Takdir belgesi aldınız.")
    elif dersNot < 85 and dersNot >= 70:
        print("Teşekkür belgesi aldınız.")
    else:
        print("Hiçbir belge alamadınız.")
else:
    print("Hiçbir belge alamadınız.")