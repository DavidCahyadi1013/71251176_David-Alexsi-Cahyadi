#Latihan 6.1
def perkalian(a,b):
    hasil = 0
    proses = ""

    for i in range(a):
        hasil = a * b
        proses += str(b)
        if i < a - 1:
            proses += " + "

    print(f"{a} x {b} = {proses} = {hasil}")


perkalian(6, 5)
perkalian(7, 10)