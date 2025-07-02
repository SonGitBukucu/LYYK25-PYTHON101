""" sıfır girilene kadar girilen değerleri toplayıp yazdır
x = int(input("bir sayı girin: "))

a = x

while x != 0:
    x = int(input("bir sayı girin: "))
    a += x
if x == 0:
    print(a)
"""