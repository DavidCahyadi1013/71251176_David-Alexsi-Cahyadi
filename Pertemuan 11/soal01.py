def terbaik(data):
    k = list(set(data))
    k.sort(reverse=True)
    return k[:3]

angka = []
n = int(input("Input jumlah bilangan: "))
for i in range (n):
    bil = int(input(f"Masukkan bilangan ke-{i+1}: "))
    angka.append(bil)

akhir = terbaik(angka)
print("3 bilangan terbaik:",akhir)