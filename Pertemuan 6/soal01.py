#Latihan 6.1
def perkalian(a,b):
    hasil = 0
    proses = ""

    for i in range(a):
        hasil = hasil + b
        proses += str(b)
        if i < a - 1:
            proses += " + "

    print(f"{a} x {b} = {proses} = {hasil}")


a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

perkalian(a,b)