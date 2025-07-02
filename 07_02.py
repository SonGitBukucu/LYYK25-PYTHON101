hava = int(input("Hava kaç derece? : "))

if hava <= 40 and hava > 30:
    print("denize gir")
elif hava <= 30 and hava > 20:
    print("dondurma ye")
elif hava <= 20 and hava > 10:
    print("hırka giy")
elif hava <= 10:
    print("mont giy")
else:
    print("hava aşırı sıcak")
