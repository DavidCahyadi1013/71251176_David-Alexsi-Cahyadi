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
    email = pecah[1]
    domain = email.split('@')[1]
    jumlah[domain] = jumlah.get(domain, 0) + 1
print(jumlah)