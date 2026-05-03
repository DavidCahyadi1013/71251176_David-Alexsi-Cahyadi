angka = []

while True:
    sok = input("Masukkan bilangan (ketik 'done' untuk selesai): ")
    if sok == "done":
        break
    angka.append(int(sok))

rata = sum(angka)/len(angka)
print("Rata-rata:",rata)