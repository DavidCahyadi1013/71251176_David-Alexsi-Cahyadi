#Latihan 6.2
def ganjil (bawah,atas):
    hasil = []

    if bawah < atas:
        for i in range(bawah, atas + 1):
            if i % 2 != 0:
                hasil.append(i)
    else:
        for i in range(bawah, atas - 1, -1):
            if i % 2 != 0:
                hasil.append(i)
    
    print("Hasil:", end=" ")
    for i in range(len(hasil)):
        if i < len(hasil) - 1:
            print(hasil[i], end=", ")
        else:
            print(hasil[i])
    
    bawah = int(input("Masukkan batas bawah: "))
    atas = int(input("Masukkan batas bawah: "))

    ganjil(bawah,atas)