#Latihan 6.2
def ganjil(bawah, atas):
    if bawah < atas:
        print(f"bawah = {bawah}, atas = {atas}. Karena bawah < atas, berarti dari kecil ke besar, maka hasilnya adalah:", end=" ")
        nentu = True
        for i in range(bawah, atas + 1):
            if i % 2 != 0:
                if not nentu:
                    print(", ", end="")
                print(i, end="")
                nentu = False
    
    else:
        print(f"bawah = {bawah}, atas = {atas}. Karena bawah > atas, berarti dari besar ke kecil, maka hasilnya adalah:", end=" ")
        nentu = True
        for i in range(bawah, atas -1, -1):
            if i % 2 != 0:
                if not nentu:
                    print(", ", end="")
                print(i, end='')
                nentu = False

bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))

ganjil(bawah,atas)