#Latihan 7.3
t = int(input("Masukkan tinggi: "))
l = int(input("Masukkan lebar: "))

kosong = 1

for i in range (1, t +1):
    for i in range (1, l + 1):
        print (kosong, end=' ')
        kosong += 1
    print()