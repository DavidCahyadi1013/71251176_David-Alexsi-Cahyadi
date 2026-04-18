k = input ("Masukkan kalimat : ")
k= k.lower()
pecah = k.split()

pendek = pecah[0]
panjang = pecah [0]

for i in pecah:
    if len (i) < len (pendek):
        pendek = i
    if len(i) > len (panjang):
        panjang = i
print(f"terpendek: {pendek}")
print(f"terpanjang: {panjang}")