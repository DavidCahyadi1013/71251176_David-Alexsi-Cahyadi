nf = input("Masukkan nama file : ")
try:
    buka = open(nf)
except FileNotFoundError:
    print("File tidak bisa dibuka:",nf)
    exit()
jumlah = dict()

for baris in buka:
    if not baris.startswith('From '):
        continue
    pecah = baris.split()
    alamat = pecah[1]
    jumlah[alamat] = jumlah.get(alamat, 0) + 1
print(jumlah)